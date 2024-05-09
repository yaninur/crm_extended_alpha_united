# -*- coding: utf-8 -*-

import logging

from odoo.exceptions import UserError, ValidationError

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.onchange("stage_id")
    def set_apply_manual(self):
        # Search for CRM teams with notify_on_stage_change set to True
        crm_teams = self.env['crm.team'].search([('notify_on_stage_change', '=', True)])
        # Get the activity type for the meeting
        meeting_activity_type = self.env.ref('mail.mail_activity_data_email')

        # Iterate over the CRM teams
        for team in crm_teams:
            # Iterate over the members of each team
            for member in team.member_ids:
                # Create activity for each member
                self.env['mail.activity'].sudo().create({
                    'activity_type_id': meeting_activity_type.id,
                    'res_model_id': self.env['ir.model'].sudo().search([('model', '=', 'crm.lead')], limit=1).id,
                    'res_id': self._origin.id,
                    'user_id': member.id,
                    'summary':  _(f" Stage updated: New stage is {self.name} new stage is {self.stage_id.name}"),
                    'note': _(f" Stage updated: New stage is    {self.name} new stage is {self.stage_id.name}"),
                })
                print("-----------------------------------", member.id)
