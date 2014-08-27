## -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EffectiveSettings data structure
##----------------------------------------------------------------------
## Copyright (C) 2007-2014 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

class EffectiveSettings(object):
    def __init__(self, metric=None, metric_type=None, is_active=True,
                 storage_rule=None, probe=None, interval=None,
                 thresholds=None, handler=None, config=None,
                 errors=None):
        """
        :param metric: Graphite metric name
        :param metric_type: MetricType object
        :param is_active: Activity mark
        :param storage_rule: StorageRule object
        :param probe: Probe object
        :param interval: Polling interval, seconds
        :param thresholds: [low_error, low_warn, high_warn, high_error
        :param handler: Name of probe's handler to use
        :param config: dict of config
        :param errors: list of errors
        """
        self.metric = metric
        self.metric_type = metric_type
        self.is_active = is_active
        self.storage_rule = storage_rule
        self.probe = probe
        self.interval = interval
        self.thresholds = thresholds
        self.handler = handler
        self.config = config
        self.errors = errors or []
        self.traces = []

    def dump(self):
        r = []
        for n in ["metric", "metric_type", "is_active", "storage_rule",
                  "probe", "interval", "thresholds", "handler",
                  "config", "errors", "traces"]:
            r += ["%s='%s'" % (n, getattr(self, n))]
        return " ".join(r)

    def error(self, msg):
        self.errors += [msg]

    def trace(self, msg):
        self.traces += [msg]
