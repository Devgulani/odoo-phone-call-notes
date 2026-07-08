from odoo import models, fields

class PhoneCallLog(models.Model):
    _name = "phone.call.log"
    _description = "Phone Call Log"

    def _default_user(self):
        return self.env.user

    partner_id = fields.Many2one(
        "res.partner", 
        string = "Customer",
        required = True
    )

    phone = fields.Char(
        string = "Phone Number"
    )

    status = fields.Selection(
        [
            ("pending", "Pending"),
            ("connected", "Connected"),
            ("busy", "Busy"),
            ("no_answer", "No Answer")
        ],
        default = "pending",
        string = "Status",
        required = True
    )

    notes = fields.Text(
        string = "Notes"
    )

    call_date = fields.Datetime(
        string = "Call Date",
        default = fields.Datetime.now
    )

    user_id = fields.Many2one(
        "res.users",
        string = "User",
        default = _default_user
    )
