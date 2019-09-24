# coding: utf-8
# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


# class AccountJournal(models.Model):
#     _inherit = 'account.journal'

#     # Columns section
#     pos_image = fields.Binary(string='PoS Image')

class AccountAnalyticLine(models.Model)
    _inherit = 'account.analytic.line'

    mon_vieux_champ = fields.Float()
