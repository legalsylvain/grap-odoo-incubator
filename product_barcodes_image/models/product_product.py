# Copyright (C) 2016 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author: Quentin Dupont (https://twitter.com/pondupont)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
import base64
# import StringIO
import logging

from odoo import _, api, exceptions, fields, models

logger = logging.getLogger(__name__)

try:
    import cairosvg
except ImportError:
    cairosvg = False
    logger.debug("product_barcodes_image - 'cairosvg' librairy not found")

try:
    import barcode
except ImportError:
    barcode = False
    logger.debug("product_barcodes_image - 'barcode' librairy not found")


class ProductProduct(models.Model):
    _inherit = "product.product"

    barcode_image = fields.Binary(
        string="Barcode Image", compute="_compute_barcode_image",
        store=True, attachment=True)

    @api.multi
    @api.depends("barcode")
    def _compute_barcode_image(self):
        if not (barcode and cairosvg):
            return
        for product in self.filtered(lambda x: x.barcode):

            if len(product["barcode"]) == 8:
                EAN = barcode.get_barcode_class("ean8")
            elif len(product["barcode"]) == 13:
                EAN = barcode.get_barcode_class("ean13")
            else:
                raise exceptions.Warning(
                    _("Barcode image will not be computed")
                )
            ean = EAN(product.barcode)
            fullname = ean.save("/tmp/" + product.barcode)
            f = open(fullname, "r")
            # output = StringIO.StringIO()
            # svg = f.read()
            # cairosvg.svg2png(
            #     bytestring=svg, write_to=output, center_text=True, dpi=300
            # )
            # product.barcode_image = base64.b64encode(output.getvalue())
            # os.remove(fullname)
