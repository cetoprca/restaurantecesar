from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Camarero(models.Model):
    _name = "restaurante.camarero"
    _description = "Camarero del restaurante"
    _rec_name = "nombre"

    nombre = fields.Char(
        string="Nombre",
        required=True
    )

    numero_empleado = fields.Integer(
        string="Número de empleado",
        required=True
    )
    
    pedido_ids = fields.One2many(
        comodel_name="restaurante.pedido",
        inverse_name="camarero_id",
        string="Pedidos"
    )

    foto = fields.Image(
        string="Foto del camarero"
    )
    
    def despedir(self):
        self.unlink()
    
    @api.constrains('numero_empleado')
    def _check_numero(self):
        for camarero in self:
            if camarero.numero_empleado <= 0:
                raise ValidationError("El número de empleado debe ser mayor que 0.")
            
            other = self.search([('numero_empleado', '=', camarero.numero_empleado), ('id', '!=', camarero.id)])
            if other:
                raise ValidationError(f"Ya existe un empleado con el número {camarero.numero_empleado}")
