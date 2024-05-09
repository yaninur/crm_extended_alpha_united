# -*- coding: utf-8 -*-

import logging

from odoo.exceptions import UserError, ValidationError

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    notify_on_stage_change = fields.Boolean(
        string='Notify on stage change',
        required=False)
