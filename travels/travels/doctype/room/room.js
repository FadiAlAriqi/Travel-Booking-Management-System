frappe.ui.form.on("Room", {
    after_save(frm) {
        if (frm.doc.hotel) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Hotel",
                    name: frm.doc.hotel,
                },
                callback: function (response) {
                    if (response.message) {
                        let hotel = response.message;

                        let room_exists = hotel.rooms.some(row => row.rooms === frm.doc.name);

                        if (!room_exists) {
                            hotel.rooms.push({
                                rooms: frm.doc.name,   
                            });

                            frappe.call({
                                method: "frappe.client.save",
                                args: {
                                    doc: hotel,
                                },
                                callback: function (save_response) {
                                    if (!save_response.exc) {
                                        frappe.msgprint(__("Done"));
                                        frappe.set_route("Form", "Hotel", frm.doc.hotel);

                                    }
                                },
                            });
                        } else {
                            frappe.msgprint(__("This room is already linked to the hotel."));
                        }
                    }
                },
            });
        }
    },
});
