# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class RestaurantePedidoController(http.Controller):
    @http.route('/api/pedidos', auth='public', type='json', methods=['GET'])
    def listPedidos(self, **kw):
        pedidos = request.env['restaurante.pedido'].sudo().search([])
        
        jsonFinal = []
        
        for pedido in pedidos:
            jsonPedido = pedido.read(['nombre_cliente', 'cliente_id', 'mesa_id', 'linea_ids', 'total', 'estado', 'fecha_pedido', 'camarero_id'])[0]
            
            jsonCliente = pedido.cliente_id.read(['cliente_id', 'name', 'pedido_ids'])[0]
            jsonPedido['cliente_id'] = jsonCliente
            
            jsonMesa = pedido.mesa_id.read(['numero', 'capacidad', 'estado'])[0]
            jsonPedido['mesa_id'] = jsonMesa
            
            jsonLineas = []
            if pedido.linea_ids:
                for linea in pedido.linea_ids:
                    jsonLinea = linea.read(['producto_id', 'cantidad', 'subtotal'])[0]
                    
                    jsonProducto = linea.producto_id.read(['nombre', 'precio', 'categoria', 'ingrediente_ids'])[0]
                    jsonIngredientes = []
                    for ingrediente in linea.producto_id.ingrediente_ids:
                        jsonIngrediente = ingrediente.read(['nombre'])[0]
                        jsonIngredientes.append(jsonIngrediente)
                    jsonProducto['ingrediente_ids'] = jsonIngredientes
                    
                    jsonLinea['producto_id'] = jsonProducto
                    
                    jsonLineas.append(jsonLinea)
            jsonPedido['linea_ids'] = jsonLineas
            
            jsonFinal.append(jsonPedido)
    
                
        return jsonFinal 
    
    @http.route('/api/pedido/add', auth='public', type='json', methods=['PUT'])
    def addPedido(self, **kw):
        
        data = json.loads(request.httprequest.data.decode('utf-8'))
        
        request.env['restaurante.pedido'].sudo().create(data)
        
    
    @http.route('/api/pedido/update', auth='public', type='json', methods=['PATCH'])
    def updatePedido(self, **kw):
        
        data = json.loads(request.httprequest.data.decode('utf-8'))

        pedido_id = data.get('id')
        
        pedido = request.env['restaurante.pedido'].sudo().search([('id', '=', pedido_id)])
        
        data.pop('id')
        
        pedido.sudo().write(data)

    @http.route('/api/pedido/delete', auth='public', type='json', methods=['DELETE'])
    def deletePedido(self, **kw):
        data = json.loads(request.httprequest.data.decode('utf-8'))
        pedido_id = data.get('id')
        
        mesa = request.env['restaurante.pedido'].sudo().search([('id', '=', pedido_id)])
        
        mesa.sudo().unlink()
        
