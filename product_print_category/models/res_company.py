# coding: utf-8
# Copyright (C) 2018-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    print_category_id = fields.Many2one(
        string='Default Print Category', comodel_name='product.print.category')
