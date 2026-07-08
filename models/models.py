# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class phone_call_notes(models.Model):
#     _name = 'phone_call_notes.phone_call_notes'
#     _description = 'phone_call_notes.phone_call_notes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

