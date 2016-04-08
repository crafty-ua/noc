# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Escalation
##----------------------------------------------------------------------
## Copyright (C) 2007-2016, The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import logging
import cachetools
## NOC modules
from noc.fm.models.utils import get_alarm
from noc.main.models.template import Template
from noc.main.models.notificationgroup import NotificationGroup
from noc.fm.models.ttsystem import TTSystem
from noc.core.tt.base import BaseTTSystem
from noc.sa.models.selectorcache import SelectorCache
from noc.inv.models.extnrittmap import ExtNRITTMap
from noc.fm.models.alarmescalation import AlarmEscalation


logger = logging.getLogger(__name__)


def escalate(alarm_id, escalation_id, escalation_delay):
    def log(message, *args):
        msg = message % args
        logger.info("[%s] %s", alarm_id, msg)
        alarm.log_message(msg, to_save=True)

    logger.info("[%s] Performing escalations", alarm_id)
    alarm = get_alarm(alarm_id)
    if alarm is None:
        logger.info("[%s] Missing alarm, skipping", alarm_id)
        return
    if alarm.status == "C":
        logger.info("[%s] Alarm is closed, skipping", alarm_id)
        return
    if alarm.root:
        log("Alarm is not root cause, skipping")
        return
    #
    escalation = escalation_cache[escalation_id]
    if not escalation:
        log("Escalation %s is not found, skipping", escalation_id)
        return

    # Evaluate escalation chain
    mo = alarm.managed_object
    for a in escalation.escalations:
        if a.delay != escalation_delay:
            continue  # Try other type
        # Check administrative domain
        if (
            a.administrative_domain and
            mo.administrative_domain.id != a.administrative_domain.id
        ):
            continue
        # Check selector
        if a.selector and not SelectorCache.is_in_selector(mo, a.selector):
            continue
        # Render escalation message
        if not a.template:
            log("No escalation template, skipping")
            return

        ctx = {
            "alarm": alarm
        }
        subject = a.template.render_subject(**ctx)
        body = a.template.render_body(**ctx)
        logger.debug("[%s] Escalation message:\nSubject: %s\n%s",
                     alarm_id, subject, body)
        # Send notification
        if a.notification_group:
            log("Sending notification to group %s", a.notification_group.name)
            a.notification_group.notify(subject, body)
        # Escalate to TT
        if a.create_tt:
            if alarm.escalation_tt:
                log(
                    "Already escalated with TT #%s",
                    alarm.escalation_tt
                )
            else:
                # Get external TT system
                d = ExtNRITTMap._get_collection().find_one({
                    "managed_object": mo.id
                })
                if d:
                    tt_system = tt_system_cache[d["tt_system"]]
                    if tt_system:
                        pre_reason = escalation.get_pre_reason(tt_system)
                        if pre_reason is not None:
                            log("Creating TT in system %s", tt_system.name)
                            tts = tt_system.get_system()
                            try:
                                tt_id = tts.create_tt(
                                    queue=d["queue"],
                                    obj=d["remote_id"],
                                    reason=pre_reason,
                                    subject=subject,
                                    body=body,
                                    login="correlator"
                                )
                                alarm.escalate(
                                    "%s:%s" % (tt_system.name, tt_id)
                                )
                            except tts.TTError as e:
                                log("Failed to create TT: %s", e)
                        else:
                            log("Cannot find pre reason")
                    else:
                        log("Cannot find TT system %s", d["tt_system"])
                else:
                    log("Cannot find TT system for %s",
                        alarm.managed_object.name)
        #
        if a.stop_processing:
            logger.debug("[%s] Stopping processing")
            break


def get_item(model, id):
    if not id:
        return None
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        return None

TTL = 60
CACHE_SIZE = 256

escalation_cache = cachetools.TTLCache(
    CACHE_SIZE, TTL, missing=lambda x: get_item(AlarmEscalation, x)
)

tt_system_cache = cachetools.TTLCache(
    CACHE_SIZE, TTL, missing=lambda x: get_item(TTSystem, x)
)