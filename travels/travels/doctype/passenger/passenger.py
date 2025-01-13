# Copyright (c) 2025, YemenFrappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Passenger(Document):
	def before_save(self):
		self.full_name = f'{self.given_names} {self.surname or ""}'