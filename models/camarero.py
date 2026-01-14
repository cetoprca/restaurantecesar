from odoo import models, fields

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
