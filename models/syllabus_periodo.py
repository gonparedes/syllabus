from odoo import models, fields, api

class SyllabusPeriodo(models.Model):
    _name = "syllabus.periodo"
    _rec_name ="anio"

    anio = fields.Integer(string="Año de Periodo")
    semestre = fields.Integer(string="Semetre")
    inicio = fields.Date(string="Fecha Inicio")
    termino = fields.Date(string="Fecha Termino")
    estado = fields.Selection([
        ('actual', 'Actual'),
        ('historico', 'Historico'),
    ], default="actual", string="Estado del Sillabus")


    _sql_constraints = [
        ('periodo', 'unique (anio,semestre)', 'Esta Período Académico ya existe')]
