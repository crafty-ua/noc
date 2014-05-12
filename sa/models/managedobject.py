# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## ManagedObject
##----------------------------------------------------------------------
## Copyright (C) 2007-2013 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import os
import re
import difflib
from collections import namedtuple
## Django modules
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.models import User, Group
## NOC modules
from administrativedomain import AdministrativeDomain
from authprofile import AuthProfile
from managedobjectprofile import ManagedObjectProfile
from activator import Activator
from collector import Collector
from objectstatus import ObjectStatus
from objectmap import ObjectMap
from terminationgroup import TerminationGroup
from noc.main.models import PyRule
from noc.main.models.notificationgroup import NotificationGroup
from noc.sa.profiles import profile_registry
from noc.lib.fields import INETField, TagsField
from noc.lib.app.site import site
from noc.sa.protocols.sae_pb2 import TELNET, SSH, HTTP
from noc.lib.stencil import stencil_registry
from noc.lib.gridvcs.manager import GridVCSField
from noc.main.models.fts_queue import FTSQueue
from noc.settings import config

scheme_choices = [(TELNET, "telnet"), (SSH, "ssh"), (HTTP, "http")]

CONFIG_MIRROR = config.get("gridvcs", "mirror.sa.managedobject.config") or None
Credentials = namedtuple("Credentials", [
    "user", "password", "super_password", "snmp_ro", "snmp_rw"])

