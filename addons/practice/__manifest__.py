{
    'name': 'Practice',
    'version': '1.0.0',
    'summary': 'มาเรียนกัน',
    'sequence': 5,
    'description': "Hello",
    'website': 'http://www.google.com',
    'category': 'Test',
    'author' : 'Madara',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/base_menu.xml','views/property_view.xml','security/ir.model.access.csv','views/owner_view.xml','views/tag_view.xml','views/sale_order_view.xml'
    ],
    'assets': {
        'web.assets_backend': ['practice/static/src/css/property.css']
    },
    'application': True,
}