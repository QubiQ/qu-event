# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https: //www.gnu.org/licenses/agpl).
from odoo import models, fields


class EventEvent(models.Model):
    _inherit = 'event.event'

    survey_count = fields.Integer(
        compute='_compute_survey_count', string='Survey Count')
    survey_ids = fields.One2many('survey.survey', 'event_id', 'Surveys')

    def _compute_survey_count(self):
            # retrieve all children partners and prefetch 'parent_id' on them
        for rec in self:
            survey_count = self.env['survey.survey'].search_count(
                [('event_id', '=', rec.id)])
            rec.survey_count = survey_count
