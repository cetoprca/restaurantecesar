from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Mesa(models.Model):
    _name = "restaurante.mesa"
    _description = "Mesa del restaurante"
    _rec_name = "numero"

    numero = fields.Integer(
        string="Número de mesa",
        required=True,
        default= 1 ##lambda self: self.env['restaurante.mesa'].search([], order='numero desc', limit=1).numero + 1 if self.env['restaurante.mesa'].search([], order='numero desc', limit=1) else 1
    )
    
    ## La lambda es un if que busca el numero mas alto de mesa y le suma 1 en caso de que haya mesas, en caso contrario deja 1
    ## el if funciona tal que asi: <valor_si> if <condicion> else <valor_no>, un poco confuso de parte de python si me preguntas a mi


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