// Copyright (c) 2024, rahul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride booking", {
	refresh(frm) {
      
	},

    rate(frm){
        // recalculate
    },
 });


 frappe.ui.form.on('Ride Booking Item', {
    refresh(frm) {
        // your code here
    },
    distance(frm, cdt, cdn) {
        let total_d = 0
      for(let item of frm.doc.items){
        console.log(item.distance)
      }
    }
 })
