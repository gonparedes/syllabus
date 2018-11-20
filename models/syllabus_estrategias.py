from odoo import models, fields, api

class SyllabusEstrategia(models.Model):
    _name = "syllabus.estrategia"
    _rec_name ="nombre"

    nombre = fields.Char(string="Estrategias de Aprendizaje")
    codigo = fields.Integer(string="Codigo de Estrategias")


    _sql_constraints = [
        ('codigo_estrategia', 'unique (codigo)', 'Esta Estrategia ya existe')]