// Copyright (c) 2024, rahul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rider order", {
	onload(frm) {
        console.log("running load...");
    },
    setup(frm) {
        console.log("setup...")
    },
    refresh(frm) {
        console.log("on refresh...")

        if (frm.doc.status !== "Accepted"){
            
            frm.add_custom_button("Accept", () => {
                // status => Accepted
                frm.set_value("status", "Accepted");
                // Save the form
                frm.save();
            } )
        }
 	},
 });
