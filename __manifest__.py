# -*- coding: utf-8 -*-
{
    'name': "Syllabus",

    'summary': """
        Modulo Syllabus UCM en Odoo 11""",

    'description': """
        Proyecto de Calidad y Produccion de Software ICI-UCM 2018
    """,

    'author': "Gonzalo Paredes",
    'website': "http://www.eici.ucm.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UCM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #Grupos
        'groups/group_admin.xml',
        'groups/group_asesor.xml',
        'groups/group_comite.xml',
        'groups/group_director_escuela.xml',
        'groups/group_profesor.xml',
        #Seguridad
        'security/ir.model.access.csv',
        #Datos
        'data/syllabus.periodo.csv',
        'data/syllabus.facultad.csv',
        'data/syllabus.carrera.csv',
        'data/syllabus.curso.csv',
        'data/syllabus.instancia.curso.csv',
        'data/syllabus.estrategia.csv',
        #Vistas
        'views/home.xml',
        'views/admin_usuarios.xml',
        'views/admin_periodo.xml',
        'views/admin_facultades.xml',
        'views/admin_carreras.xml',
        'views/admin_cursos.xml',
        'views/admin_syllabus.xml',
        'views/director_periodo.xml',
        'views/director_carreras.xml',
        'views/director_cursos.xml',
        'views/director_syllabus.xml',
        'views/profesor.xml',
        'views/comite.xml',
        'views/asesor.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'instalable': True,
    'application': True,
}