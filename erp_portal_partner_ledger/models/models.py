# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions
from odoo.http import content_disposition, Controller, request, route
from odoo import http


class AccountMoveLines(models.Model):
    _inherit = "account.move.line"

    def _get_report_base_filename(self):
        return "Portal Ledger Report"
