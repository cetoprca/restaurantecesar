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

    mesa_ids = fields.Many2many(
        comodel_name="restaurante.mesa",
        relation="camarero_mesa_rel",
        column1="camarero_id",
        column2="mesa_id",
        string="Mesas asignadas"
    )
    
    foto = fields.Image(
        string="Foto del camarero"
    )
    
    @api.constrains('numero_empleado')
    def _check_numero(self):
        for camarero in self:
            if camarero.numero_empleado <= 0:
                raise ValidationError("El número de empleado debe ser mayor que 0.")
            
            other = self.search([('numero_empleado', '=', camarero.numero_empleado), ('id', '!=', camarero.id)])
            if other:
                raise ValidationError(f"Ya existe un empleado con el número {camarero.numero_empleado}")
