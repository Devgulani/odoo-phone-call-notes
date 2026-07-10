from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    call_log_ids = fields.One2many(
        "phone.call.log",
        "partner_id",
        string = "Call Logs"
    )

    call_log_count = fields.Integer(
        string = "Call Logs",
        compute = "_compute_call_log_count"

    )

    def _compute_call_log_count(self):
        for partner in self:
            partner.call_log_count = len(partner.call_log_ids)

    def action_view_call_logs(self):
        self.ensure_one()

        return{
            "type": "ir.actions.act_window",
            "name": "Phone Call Logs",
            "res_model": "phone.call.log",
            "view_mode": "list,form",
            "domain": [("partner_id", "=", self.id)],
            "context": {
                "default_partner_id": self.id,
            },
        }
    
    def action_open_call_wizard(self):
        self.ensure_one()

        return{
            "type": "ir.actions.act_window",
            "name": "Call Contact",
            "res_model": "phone.call.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_partner_id": self.id,
                "default_phone": self.phone,
            },
        }