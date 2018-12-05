from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError

class SyllabusCurso(models.Model):
    _name = "syllabus.curso"
    codigo = fields.Char(string="Codigo")
    curso = fields.Char(string="Nombre")
    creditos = fields.Integer(string="Creditos")
    horas_pre = fields.Integer(string="Horas Presenciales")
    horas_auto = fields.Integer(string="Horas Autonomas")
    malla = fields.Char(string="Malla")
    carrera_curso = fields.Many2one('syllabus.carrera', string="Carrera")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [('curso_unico','unique(codigo,curso,malla,carrera_curso)','No se puede repetir el curso')]

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo creditos para que no sea negativo
    @api.constrains('creditos')
    def _check_creditos(self):
        for record in self:
            if record.creditos <= 0:
                raise ValidationError("EL curso debe tener un creditaje superior al %s" % record.creditos)

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo horas_pre para que no sea negativo
    @api.constrains('horas_pre')
    def _check_horas_pre(self):
        for record in self:
            if record.horas_pre <= 0:
                raise ValidationError("El curso debe tener horas presenciales superior a %s" % record.horas_pre)

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo horas_auto para que no sea negativo
    @api.constrains('horas_auto')
    def _check_horas_auto(self):
        for record in self:
            if record.horas_auto <= 0:
                raise ValidationError("El curso debe tener horas autonomas superior a %s" % record.horas_auto)

    #   Aplicacion un alter _rec_name para poder designar un nuevo tag hacia la id de la tabla,
    #   en este caso a la id se le reconoce visualmente por la concatenacion del curso y su codigo
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.curso+"-"+record.codigo))
        return result