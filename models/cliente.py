from odoo import models, fields

class Cliente(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    es_cliente_restaurante = fields.Boolean(
        string="Cliente del restaurante",
        default=False
    )

    cliente_id = fields.Integer(
        string="ID del Cliente",
        default= 1
    )
    
    ## la lambda funciona como la lambda del default del id de las mesas