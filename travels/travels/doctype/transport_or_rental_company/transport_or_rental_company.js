// Copyright (c) 2025, YemenFrappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Transport or Rental Company", {
	refresh(frm) {

        // if (frm.doc.docstatus === 1) {
            if (!frm.custom_buttons['Payment']) {
                frm.add_custom_button(__('Payment'), function() {
                    frappe.msgprint(__('Processing Payment...'));
                    frappe.call({
                        method: "travels.api.make_payment_entry_from_hotel",
                        args: {
                            source_name: frm.doc.name
                        },
                        callback: function (r) {
                            if (r.message) {
                                frappe.model.sync(r.message);
                                frappe.set_route("Form", r.message.doctype, r.message.name);
                            }
                        }
                    });
                });
            }
        // }
	},
});
