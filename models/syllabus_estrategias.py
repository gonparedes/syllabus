from odoo import models, fields, api

class SyllabusEstrategia(models.Model):
    _name = "syllabus.estrategia"
    _rec_name ="nombre"
    nombre = fields.Char(string="Estrategias de Aprendizaje")
    codigo = fields.Integer(string="Codigo de Estrategias")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [
        ('codigo_estrategia', 'unique (nombre,codigo)', 'Esta Estrategia ya existe')]