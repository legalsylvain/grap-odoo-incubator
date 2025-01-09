# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields

from odoo.addons.base.models.res_config import ResConfigSettings


class AccountingConfigSettings(ResConfigSettings):
    # class AccountingConfigSettings(models.TransientModel):
    #     _inherit = "res.config.settings"

    _name = "account.config.settings"
    _description = "Accounting Settings"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )

    fiscalyear_last_day = fields.Integer(
        related="company_id.fiscalyear_last_day",
        readonly=False,
        required=True,
        compute_sudo=True,
    )
    fiscalyear_last_month = fields.Selection(
        related="company_id.fiscalyear_last_month",
        readonly=False,
        required=True,
        compute_sudo=True,
    )
    period_lock_date = fields.Date(
        string="Lock Date for Non-Advisers",
        related="company_id.period_lock_date",
        readonly=False,
        compute_sudo=True,
        help="Only users with the 'Adviser' role can"
        " edit accounts prior to and inclusive of this date."
        " Use it for period locking inside an open fiscal year,"
        " for example.",
    )
    fiscalyear_lock_date = fields.Date(
        string="Lock Date",
        related="company_id.fiscalyear_lock_date",
        readonly=False,
        compute_sudo=True,
        help="No users, including Advisers, can edit accounts prior to"
        " and inclusive of this date. Use it for fiscal year"
        " locking for example.",
    )
    incoterm_id = fields.Many2one(
        comodel_name="account.incoterms",
        related="company_id.incoterm_id",
        readonly=False,
        compute_sudo=True,
        string="Default incoterm",
        help="International Commercial Terms are a series"
        " of predefined commercial terms used in international transactions.",
    )

    def execute(self):
        return super(AccountingConfigSettings, self.sudo()).execute()
