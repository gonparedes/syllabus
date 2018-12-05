from odoo import models, fields, api, exceptions

class SyllabusFacultad(models.Model):
    _name = "syllabus.facultad"
    _rec_name = "nombre"
    nombre = fields.Char(string="Nombre")
    descripcion = descripcion = fields.Html(string="Descripcion")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [('facultad_unica', 'unique (nombre,descripcion)', 'Esta Facultad ya existe')]