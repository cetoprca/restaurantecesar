from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineaPedido(models.Model):
    _name = "restaurante.linea_pedido"
    _description = "Línea de pedido del restaurante"

    pedido_id = fields.Many2one(
        comodel_name="restaurante.pedido",
        string="Pedido",
        required=True
    )

    producto_id = fields.Many2one(
        comodel_name="restaurante.producto",
        string="Producto",
        required=True
    )

    cantidad = fields.Integer(
        string="Cantidad",
        required=True,
        default=1
    )

    subtotal = fields.Float(
        string="Subtotal (€)",
        compute="_compute_subtotal",
        store=True
    )
    
    @api.depends('producto_id', 'cantidad')
    def _compute_subtotal(self):
        for linea in self:
            linea.subtotal = linea.cantidad * (linea.producto_id.precio or 0.0)

    @api.constrains('cantidad')
    def _check_cantidad(self):
        for linea in self:
            if linea.cantidad <= 0:
                raise ValidationError("La cantidad debe ser mayor que 0.")
