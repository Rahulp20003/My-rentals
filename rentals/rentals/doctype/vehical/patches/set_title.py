import frappe

def execute():
    Vehical = frappe.db.get_all("vehical", pluck="name")
    for v in vehical:
        vehical = frappe.get_doc("vehical",v)
        vehical.set_title()
        vehical.save()

    frappe.db.commit()
