# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Accountant (OCA)",
    "summary": "Add missing features for Odoo Community Edition"
    " to configure properly accounting. (Fiscal years, Overdue Message, ...)",
    "version": "16.0.1.0.1",
    "category": "Accounting",
    "author": "GRAP,Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/grap/grap-odoo-incubator",
    "license": "AGPL-3",
    "depends": ["account", "base_setup"],
    "data": [
        "security/ir.model.access.csv",
        "views/view_account_config_settings.xml",
    ],
}
