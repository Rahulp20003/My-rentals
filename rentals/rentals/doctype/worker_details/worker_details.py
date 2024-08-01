# Copyright (c) 2024, rahul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class workerdetails(Document):
	def before_save(self):
		parts = []
		if self.first_name:
			parts.append(self.first_name)
		if self.mid_name:
			parts.append(self.mid_name)
		if self.last_name:
			parts.append(self.last_name)
		
		self.full_name = " ".join(parts).strip()


	def before_insert(self):
		self.virtual = f"{self.first_name[0:3]}"

#########

class workerdetails(Document):
	def validate(self):
		for item in self.items:
			item.total = item.a + item.b + item.c

		grand_total = 0
		for item in self.items:
			total = item.total
			grand_total += total	
		
		
		self.subtotal = grand_total

		#######

		# Function to check if amount should be accepted or rejected
