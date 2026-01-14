from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Cliente(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    es_cliente_restaurante = fields.Boolean(
        string="Cliente del restaurante",
        default=True,
    )

    cliente_id = fields.Integer(
        string="ID del Cliente",
        default= 1 
    )
    
    pedido_ids = fields.One2many(
        comodel_name="restaurante.pedido",
        inverse_name="cliente_id",
        string="Pedidos del cliente"
    )
    
    ## para que no de error en la base de datos he tenido que matener aqui un numero estatico en vez de la lambda
    ## pero para mantener el comportamiento he añadido un @api.model create() para realizar ahi la operacion
    
    @api.model
    def create(self, vals):
        if not vals.get('es_cliente_restaurante'):
            raise ValidationError("Debes activar 'Cliente del restaurante' para crear nuevos registros")
            
        last = self.env['res.partner'].search([('es_cliente_restaurante','=',True)],order='cliente_id desc', limit=1)
        id = (lambda : (last.cliente_id + 1 if last else 1))
            
        if vals['cliente_id'] < id():
            vals['cliente_id'] = id()
        return super().create(vals)