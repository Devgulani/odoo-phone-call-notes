# -*- coding: utf-8 -*-
# from odoo import http


# class PhoneCallNotes(http.Controller):
#     @http.route('/phone_call_notes/phone_call_notes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phone_call_notes/phone_call_notes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('phone_call_notes.listing', {
#             'root': '/phone_call_notes/phone_call_notes',
#             'objects': http.request.env['phone_call_notes.phone_call_notes'].search([]),
#         })

#     @http.route('/phone_call_notes/phone_call_notes/objects/<model("phone_call_notes.phone_call_notes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phone_call_notes.object', {
#             'object': obj
#         })

