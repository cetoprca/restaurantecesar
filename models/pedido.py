from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pedido(models.Model):
    _name = "restaurante.pedido"
    _description = "Pedido del restaurante"
    _rec_name = "nombre_cliente"

    nombre_cliente = fields.Char(
        string="Nombre del cliente",
        required=True
    )

    mesa_id = fields.Many2one(
        comodel_name="restaurante.mesa",
        string="Mesa",
        required=True
    )

    linea_ids = fields.One2many(
        comodel_name="restaurante.linea_pedido",
        inverse_name="pedido_id",
        string="Líneas del pedido"
    )

    total = fields.Float(
        string="Total (€)",
        compute="_compute_total",
        store=True
    )

    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('preparacion', 'En preparación'),
            ('servido', 'Servido'),
            ('pagado', 'Pagado')
        ],
        string="Estado",
        default='borrador'
    )

    fecha_pedido = fields.Datetime(
        string="Fecha del pedido",
        default=fields.Datetime.now
    )

    camarero_id = fields.Many2one(
        comodel_name="restaurante.camarero",
        string="Camarero"
    )

    @api.depends('linea_ids.subtotal')
    def _compute_total(self):
        for pedido in self:
            pedido.total = sum(linea.subtotal for linea in pedido.linea_ids)

    @api.constrains('mesa_id')
    def _check_mesa_unica(self):
        for pedido in self:
            if pedido.mesa_id and pedido.mesa_id.estado == 'ocupada' and pedido.estado == 'borrador':
                raise ValidationError(f"La mesa {pedido.mesa_id.numero} ya está ocupada.")
