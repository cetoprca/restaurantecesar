# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import Response
import json

class RestauranteMesaController(http.Controller):
    @http.route('/api/mesas', auth='public', type='json', methods=['GET'])
    def listMesas(self, **kw):
        try:
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
        
        except:
            return {
                'status':400,
                'content_type':'application/json',
                "error":"Bad Request",
                "message":"Datos invalidos"
                }
    
    @http.route('/api/mesa/add', auth='public', type='json', methods=['PUT'])
    def addMesa(self, **kw):
        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))
            
            request.env['restaurante.mesa'].sudo().create(data)
        except:
            return {
                'status':400,
                'content_type':'application/json',
                "error":"Bad Request",
                "message":"Datos invalidos"
                }
        
    
    @http.route('/api/mesa/update', auth='public', type='json', methods=['PATCH'])
    def updateMesa(self, **kw):
        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))

            mesa_id = data.get('numero')
            
            mesa = request.env['restaurante.mesa'].sudo().search([('numero', '=', mesa_id)])
            
            data.pop('numero')
            
            mesa.sudo().write(data)
        except:
            return {
                'status':400,
                'content_type':'application/json',
                "error":"Bad Request",
                "message":"Datos invalidos"
                }

    @http.route('/api/mesa/delete', auth='public', type='json', methods=['DELETE'])
    def deleteMesa(self, **kw):
        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))
            mesa_id = data.get('numero')
            
            mesa = request.env['restaurante.mesa'].sudo().search([('numero', '=', mesa_id)])
            
            mesa.sudo().unlink()
        except:
            return {
                'status':400,
                'content_type':'application/json',
                "error":"Bad Request",
                "message":"Datos invalidos"
                }
