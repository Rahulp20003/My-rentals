# Copyright (c) 2024, rahul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class test1(Document):
	def validate(self):
		for item in self.items:
			item.total = item.a + item.b + item.c

		grand_total = 0
		for item in self.items:
			total = item.total
			grand_total += total	
		
		
		self.subtotal = grand_total
