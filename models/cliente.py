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
    
    ## para que no de error en la base de datos he tenido que matener aqui un numero estatico en vez de la lambda
    ## pero para mantener el comportamiento he añadido un @api.model create() para realizar ahi la operacion
    
    @api.model
    def create(self, vals):
        if vals.get('es_cliente_restaurante', False) and vals.get('cliente_id', 0) == 0:
            last = self.env['res.partner'].search([('es_cliente_restaurante','=',True)],order='cliente_id desc', limit=1)
            id = (lambda : (last.cliente_id + 1 if last else 1))
            
            vals['cliente_id'] = id
        return super().create(vals)