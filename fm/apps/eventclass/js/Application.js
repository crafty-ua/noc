//---------------------------------------------------------------------
// fm.eventclass application
//---------------------------------------------------------------------
// Copyright (C) 2007-2013 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.fm.eventclass.Application");

Ext.define("NOC.fm.eventclass.Application", {
    extend: "NOC.core.ModelApplication",
    uses: [
        "NOC.fm.eventclass.Model"
    ],
    model: "NOC.fm.eventclass.Model",
    search: true,
    columns: [
        {
            text: "Name",
            dataIndex: "name",
            width: 250
        },
        {
            text: "Builtin",
            dataIndex: "is_builtin",
            renderer: NOC.render.Bool,
            width: 30
        },
        {
            text: "Description",
            dataIndex: "description",
            flex: 1
        }
    ],
    fields: [
        {
            name: "name",
            xtype: "textfield",
            fieldLabel: "Name",
            allowBlank: false
        },
        {
            name: "is_builtin",
            xtype: "checkboxfield",
            boxLabel: "Builtin"
        },
        {
            name: "description",
            xtype: "textarea",
            fieldLabel: "Description"
        }
    ],
    filters: [
        {
            title: "By Builtin",
            name: "is_builtin",
            ftype: "boolean"
        }
    ],
    //
    initComponent: function() {
        var me = this;
        Ext.apply(me, {
            formToolbar: [
                {
                    text: "JSON",
                    iconCls: "icon_page",
                    tooltip: "View as JSON",
                    hasAccess: NOC.hasPermission("read"),
                    scope: me,
                    handler: me.onJSON
                }
            ]
        });
        me.jsonPanel = Ext.create("NOC.core.JSONPreview", {
            app: me,
            restUrl: "/fm/eventclass/{{id}}/json/",
            previewName: "Event Class: {{name}}"
        });
        me.ITEM_JSON = me.registerItem(me.jsonPanel);
        me.callParent();
    },
    //
    onJSON: function() {
        var me = this;
        me.showItem(me.ITEM_JSON);
        me.jsonPanel.preview(me.currentRecord);
    }
});
