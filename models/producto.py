from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Producto(models.Model):
    _name = "restaurante.producto"
    _description = "Producto del menú"
    _rec_name = "nombre"

    nombre = fields.Char(
        string="Nombre",
        required=True
    )

    precio = fields.Float(
        string="Precio (€)",
        required=True,
        default=0.0
    )

    categoria = fields.Selection(
        [
            ('entrante', 'Entrante'),
            ('principal', 'Plato Principal'),
            ('postre', 'Postre'),
            ('bebida', 'Bebida'),
        ],
        string="Categoría",
        required=True
    )

    ingrediente_ids = fields.Many2many(
        comodel_name="restaurante.ingrediente",
        relation="producto_ingrediente_rel",
        column1="producto_id",
        column2="ingrediente_id",
        string="Ingredientes"
    )

    cantidad_ingredientes = fields.Integer(
        string="Número de ingredientes",
        compute="_compute_cantidad_ingredientes",
        store=True
    )

    @api.depends('ingrediente_ids')
    def _compute_cantidad_ingredientes(self):
        for prod in self:
            prod.cantidad_ingredientes = len(prod.ingrediente_ids)

    @api.constrains('precio')
    def _check_precio(self):
        for prod in self:
            if prod.precio < 0:
                raise ValidationError("El precio no puede ser negativo.")