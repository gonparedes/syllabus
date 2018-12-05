from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError

class SyllabusEvaluacion(models.Model):
    _inherits = {'syllabus.instancia.curso': 'curso'}
    _name = "syllabus.evaluacion"
    _rec_name = "nombre"
    curso = fields.Many2one('syllabus.instancia.curso', string="Curso")
    nombre = fields.Char(string="Nombre")
    evaluacion = fields.Selection([
         ('prueba', 'Prueba'),
         ('taller', 'Taller'),
         ('examen', 'Exámen'),
         ('proyecto', 'Proyecto'),
    ], default="prueba", string="Estado")
    fecha = fields.Date(string="Fecha")
    porcentaje = fields.Integer(string="Ponderacion")
    notas = fields.Binary()
    pauta = fields.Binary()
    observacion = fields.Html(string="Observacion")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [('evaluacion_unico', 'unique (nombre,evaluacion)', 'No se puede repetir la evaluacion')]

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo porcentaje para que no sea negativo
    @api.constrains('porcentaje')
    def _check_porcentaje(self):
        for record in self:
            if record.porcentaje <= 0:
                raise ValidationError("El porcentaje tiene que ser mayor que %s" % record.porcentaje)