from odoo import models, fields

class Cliente(models.Model):
    _inherit = "res.partner"

    es_cliente_restaurante = fields.Boolean(
        string="Cliente del restaurante",
        default=False
    )

    cliente_id = fields.Integer(
        string="ID del Cliente",
        default= lambda self: (
            self.env['res.partner'].search([('es_cliente_restaurante','=',True)], order='codigo_cliente desc', limit=1).codigo_cliente + 1
            if self.env['res.partner'].search([('es_cliente_restaurante','=',True)], order='codigo_cliente desc', limit=1)
            else 1
        )
    )
    
    ## la lambda funciona como la lambda del default del id de las mesas