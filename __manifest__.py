# -*- coding: utf-8 -*-
{
    'name': "Restaurante Cesar",

    'summary': "Modulo para el manejo de las mesas y pedidos de un restaurante, y camareros",

    'description': """
Módulo de gestión de restaurante:
- Gestión de mesas
- Gestión de productos e ingredientes
- Pedidos y líneas de pedido
- Camareros y clientes
Incluye vistas Kanban, Tree y Form, así como asignación automática de IDs.
    """,

    'author': "César Tomás Prieto Calvo",
    'website': "https://www.github.com/cetoprca",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base'],

    "data": [
        "security/ir.model.access.csv",
        "views/mesa_view.xml",
        "views/producto_view.xml",
        "views/ingrediente_view.xml",
        "views/pedido_view.xml",
        "views/linea_pedido_view.xml",
        "views/camarero_view.xml",
        "views/cliente_view.xml",
        "views/restaurante_menu.xml",
    ],
    "application":True
}

