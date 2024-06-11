{
    'name': 'To-Do App',
    'version': '17.0.0.1.0',
    'summary': 'มาเรียนกัน',
    'description': "Hello",
    'website': 'http://www.google.com',
    'author' : 'Madara Uchiha',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml'
    ],
    'application': True,
}