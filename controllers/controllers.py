# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/syllabus(http.Controller):
#     @http.route('/custom-addons/syllabus/custom-addons/syllabus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/syllabus/custom-addons/syllabus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/syllabus.listing', {
#             'root': '/custom-addons/syllabus/custom-addons/syllabus',
#             'objects': http.request.env['custom-addons/syllabus.custom-addons/syllabus'].search([]),
#         })

#     @http.route('/custom-addons/syllabus/custom-addons/syllabus/objects/<model("custom-addons/syllabus.custom-addons/syllabus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/syllabus.object', {
#             'object': obj
#         })