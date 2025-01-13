// Copyright (c) 2025, YemenFrappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Car Rental", {
	refresh(frm) {

	},

    company: function (frm) {
        filter_vehicles(frm);
    },
    
    vehicle_type: function (frm) {
        filter_vehicles(frm);
    }
});


function filter_vehicles(frm) {
    const company = frm.doc.company;
    const vehicle_type = frm.doc.vehicle_type;

    let filters = {};

    if (company) {
        filters["company"] = company;
    }

    if (vehicle_type && vehicle_type !== '') {
        filters["type"] = vehicle_type;
    }

    frm.set_query('vehicle', function () {
        return {
            filters: filters
        };
    });
}
