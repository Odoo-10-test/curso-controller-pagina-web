# coding: utf-8
from odoo import http
from odoo.http import request
import simplejson


class JsonController(http.Controller):

    @http.route('/get_user_info', auth='public')
    def get_user_info(self):
        user = request.env.user

        return simplejson.dumps({
            'user': user.name,
            'login': user.login,
            'company': user.company_id.name,
            'company_phone': user.company_id.phone,
            'company_street': user.company_id.street
        })
