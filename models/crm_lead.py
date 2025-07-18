from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    last_message_body = fields.Html(
        string="Last Message",
        compute="_compute_last_message_body",
        store=True,
    )

    @api.depends('message_ids')
    def _compute_last_message_body(self):
        for lead in self:
            last_msg = lead.message_ids.sorted(key='date', reverse=True)[:1]
            lead.last_message_body = last_msg.body if last_msg else ''