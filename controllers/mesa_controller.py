# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class RestauranteMesaController(http.Controller):
    @http.route('/api/mesas', auth='public', type='json', methods=['GET'])
    def listMesas(self, **kw):
        mesas = request.env['restaurante.mesa'].sudo().search([])
        
        jsonFinal = []
        
        for mesa in mesas:
            jsonMesa = mesa.read(['numero', 'capacidad', 'estado'])[0]

            if mesa.pedido_ids:
                
                jsonPedido = mesa.pedido_ids.read(['nombre_cliente', 'estado', 'total'])
                jsonMesa['pedido_ids'] = jsonPedido
                
            else:
                jsonMesa['pedido_ids'] = []

            jsonFinal.append(jsonMesa)
        
        return jsonFinal 
    
    @http.route('/api/mesa/add', auth='public', type='json', methods=['PUT'])
    def addMesa(self, **kw):
        
        data = json.loads(request.httprequest.data.decode('utf-8'))
        
        request.env['restaurante.mesa'].sudo().create(data)
        
    
    @http.route('/api/mesa/update', auth='public', type='json', methods=['PATCH'])
    def updateMesa(self, **kw):
        
        data = json.loads(request.httprequest.data.decode('utf-8'))

        mesa_id = data.get('numero')
        
        mesa = request.env['restaurante.mesa'].sudo().search([('numero', '=', mesa_id)])
        
        data.pop('numero')
        
        mesa.sudo().write(data)

    @http.route('/api/mesa/delete', auth='public', type='json', methods=['DELETE'])
    def deleteMesa(self, **kw):
        data = json.loads(request.httprequest.data.decode('utf-8'))
        mesa_id = data.get('numero')
        
        mesa = request.env['restaurante.mesa'].sudo().search([('numero', '=', mesa_id)])
        
        mesa.sudo().unlink()
        
