# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class PosSession(models.Model):
    _inherit = "pos.session"

    @api.multi
    def action_pos_session_validate_draft(self):
        super(
            PosSession, self.with_context(pos_draft_move=True)
        ).action_pos_session_validate()
