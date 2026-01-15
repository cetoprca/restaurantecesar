from odoo import http
from odoo.http import request
from odoo.http import Response 
import json

class RestauranteCamareroController(http.Controller):
    @http.route('/api/camareros', auth='public', type='json', methods=['GET'])
    def listCamareros(self, **kw):
        try:
            camareros = request.env['restaurante.camarero'].sudo().search([])
            
            jsonFinal = []
            
            for camarero in camareros:
                jsonCamarero = camarero.read(['nombre', 'numero_empleado', 'mesa_ids'])[0]

                jsonFinal.append(jsonCamarero)
            
            return jsonFinal

        except:
            return Response(
                status=400,
                content_type='application/json',
                response=json.dumps({
                    "error":"Bad Request",
                    "message":"Datos invalidos"
                })
            )
    
    @http.route('/api/camarero/add', auth='public', type='json', methods=['PUT'])
    def addCamarero(self, **kw):
            
        try:    
            data = json.loads(request.httprequest.data.decode('utf-8'))
            
            request.env['restaurante.camarero'].sudo().create(data)
        
        except:
            return Response(
                status=400,
                content_type='application/json',
                response=json.dumps({
                    "error":"Bad Request",
                    "message":"Datos invalidos"
                })
            )
        
    
    @http.route('/api/camarero/update', auth='public', type='json', methods=['PATCH'])
    def updateCamarero(self, **kw):
        
        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))

            numero_empleado = data.get('numero_empleado')
            
            camarero = request.env['restaurante.camarero'].sudo().search([('numero_empleado', '=', numero_empleado)])
            
            data.pop('numero_empleado')
            
            camarero.sudo().write(data)
        except:
            return Response(
                status=400,
                content_type='application/json',
                response=json.dumps({
                    "error":"Bad Request",
                    "message":"Datos invalidos"
                })
            )

    @http.route('/api/camarero/delete', auth='public', type='json', methods=['DELETE'])
    def deleteCamarero(self, **kw):
        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))
            
            numero_empleado = data.get('numero_empleado')
            
            camarero = request.env['restaurante.camarero'].sudo().search([('numero_empleado', '=', numero_empleado)])
            
            camarero.sudo().unlink()
        except:
            return Response(
                status=400,
                content_type='application/json',
                response=json.dumps({
                    "error":"Bad Request",
                    "message":"Datos invalidos"
                })
            )
