#from datetime import datetime
from odoo import models, fields, api, exceptions
#from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
#from odoo.exceptions import Warning

class SyllabusEvaluacion(models.Model):
    _name = "syllabus.evaluacion"

    _rec_name = "evaluacion"

    evaluacion = fields.Selection([
         ('prueba', 'Prueba'),
         ('taller', 'Taller'),
         ('examen', 'Exámen'),
         ('proyecto', 'Proyecto'),
    ], default="nuevo", string="Estado")
    fecha = fields.Date(string="Fecha")
    porcentaje = fields.Integer(string="Ponderacion")
    notas = fields.Binary()
    pauta = fields.Binary()
    observacion = fields.Html(string="Observacion")
    curso = fields.Many2one('syllabus.instancia.curso', string="Curso")

    #@api.onchange('fecha')
    #def onchange_date(self):
    #    if datetime.strptime(self.current_date, DEFAULT_SERVER_DATE_FORMAT).date() < datetime.now().date():
            #raise warning('Please select a date equal/or greater than the current date')
    #        return False
    #    return my_date