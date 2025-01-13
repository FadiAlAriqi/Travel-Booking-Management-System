frappe.ui.form.on("Ticket", {
    after_save(frm) {
        if (frm.doc.related_ticket && frm.doc.related_ticket.length > 0) {
            frm.doc.related_ticket.forEach(row => {
                frappe.call({
                    method: "frappe.client.get",
                    args: {
                        doctype: "Ticket",
                        name: row.ticket,
                    },
                    callback: function(response) {
                        if (response.message) {
                            let related_ticket = response.message;

                            // تحديث الحقول في التذكرة المرتبطة
                            related_ticket.parent_ticket = frm.doc.name; // تعيين اسم التذكرة الأب
                            related_ticket.is_dependent = 1; // تعيين is_dependent إلى Checked (1)

                            // حفظ التغييرات
                            frappe.call({
                                method: "frappe.client.save",
                                args: {
                                    doc: related_ticket,
                                },
                                callback: function(save_response) {
                                    if (!save_response.exc) {
                                        frappe.msgprint(__(`Related Ticket ${row.ticket} has been updated.`));
                                    }
                                }
                            });
                        }
                    }
                });
            });
        }
    }
});
