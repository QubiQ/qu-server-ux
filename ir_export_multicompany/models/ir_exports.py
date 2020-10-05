# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class IrExport(models.Model):
    _inherit = 'ir.exports'

    company_id = fields.Many2one(comodel_name='res.company')

    @api.model
    def create(self, values):
        values['company_id'] = self.env.user.company_id.id
        return super(IrExport, self).create(values)
