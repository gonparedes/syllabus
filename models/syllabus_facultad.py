from odoo import models, fields, api, exceptions

class SyllabusFacultad(models.Model):
    _name = "syllabus.facultad"

    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    descripcion = descripcion = fields.Html(string="Descripcion")
    #carrera = fields.Many2one('syllabus.carrera', string="Id Carrera")