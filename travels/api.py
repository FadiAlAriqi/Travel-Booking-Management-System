import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_payment_entry(source_name, target_doc=None):
    def update_item(source, target, source_parent):
        target.party_type = "Customer"
        target.party = source.customer_name
        target.party_name = source.customer_name
        # target.paid_to = source.shipper_name
        # target.paid_from = source.debit_to
        target.payment_type = "Receive"
        # target.custom_total_amount =source.outstanding
        # account_currency = frappe.db.get_value("Account", source.debit_to, "account_currency")
        # target.paid_from_account_currency = account_currency


    doc = get_mapped_doc(
        "Booking Services",  
        source_name,
        {
            "Booking Services": {
                "doctype": "Payment Entry",
                "field_map": {
                    "customer": "party",
                    "total": "paid_amount",
                    
                },
                "postprocess": update_item,
            },
        },
        target_doc
    )

    return doc


# @frappe.whitelist()
# def make_payment_entry_from_hotel(source_name):
#     def update_item(source, target, source_parent):
#         target.party_type = "Supplier"
        
#         # استعراض التشابلد تيبل (hotel) واستخدام البيانات منه
#         for hotel_entry in source.hotel:  # استعراض البيانات داخل الـ hotel child table
#             target.party = hotel_entry.hotel_name  # استخدام اسم الفندق من الـ child table
#             target.party_name = hotel_entry.hotel_name
#             target.payment_type = "Pay"
#             target.paid_amount = hotel_entry.hotel_payable_amount  # إذا كان هناك حقل للمدفوعات في التشابلد تيبل

#     try:
#         # الحصول على البيانات من Booking Services ونسخها إلى Payment Entry
#         doc = get_mapped_doc(
#             "Booking Services",  # اسم الـ DocType الأصلي
#             source_name,
#             {
#                 "Booking Services": {
#                     "doctype": "Payment Entry",  # الـ DocType الهدف
#                     "field_map": {
#                         "customer": "party",  # مثال: ربط حقل العميل بالـ party في Payment Entry
#                         "hotel_payable_amount": "paid_amount",  # ربط حقل المبلغ المدفوع
#                     },
#                     "postprocess": update_item,  # معالجة البيانات بعد النقل
#                 },
#             },
#             target_doc=None  # لا حاجة لتحديد هدف إذا كنت ستقوم بإنشاء الـ doc مباشرة
#         )
#         return doc  # إرجاع الـ Payment Entry المنشأ

#     except Exception as e:
#         frappe.log_error(f"Error while creating payment entry: {str(e)}", "Make Payment Entry Error")
@frappe.whitelist()
def make_payment_entry_from_hotel(source_name, target_doc=None):
    def update_item(source, target, source_parent):
        # تعيين القيم المطلوبة في مستند Payment Entry
        target.party_type = "Supplier"  # نوع الطرف
        target.party = source.hotel  # اسم الفندق كطرف
        target.party_name = source.hotel  # اسم المورد
        target.payment_type = "Pay"  # نوع الدفع
        target.paid_amount = source.hotel_amount  # المبلغ المدفوع
        target.received_amount = 0  # المبلغ المستلم (صفر افتراضيًا)
    
    # استخدام الدالة get_mapped_doc لإنشاء مستند جديد
    doc = get_mapped_doc(
        "Hotel Booking",  # اسم المستند المصدر
        source_name,  # اسم السجل المصدر
        {
            "Hotel Booking": {  # إعدادات الماب
                "doctype": "Payment Entry",  # اسم المستند الهدف
                "field_map": {  # خريطة الحقول
                    "hotel": "party",  # ربط حقل الفندق مع الطرف
                    "hotel_amount": "paid_amount",  # ربط حقل المبلغ المدفوع
                },
                "postprocess": update_item,  # تنفيذ المعالجة بعد النقل
            },
        },
        target_doc
    )

    return doc


@frappe.whitelist()
def make_payment_entry_from_transport_company(source_name, target_doc=None):
    def update_item(source, target, source_parent):
        # تعيين القيم المطلوبة في مستند Payment Entry
        target.party_type = "Supplier"  # نوع الطرف
        target.party = source.company  # اسم الفندق كطرف
        target.party_name = source.company  # اسم المورد
        target.payment_type = "Pay"  # نوع الدفع
        target.paid_amount = source.rental_company_amount  # المبلغ المدفوع
        # target.received_amount = 0  # المبلغ المستلم (صفر افتراضيًا)
    
    # استخدام الدالة get_mapped_doc لإنشاء مستند جديد
    doc = get_mapped_doc(
        "Vehicle Rental",  # اسم المستند المصدر
        source_name,  # اسم السجل المصدر
        {
            "Vehicle Rental": {  # إعدادات الماب
                "doctype": "Payment Entry",  # اسم المستند الهدف
                "field_map": {  # خريطة الحقول
                    "company": "party",  # ربط حقل الفندق مع الطرف
                    "rental_company_amount": "paid_amount",  # ربط حقل المبلغ المدفوع
                },
                "postprocess": update_item,  # تنفيذ المعالجة بعد النقل
            },
        },
        target_doc
    )

    return doc