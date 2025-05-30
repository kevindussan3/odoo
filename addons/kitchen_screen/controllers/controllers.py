# -*- coding: utf-8 -*-
# from odoo import http


# class KitchenScreen(http.Controller):
#     @http.route('/kitchen_screen/kitchen_screen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kitchen_screen/kitchen_screen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kitchen_screen.listing', {
#             'root': '/kitchen_screen/kitchen_screen',
#             'objects': http.request.env['kitchen_screen.kitchen_screen'].search([]),
#         })

#     @http.route('/kitchen_screen/kitchen_screen/objects/<model("kitchen_screen.kitchen_screen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kitchen_screen.object', {
#             'object': obj
#         })

