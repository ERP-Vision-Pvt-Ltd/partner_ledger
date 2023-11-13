# -*- coding: utf-8 -*-

import re
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http
# from odoo.addons.portal.controllers.portal import CustomerPortal
from datetime import datetime
from odoo.http import content_disposition, Controller, request, route


class PortalAccount(CustomerPortal):
    current_year = datetime.now().year
    date_from = datetime(current_year, 1, 1)
    date_to = datetime(current_year, 12, 31)

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        if 'ledger_invo' in counters:
            partner = request.env.user.partner_id
            domain = [
                ('parent_state', '=', 'posted'),
                ('account_id.reconcile', '=', True),
                ('partner_id', '=', partner.id)
            ]
            ledger = request.env['account.move.line'].sudo().search_count(domain)
            values['ledger_invo'] = ledger
        return values

    @http.route(['/my/ledger', '/my/quotes/page/<int:page>'], type='http', auth="user", website=True)
    def my_ledger_route(self, **kwargs):
        partner = request.env.user.partner_id
        domain = [

            ('parent_state', '=', 'posted'),
            ('account_id.reconcile', '=', True),
            ('partner_id', '=', partner.id),
        ]
        ledger = request.env['account.move.line'].sudo().search(domain)
        ledger = sorted(ledger, key=lambda rec: rec.partner_id.name if rec.partner_id else '')

        values = {
            'partner': partner.sudo(),
            'force_refresh': True,
            'ledger': ledger,
        }

        return request.render("erp_portal_partner_ledger.portal_my_ledger", values)

    @http.route(["/my/ledger/download"], type='http', auth="user", website=True)
    def _get_name_invoice_report(self, access_token=None, report_type='pdf', download=True, **kw):
        partner = request.env.user.partner_id
        domain = [
            ('parent_state', '=', 'posted'),
            ('account_id.reconcile', '=', True),
            ('partner_id', '=', partner.id),
        ]
        ledger = request.env['account.move.line'].sudo().search(domain)
        values = {
            'partner': partner.sudo(),
            'force_refresh': True,
            'ledger': ledger,
        }

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=ledger, report_type=report_type,
                                     report_ref='erp_portal_partner_ledger.action_report_portal_ledger',
                                     download=download, **kw)

    @http.route(["/my/ledger/print"], type='http', auth="user", website=True)
    def _get_name_print_report(self, access_token=None, report_type='pdf', download=False, **kw):
        partner = request.env.user.partner_id
        domain = [
            ('parent_state', '=', 'posted'),
            ('account_id.reconcile', '=', True),
            ('partner_id', '=', partner.id),
        ]
        ledger = request.env['account.move.line'].sudo().search(domain)
        values = {
            'partner': partner.sudo(),
            'force_refresh': True,
            'ledger': ledger,
        }
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=ledger, report_type=report_type,
                                     report_ref='erp_portal_partner_ledger.action_report_print', download=download,
                                     **kw)
