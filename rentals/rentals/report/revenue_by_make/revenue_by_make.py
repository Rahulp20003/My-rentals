# Copyright (c) 2024, rahul and contributors
# For license information, please see license.txt
import frappe



def execute(filters=None):

	frappe.errprint(filters)
	print(filters)

	columns = [{
		"fieldname": "make",
		"label": "make",
		"fieldtype": "Data"
	}, {
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldtype": "currency",
		"options": "AED"
	}, ]

	data = frappe.get_all(
		"Ride booking",
		fields=["SUM(total_amount) AS total_revenue", "vehical.make"],
		filters={"docstatus": 1},
		group_by="make"
	)

	chart = {
		"data": {
			"labels": [x.make for x in data],
		"datasets": [{"values": [x.total_revenue for x in data ]}],
		},
		"type": "pie"		
	}
	return columns,data, "message summary", chart