class ManagedObject(models.Model):
    """
    Managed Object
    """

    class Meta:
        verbose_name = _("Managed Object")
        verbose_name_plural = _("Managed Objects")
        db_table = "sa_managedobject"
        app_label = "sa"
        ordering = ["name"]

    name = models.CharField(_("Name"), max_length=64, unique=True)
    is_managed = models.BooleanField(_("Is Managed?"), default=True)
    administrative_domain = models.ForeignKey(AdministrativeDomain,
            verbose_name=_("Administrative Domain"))
    activator = models.ForeignKey(Activator,
            verbose_name=_("Activator"),
            limit_choices_to={"is_active": True})
    collector = models.ForeignKey(Collector,
            verbose_name=_("Collector"),
            limit_choices_to={"is_active": True}, null=True, blank=True)
    profile_name = models.CharField(_("SA Profile"),
            max_length=128, choices=profile_registry.choices)
    object_profile = models.ForeignKey(ManagedObjectProfile,
        verbose_name=_("Object Profile"))
    description = models.CharField(_("Description"),
            max_length=256, null=True, blank=True)
    # Access
    auth_profile = models.ForeignKey(
        AuthProfile, verbose_name="Auth Profile", null=True, blank=True)
    scheme = models.IntegerField(_("Scheme"), choices=scheme_choices)
    address = models.CharField(_("Address"), max_length=64)
    port = models.IntegerField(_("Port"), blank=True, null=True)
    user = models.CharField(_("User"), max_length=32, blank=True, null=True)
    password = models.CharField(_("Password"),
            max_length=32, blank=True, null=True)
    super_password = models.CharField(_("Super Password"),
            max_length=32, blank=True, null=True)
    remote_path = models.CharField(_("Path"),
            max_length=256, blank=True, null=True)
    trap_source_ip = INETField(_("Trap Source IP"), null=True,
            blank=True, default=None)
    trap_community = models.CharField(_("Trap Community"),
            blank=True, null=True, max_length=64)
    snmp_ro = models.CharField(_("RO Community"),
            blank=True, null=True, max_length=64)
    snmp_rw = models.CharField(_("RW Community"),
            blank=True, null=True, max_length=64)
    #
    vc_domain = models.ForeignKey(
        "vc.VCDomain", verbose_name="VC Domain", null=True, blank=True)
    # CM
    config = GridVCSField("config", mirror=CONFIG_MIRROR)
    # Default VRF
    vrf = models.ForeignKey("ip.VRF", verbose_name=_("VRF"),
                            blank=True, null=True)
    # For service terminators
    # Name of service termination group (i.e. BRAS, SBC)
    termination_group = models.ForeignKey(
        TerminationGroup, verbose_name=_("Termination Group"),
        blank=True, null=True,
        related_name="termination_set"
    )
    # For access switches -- L3 terminator
    service_terminator = models.ForeignKey(
        TerminationGroup, verbose_name=_("Service termination"),
        blank=True, null=True,
        related_name="access_set"
    )
    # Stencils
    shape = models.CharField(_("Shape"), blank=True, null=True,
        choices=stencil_registry.choices, max_length=128)
    # pyRules
    config_filter_rule = models.ForeignKey(PyRule,
            verbose_name="Config Filter pyRule",
            limit_choices_to={"interface": "IConfigFilter"},
            null=True, blank=True,
            on_delete=models.SET_NULL,
            related_name="managed_object_config_filter_rule_set")
    config_diff_filter_rule = models.ForeignKey(PyRule,
            verbose_name=_("Config Diff Filter Rule"),
            limit_choices_to={"interface": "IConfigDiffFilter"},
            null=True, blank=True,
            on_delete=models.SET_NULL,
            related_name="managed_object_config_diff_rule_set")
    config_validation_rule = models.ForeignKey(PyRule,
            verbose_name="Config Validation pyRule",
            limit_choices_to={"interface": "IConfigValidator"},
            null=True, blank=True,
            on_delete=models.SET_NULL,
            related_name="managed_object_config_validation_rule_set")
    max_scripts = models.IntegerField(_("Max. Scripts"),
            null=True, blank=True,
            help_text=_("Concurrent script session limits"))
    #
    tags = TagsField(_("Tags"), null=True, blank=True)

    # Use special filter for profile
    profile_name.existing_choices_filter = True

    # Event ids
    EV_CONFIG_CHANGED = "config_changed"  # Object's config changed
    EV_ALARM_RISEN = "alarm_risen"  # New alarm risen
    EV_ALARM_REOPENED = "alarm_reopened"  # Alarm has been reopen
    EV_ALARM_CLEARED = "alarm_cleared"  # Alarm cleared
    EV_ALARM_COMMENTED = "alarm_commented"  # Alarm commented
    EV_NEW = "new"  # New object created
    EV_DELETED = "deleted"  # Object deleted
    EV_VERSION_CHANGED = "version_changed"  # Version changed
    EV_INTERFACE_CHANGED = "interface_changed"  # Interface configuration changed
    EV_SCRIPT_FAILED = "script_failed"  # Script error
    EV_CONFIG_POLICY_VIOLATION = "config_policy_violation"  # Policy violations found

    ## object.scripts. ...
    class ScriptsProxy(object):
        class CallWrapper(object):
            def __init__(self, obj, name):
                self.name = name
                self.object = obj

            def __call__(self, **kwargs):
                task = ReduceTask.create_task(
                    [self.object],
                    reduce_object_script, {},
                    self.name, kwargs, None
                )
                return task.get_result(block=True)

        def __init__(self, obj):
            self._object = obj
            self._cache = {}

        def __getattr__(self, name):
            if name in self._cache:
                return self._cache[name]
            if name not in self._object.profile.scripts:
                raise AttributeError(name)
            cw = ManagedObject.ScriptsProxy.CallWrapper(self._object, name)
            self._cache[name] = cw
            return cw

    def __init__(self, *args, **kwargs):
        super(ManagedObject, self).__init__(*args, **kwargs)
        self.scripts = ManagedObject.ScriptsProxy(self)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return site.reverse("sa:managedobject:change", self.id)

    @property
    def profile(self):
        """
        Get object's profile instance. Instances are cached. Same profile's
        instance will be returned for all .profile invocations for
        given managed objet

        :rtype: Profile instance
        """
        try:
            return self._cached_profile
        except AttributeError:
            self._cached_profile = profile_registry[self.profile_name]()
            return self._cached_profile

    @classmethod
    def user_objects(cls, user):
        """
        Get objects available to user

        :param user: User
        :type user: User instance
        :rtype: Queryset instance
        """
        return cls.objects.filter(UserAccess.Q(user))

    def has_access(self, user):
        """
        Check user has access to object

        :param user: User
        :type user: User instance
        :rtype: Bool
        """
        if user.is_superuser:
            return True
        return self.user_objects(user).filter(id=self.id).exists()

    @property
    def granted_users(self):
        """
        Get list of user granted access to object

        :rtype: List of User instancies
        """
        return [u for u in User.objects.filter(is_active=True)
                if ManagedObject.objects.filter(UserAccess.Q(u) &
                                                Q(id=self.id)).exists()]

    @property
    def granted_groups(self):
        """
        Get list of groups granted access to object

        :rtype: List of Group instancies
        """
        return [g for g in Group.objects.filter()
                if ManagedObject.objects.filter(GroupAccess.Q(g) &
                                                Q(id=self.id)).exists()]

    def save(self):
        """
        Overload model's save()
        """
        # Get previous version
        if self.id:
            old = ManagedObject.objects.get(id=self.id)
        else:
            old = None
        # Save
        super(ManagedObject, self).save()
        # IPAM sync
        if self.object_profile.sync_ipam:
            self.sync_ipam()
        # Notify changes
        if ((old is None and self.trap_source_ip) or
            (old and self.trap_source_ip != old.trap_source_ip) or
            (old and self.activator.id != old.activator.id)):
            self.sae_refresh_event_filter()
        # Notify new object
        if old is None:
            SelectorCache.rebuild_for_object(self)
            self.event(self.EV_NEW, {"object": self})
        if not self.collector or not self.trap_source_ip:
            # Remove from object mappings
            ObjectMap.delete_map(self)
        else:
            # Add to object mappings
            ObjectMap.update_map(
                self, self.collector, self.trap_source_ip)

    def delete(self, *args, **kwargs):
        # Deny to delete "SAE" object
        if self.name == "SAE":
            raise IntegrityError("Cannot delete SAE object")
        super(ManagedObject, self).delete(*args, **kwargs)

    def sync_ipam(self):
        """
        Synchronize FQDN and address with IPAM
        """
        from noc.ip.models.address import Address
        from noc.ip.models.vrf import VRF
        # Generate FQDN from template
        fqdn = self.object_profile.get_fqdn(self)
        # Get existing IPAM record
        vrf = self.vrf if self.vrf else VRF.get_global()
        try:
            a = Address.objects.get(vrf=vrf, address=self.address)
        except Address.DoesNotExist:
            # Create new address
            Address(
                vrf=vrf,
                address=self.address,
                fqdn=fqdn,
                managed_object=self
            ).save()
            return
        # Update existing address
        if (a.managed_object != self or
            a.address != self.address or a.fqdn != fqdn):
            a.managed_object = self
            a.address = self.address
            a.fqdn = fqdn
            a.save()

    def get_index(self):
        """
        Get FTS index
        """
        card = "Managed object %s (%s)" % (self.name, self.address)
        content = [
            self.name,
            self.address,
        ]
        if self.trap_source_ip:
            content += [self.trap_source_ip]
        platform = self.platform
        if platform:
            content += [platform]
            card += " [%s]" % platform
        version = self.get_attr("version")
        if version:
            content += [version]
            card += " version %s" % version
        if self.description:
            content += [self.description]
        config = self.config.read()
        if config:
            content += [config]
        r = {
            "id": "sa.managedobject:%s" % self.id,
            "title": self.name,
            "content": "\n".join(content),
            "card": card
        }
        if self.tags:
            r["tags"] = self.tags
        return r

    def get_search_info(self, user):
        if self.has_access(user):
            return ("sa.managedobject", "history", {"args": [self.id]})
        else:
            return None

    ##
    ## Returns True if Managed Object presents in more than one networks
    ## @todo: Rewrite
    ##
    @property
    def is_router(self):
        return self.address_set.count() > 1

    ##
    ## Return attribute as string
    ##
    def get_attr(self, name, default=None):
        try:
            return self.managedobjectattribute_set.get(key=name).value
        except ManagedObjectAttribute.DoesNotExist:
            return default

    ##
    ## Return attribute as bool
    ##
    def get_attr_bool(self, name, default=False):
        v = self.get_attr(name)
        if v is None:
            return default
        if v.lower() in ["t", "true", "y", "yes", "1"]:
            return True
        else:
            return False

    ##
    ## Return attribute as integer
    ##
    def get_attr_int(self, name, default=0):
        v = self.get_attr(name)
        if v is None:
            return default
        try:
            return int(v)
        except:
            return default

    ##
    ## Set attribute
    ##
    def set_attr(self, name, value):
        value = unicode(value)
        try:
            v = self.managedobjectattribute_set.get(key=name)
            v.value = value
        except ManagedObjectAttribute.DoesNotExist:
            v = ManagedObjectAttribute(managed_object=self,
                                       key=name, value=value)
        v.save()

    @property
    def platform(self):
        """
        Return "vendor model" string from attributes
        """
        x = [self.get_attr("vendor"), self.get_attr("platform")]
        x = [a for a in x if a]
        if x:
            return " ".join(x)
        else:
            return None

    def is_ignored_interface(self, interface):
        interface = self.profile.convert_interface_name(interface)
        rx = self.get_attr("ignored_interfaces")
        if rx:
            return re.match(rx, interface) is not None
        return False

    def sae_refresh_event_filter(self):
        """
        Refresh event filters for all activators serving object
        """
        def reduce_notify(task):
            mt = task.maptask_set.all()[0]
            if mt.status == "C":
                return mt.script_result
            return False

        ReduceTask.create_task(
            "SAE",
            reduce_notify, {},
            "notify", {
                "event": "refresh_event_filter",
                "object_id": self.id},
            1
        )

    def get_status(self):
        return ObjectStatus.get_status(self)

    def set_status(self, status):
        ObjectStatus.set_status(self, status)

    def get_inventory(self):
        """
        Retuns a list of inventory Objects managed by
        this managed object
        """
        from noc.inv.models.object import Object
        return list(Object.objects.filter(
            data__management__managed_object=self.id))

    def run_discovery(self, delta=0):
        op = self.object_profile
        for attr, job, duration in [
            ("enable_version_inventory", "version_inventory", 1),
            ("enable_id_discovery", "id_discovery", 1),
            ("enable_config_polling", "config_discovery", 1),
            ("enable_interface_discovery", "interface_discovery", 1),
            ("enable_asset_discovery", "asset_discovery", 1),
            ("enable_vlan_discovery", "vlan_discovery", 1),
            ("enable_lldp_discovery", "lldp_discovery", 1),
            ("enable_udld_discovery", "udld_discovery", 1),
            ("enable_bfd_discovery", "bfd_discovery", 1),
            ("enable_stp_discovery", "stp_discovery", 1),
            ("enable_cdp_discovery", "cdp_discovery", 1),
            ("enable_oam_discovery", "oam_discovery", 1),
            ("enable_rep_discovery", "rep_discovery", 1),
            ("enable_ip_discovery", "ip_discovery", 1),
            ("enable_mac_discovery", "mac_discovery", 1)
        ]:
            if getattr(op, attr):
                refresh_schedule(
                    "inv.discovery", job, self.id, delta=delta)
                delta += duration

    def event(self, event_id, data=None, delay=None, tag=None):
        """
        Process object-related event
        :param event_id: ManagedObject.EV_*
        :param data: Event context to render
        :param delay: Notification delay in seconds
        :param tag: Notification tag
        """
        # Get cached selectors
        selectors = SelectorCache.get_object_selectors(self)
        # Find notification groups
        groups = set()
        for o in ObjectNotification.objects.filter(**{
            event_id: True,
            "selector__in": selectors}):
            groups.add(o.notification_group)
        if not groups:
            return  # Nothing to notify
        # Render message
        subject, body = ObjectNotification.render_message(event_id, data)
        # Send notification
        if not tag and event_id in (
                self.EV_ALARM_CLEARED,
                self.EV_ALARM_COMMENTED,
                self.EV_ALARM_REOPENED,
                self.EV_ALARM_RISEN) and "alarm" in data:
            tag = "alarm:%s" % data["alarm"].id
        NotificationGroup.group_notify(
            groups, subject=subject, body=body, delay=delay, tag=tag)
        # Schedule FTS reindex
        if event_id in (
            self.EV_CONFIG_CHANGED, self.EV_VERSION_CHANGED):
            FTSQueue.schedule_update(self)

    def save_config(self, data):
        if isinstance(data, list):
            # Convert list to plain text
            r = []
            for d in sorted(data, lambda x, y: cmp(x["name"], y["name"])):
                r += ["==[ %s ]========================================\n%s" % (d["name"], d["config"])]
            data = "\n".join(r)
        # Pass data through config filter, if given
        if self.config_filter_rule:
            data = self.config_filter_rule(
                managed_object=self, config=data)
        # Pass data through the validation filter, if given
        if self.config_validation_rule:
            warnings = self.config_validation_rule(
                managed_object=self, config=data)
            if warnings:
                # There are some warnings. Notify responsible persons
                self.event(
                    self.EV_CONFIG_POLICY_VIOLATION,
                    {
                        "object": self,
                        "warnings": warnings
                    }
                )
        # Calculate diff
        old_data = self.config.read()
        is_new = not bool(old_data)
        diff = None
        if not is_new:
            # Calculate diff
            if self.config_diff_filter_rule:
                # Pass through filters
                old_data = self.config_diff_filter_rule(
                    managed_object=self, config=old_data)
                new_data = self.config_diff_filter_rule(
                    managed_object=self, config=data)
            else:
                new_data = data
            if old_data == new_data:
                return  # Nothing changed
            diff = "".join(difflib.unified_diff(
                old_data.splitlines(True),
                new_data.splitlines(True),
                fromfile=os.path.join("a", self.name.encode("utf8")),
                tofile=os.path.join("b", self.name.encode("utf8"))
            ))
        # Notify changes
        self.event(
            self.EV_CONFIG_CHANGED,
            {
                "object": self,
                "is_new": is_new,
                "config": data,
                "diff": diff
            }
        )
        # Save config
        self.config.write(data)

    @property
    def credentials(self):
        """
        Get effective credentials
        """
        if self.auth_profile:
            return Credentials(
                user=self.auth_profile.user,
                password=self.auth_profile.password,
                super_password=self.auth_profile.super_password,
                snmp_ro=self.auth_profile.snmp_ro,
                snmp_rw=self.auth_profile.snmp_rw
            )
        else:
            return Credentials(
                user=self.user,
                password=self.password,
                super_password=self.super_password,
                snmp_ro=self.snmp_ro,
                snmp_rw=self.snmp_rw
            )

    @property
    def scripts_limit(self):
        ol = self.max_scripts or None
        pl = self.profile.max_scripts
        if not ol:
            return pl
        if pl:
            return min(ol, pl)
        else:
            return ol


class ManagedObjectAttribute(models.Model):

    class Meta:
        verbose_name = _("Managed Object Attribute")
        verbose_name_plural = _("Managed Object Attributes")
        db_table = "sa_managedobjectattribute"
        app_label = "sa"
        unique_together = [("managed_object", "key")]
        ordering = ["managed_object", "key"]

    managed_object = models.ForeignKey(ManagedObject,
            verbose_name=_("Managed Object"))
    key = models.CharField(_("Key"), max_length=64)
    value = models.CharField(_("Value"), max_length=4096,
            blank=True, null=True)

    def __unicode__(self):
        return u"%s: %s" % (self.managed_object, self.key)

## Avoid circular references
from reducetask import ReduceTask, reduce_object_script
from useraccess import UserAccess
from groupaccess import GroupAccess
from noc.lib.scheduler.utils import refresh_schedule
#from noc.vc.models.vcdomain import VCDomain
from objectnotification import ObjectNotification
from selectorcache import SelectorCache
