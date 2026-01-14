from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Mesa(models.Model):
    _name = "restaurante.mesa"
    _description = "Mesa del restaurante"
    _rec_name = "numero"

    numero = fields.Integer(
        string="Número de mesa",
        required=True,
        default= 1 
    )
    
    ## para que no de error en la base de datos he tenido que matener aqui un numero estatico en vez de la lambda
    ## pero para mantener el comportamiento he añadido un @api.model create() para realizar ahi la operacion

    capacidad = fields.Integer(
        string="Capacidad",
        required=True,
        default=2
    )

    estado = fields.Selection(
        [
            ('libre', 'Libre'),
            ('ocupada', 'Ocupada'),
            ('reservada', 'Reservada')
        ],
        string="Estado",
        default="libre"
    )

    pedido_ids = fields.One2many(
        comodel_name="restaurante.pedido",
        inverse_name="mesa_id",
        string="Pedidos"
    )

    @api.constrains('capacidad')
    def _check_capacidad(self):
        for mesa in self:
            if mesa.capacidad <= 0:
                raise ValidationError("La capacidad debe ser mayor que 0.")

    @api.constrains('numero')
    def _check_numero(self):
        for mesa in self:
            if mesa.numero <= 0:
                raise ValidationError("El número de la mesa debe ser mayor que 0.")
            
    @api.model
    def create(self, vals):
        if vals.get('es_cliente_restaurante', False) and vals.get('cliente_id', 0) == 0:
            last = self.env['restaurante.mesa'].search([('numero','=',True)],order='numero desc', limit=1)
            
            id = (lambda : (last.numero + 1 if last else 1))
            
            vals['numero'] = id
        return super().create(vals)