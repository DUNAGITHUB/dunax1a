# -*- coding: utf-8 -*-
{
    'name': 'Reporte Presupuestos y Nota de Venta Dunati',
    'version': '1.0',
    'author': 'Open Solutions',
    'description': """
Nuevo formato de reporte de Presupuestos y Nota de Venta
======================================================
 """,
    'website': 'https://www.opens.cl',
    'depends': ['sale', 'delivery', 'mrp'],
    'data': [
        'report/sale_order_templates.xml',
        'report/pedido_venta.xml',
        'views/layouts.xml',
        ],
    'active': True,
    'installable': True,
    'application': False,
    'auto_install': False,
}