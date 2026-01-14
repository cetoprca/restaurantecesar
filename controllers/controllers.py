# -*- coding: utf-8 -*-
# from odoo import http


# class Restaurantecesar(http.Controller):
#     @http.route('/restaurantecesar/restaurantecesar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restaurantecesar/restaurantecesar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restaurantecesar.listing', {
#             'root': '/restaurantecesar/restaurantecesar',
#             'objects': http.request.env['restaurantecesar.restaurantecesar'].search([]),
#         })

#     @http.route('/restaurantecesar/restaurantecesar/objects/<model("restaurantecesar.restaurantecesar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restaurantecesar.object', {
#             'object': obj
#         })

