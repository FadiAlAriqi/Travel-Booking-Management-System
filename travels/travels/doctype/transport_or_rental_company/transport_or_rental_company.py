# Copyright (c) 2025, YemenFrappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TransportorRentalCompany(Document):

	def before_save(self):

		existing_supplier = frappe.db.exists("Supplier", {"supplier_name": self.name1})
		if existing_supplier:
			supplier_doc = frappe.get_doc("Supplier", existing_supplier)
			supplier_doc.phone_number = self.phone_number
			supplier_doc.email = self.email
			supplier_doc.country = self.country
			supplier_doc.save()
			# frappe.msgprint(f"Supplier '{self.name1}' updated successfully!")
		else:
			supplier_doc = frappe.get_doc({
				"doctype": "Supplier",
				"supplier_name": self.name1,
				"supplier_group": f'{self.type} Company',
				"phone_number": self.phone_number,
				"email": self.email,
				"country": self.country,
			})
			supplier_doc.insert(ignore_permissions=True)
			# frappe.msgprint(f"Supplier '{self.name1}' created successfully!")