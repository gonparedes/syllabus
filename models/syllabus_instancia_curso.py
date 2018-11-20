from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError

class SyllabusInstanciaCurso(models.Model):
    _name = "syllabus.instancia.curso"
    #_inherits = {'syllabus.carrera': 'id'}
    #pertenencia = fields.Many2one('syllabus.carrera', string="Carrera - Instancia Curso")
    _rec_name = "nombre"
    #pertenencia = fields.Reference([('syllabus.carrera','comite')], 'Refers to')
    nombre = fields.Many2one('syllabus.curso', string="Curso")
    #carrera = fields.Reference([('syllabus.curso', 'carrera')], 'Refers to')
    carrera = fields.Many2one('syllabus.carrera', string="Carrera")
    #semestre = fields.Integer(string="Semestre")
    #anio = fields.Integer(string="Año")
    anio = fields.Many2one('syllabus.periodo',string="Año")
    semestre = fields.Integer(string="Semestre")
    Seccion = fields.Integer(string="Seccion")
    profesor = fields.Many2one('res.users', string="Profesor", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_profesor" ).id )])
    syllabus = fields.Binary(string="Archivo de Syllabus")
    estado_syllabus = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_revision', 'En Revision'),
        ('aprobado', 'Aprobado'),
    ], default="nuevo", string="Estado del Sillabus")
    observacion_syllabus = fields.Html(string="Observacion Syllabus")

    #_sql_constraints = [
    #    ('instancia_curso', 'unique (semestre,seccion)', 'Este elemento ya existe, cree uno nuevo.')]

    @api.one

    def profesor_syllabus(self):
        if self.estado_syllabus != 'nuevo':
            raise UserError("Solo los nuevos Syllabus pueden ser enviadas a revisión...")
        else:
            self.estado_syllabus = 'en_revision'

    def rechazo_comite(self):
        if self.estado_syllabus != 'en_revision':
            raise UserError("Solo los Syllabus marcados para revisión pueden ser rechazados...")
        else:
            self.estado_syllabus = 'nuevo'

    def aprobacion_comite(self):
        if self.estado_syllabus != 'en_revision':
            raise UserError("Solo los Syllabus marcados para revisión pueden ser aprobados...")
        else:
            self.estado_syllabus = 'aprobado'