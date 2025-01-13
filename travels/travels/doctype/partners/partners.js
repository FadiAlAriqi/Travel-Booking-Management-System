// Copyright (c) 2025, YemenFrappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Partners", {
	refresh(frm) {

	},

    onload: function (frm) {
        frm.fields_dict['rental_companies'].grid.get_field('rental_company').get_query = function () {
            return {
                filters: {
                    type: 'Rental'
                }
            };
        };

        frm.fields_dict['transport_companies'].grid.get_field('transport_company').get_query = function () {
            return {
                filters: {
                    type: 'Transport'
                }
            };
        };
    }
});
