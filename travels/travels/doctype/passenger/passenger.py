# Copyright (c) 2025, YemenFrappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class Passenger(Document):
    def before_insert(self):
        if self.given_names and self.surname:
            self.full_name = f'{self.given_names} {self.surname}'
        else:
            frappe.throw("Please, fill in the empty fields")

        # إنشاء سجل في Customer
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": self.full_name,
            "mobile_no": self.phone_number,
            "email_id": self.email,
            "customer_type": "Individual",  # يمكنك تخصيص نوع العميل إذا لزم
            # "customer_group": "Individual",  # تأكد من وجود المجموعة أو قم بتغييرها حسب احتياجاتك
            # "territory": "All Territories",  # قم بتحديث هذا بناءً على الإعدادات لديك
        })
        customer.insert(ignore_permissions=True)
        frappe.db.commit()

