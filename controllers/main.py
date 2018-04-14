# coding: utf-8
from odoo import http


class MainController(http.Controller):

    @http.route('/web/hola_mundo', type='http', auth='none')
    def hola(self):
        return '<h1>Hola Mundo</h1>'

    @http.route('/web/clientes', type='http', auth='none')
    def clientes(self):
        partners = http.request.env['res.partner'].sudo().search([])
        res = '<ul>'
        for partner in partners:
            res += '\n\t<li>%s</li>' % partner.name
        res += '\n</ul>'
        return res
        # return '<ul>\n' + '\n'.join('<li>%s</li>' % p.name for p in res) + '\n</ul>'

    @http.route('/web/clientes/form_create', type='http', auth='none')
    def crear_cliente_form(self):
        return """
        <form action="/web/clientes/crear_cliente" method="post">
            <label for="name">Nombre</label>
            <input type="text" name="name" id="name" placeholder="Nombre Cliente"/>
            <input type="submit" value="Enviar"/>
        </form>
        """

    @http.route('/web/clientes/crear_cliente', type='http', auth='none', csrf=False)
    def crear_cliente(self, name):
        partners = http.request.env['res.partner'].sudo().search([])
        partner = partners.create({'name': name})
        return '<h1>Creado el partner: %s</h1>' % partner.name

    @http.route('/web/clientes/form_delete', type='http', auth='none')
    def borrar_cliente_form(self):
        return """
        <form action="/web/clientes/borrar_cliente" method="post">
            <label for="name">Nombre</label>
            <input type="text" name="name" id="name" placeholder="Nombre Cliente a borrar"/>
            <input type="submit" value="Enviar"/>
        </form>
        """

    @http.route('/web/clientes/borrar_cliente', type='http', auth='none', csrf=False)
    def borrar_cliente(self, name):
        partners = http.request.env['res.partner'].sudo().search([('name', 'ilike', name)])
        if partners:
            partners.unlink()
            return '<h1>Borrado el partner %s</h1>' % name
        else:
            return '<h1>No existe el partner %s</h1>' % name

    @http.route('/web/clientes/json/', type='json', auth='none', methods=['POST'], cors="*", csrf=False)
    def get_partners(self):
        name = http.request.params.get('name')
        partners = http.request.env['res.partner'].sudo().search([('name', '=', name)])
        return {
            'partners': [{
                'name': partner.name,
                'id': partner.id,
                'address': partner.address_get()
            } for partner in partners]
        }
