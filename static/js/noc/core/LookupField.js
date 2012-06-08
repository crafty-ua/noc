//---------------------------------------------------------------------
// NOC.core.LookupField -
// Lookup form field
//---------------------------------------------------------------------
// Copyright (C) 2007-2011 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.core.LookupField");

Ext.define("NOC.core.LookupField", {
    extend: "Ext.form.ComboBox",
    displayField: "label",
    valueField: "id",
    queryMode: "remote",
    queryParam: "__query",
    queryCaching: false,
    queryDelay: 200,
    forceSelection: true,
    minChars: 2,
    typeAhead: true,
    triggerAction: "all",
    editable: true,
    query: {},
    stateful: false,
    autoSelect: false,
    pageSize: 0,

    initComponent: function() {
        var me = this,
            sclass = me.__proto__.$className.replace("LookupField",
                                                     "Lookup");
        Ext.applyIf(me, {
            store: Ext.create(sclass)
        });
        if(me.query) {
            Ext.apply(me.store.proxy.extraParams, me.query);
        }
        me.addEvents("clear");
        me.callParent();
        me.on("specialkey", me.onSpecialKey, me, {delay: 100});
    },

    // setValue
    // Value can be
    //    * id (int or string), when loaded from form
    //    * record object, when store loaded
    //    * [record]
    setValue: function(value) {
        var me = this;

        if(me.store.loading) {
            // Value will actually be set
            // by store.load callback.
            // Ignore it now
            return me;
        }
        if(!value || value.length == 0) {
            // Empty value
            return me.callParent([]);
        }
        if(typeof(value) == "object") {
            // Called when item selected from drop-down list
            // can be either
            // * record
            // * [record]
            if(value.length == undefined) {
                return me.callParent([value]);
            } else {
                return me.callParent([value[0]]);
            }
        } else {
            // number or string
            // Start store lookup
            // @todo: do not refresh current value
            me.store.load({
                params: {id: value},
                scope: me,
                callback: function(records, operation, success) {
                    if(success && records.length > 0) {
                        this.setValue(records[0]);
                    }
                }
            });
        }
        return me;
    },

    getLookupData: function() {
        return this.getDisplayValue();
    },

    onSpecialKey: function(field, e) {
        var me = this;
        if(e.keyCode == e.ESC) {
            me.clearValue();
            me.fireEvent("clear");
        }
    }
});
