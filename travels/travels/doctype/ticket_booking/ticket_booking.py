# Copyright (c) 2025, YemenFrappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TicketBooking(Document):
    def calculate_commission_and_total(self, total_ticket_amount, commission_rate):
        """
        حساب مبلغ العمولة والمبلغ المتبقي بعد خصم العمولة.

        :param total_ticket_amount: القيمة الإجمالية للتذكرة
        :param commission_rate: نسبة العمولة (بالنسبة المئوية)
        :return: قاموس يحتوي على مبلغ العمولة والمبلغ المتبقي
        """
        # حساب مبلغ العمولة
        commission_amount = (total_ticket_amount * commission_rate) / 100

        # حساب المبلغ المتبقي بعد خصم العمولة
        total_amount = total_ticket_amount - commission_amount

        # إرجاع النتائج
        return {
            "commission_amount": commission_amount,
            "total_amount": total_amount,
        }

    def validate(self):
        """
        تنفيذ الحسابات عند حفظ المستند.
        """
        # التحقق من القيم الأساسية
        total_ticket_amount = self.total_ticket_amount or 0  # إذا كان الحقل فارغًا، استخدم 0
        commission_rate = self.commission_rate or 0  # إذا كان الحقل فارغًا، استخدم 0

        # استدعاء دالة الحساب
        results = self.calculate_commission_and_total(total_ticket_amount, commission_rate)

        # تحديث الحقول بالقيم المحسوبة
        self.commission_amount = results["commission_amount"]
        self.total_amount = results["total_amount"]


