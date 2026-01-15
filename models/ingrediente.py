from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Ingrediente(models.Model):
    _name = "restaurante.ingrediente"
    _description = "Ingrediente del menú"
    _rec_name = "nombre"

    nombre = fields.Char(
        string="Nombre",
        required=True
    )

    stock = fields.Float(
        string="Stock disponible (unidades)",
        required=True,
        default=0.0
    )

    unidad = fields.Selection(
        [
            ('kg', 'Kilogramos'),
            ('g', 'Gramos'),
            ('l', 'Litros'),
            ('ml', 'Mililitros'),
            ('unidad', 'Unidad')
        ],
        string="Unidad",
        required=True,
        default='unidad'
    )

    producto_ids = fields.Many2many(
        comodel_name="restaurante.producto",
        relation="producto_ingrediente_rel",
        column1="ingrediente_id",
        column2="producto_id",
        string="Productos"
    )

    @api.constrains('stock')
    def _check_stock(self):
        for ingr in self:
            if ingr.stock < 0:
                raise ValidationError("El stock no puede ser negativo.")
            
    def unlink(self):
        # antes de borrar, revisamos que no tenga productos asociados
        for ing in self:
            if ing.producto_ids:
                raise ValidationError(
                    f"No se puede borrar el ingrediente {ing.nombre} porque está usado en productos."
                )
        return super().unlink()
