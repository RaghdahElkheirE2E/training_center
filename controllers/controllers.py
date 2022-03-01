# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmad(http.Controller):
#     @http.route('/amal_center/amal_center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/amal_center/amal_center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('amal_center.listing', {
#             'root': '/amal_center/amal_center',
#             'objects': http.request.env['amal_center.amal_center'].search([]),
#         })

#     @http.route('/amal_center/amal_center/objects/<model("amal_center.amal_center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('amal_center.object', {
#             'object': obj
#         })
