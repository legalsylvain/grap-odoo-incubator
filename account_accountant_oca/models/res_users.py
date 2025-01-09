# Copyright (C) 2025 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class ResUsers(models.Model):
    _inherit = "res.users"

    def _is_admin(self):
        self.ensure_one()
        result = self._is_superuser() or self.has_group("base.group_erp_manager")
        if not result and self.env.context.get("check_accountant_group", False):
            # TODO FIXME
            print("CHECKED!!!")
            return self.has_group("base.group_user")
