from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError

class SyllabusInstanciaCurso(models.Model):

    _inherits = {'syllabus.carrera': 'carrera'}
    _name = "syllabus.instancia.curso"
    _rec_name = "curso"
    curso = fields.Many2one('syllabus.curso', string="Curso")
    carrera = fields.Many2one('syllabus.carrera',string="Carrera",required=True,index=True,copy=False,ondelete='restrict')
    anio = fields.Many2one('syllabus.periodo', string="Año")
    seccion = fields.Integer(string="Seccion", default=1)
    profesor = fields.Many2one('res.users', string="Profesor",
                               domain=lambda self: [("groups_id", "=", self.env.ref("syllabus.group_profesor").id)])
    syllabus = fields.Binary(string="Archivo de Syllabus")
    estado_syllabus = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_revision', 'En Revision'),
        ('aprobado', 'Aprobado'),
    ], default="nuevo", string="Estado del Sillabus")
    observacion_syllabus = fields.Html(string="Observacion Syllabus")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [('seccion_unico', 'unique (seccion,curso,anio,semestre)', 'No se puede repetir el curso')]

    #   Aplicacion de una validacion en campo estado_syllabus
    #   para cuando quiera ser revisado deba estar previamente en nuevo
    def profesor_syllabus(self):
        if self.estado_syllabus != 'nuevo':
            raise UserError("Solo los nuevos Syllabus pueden ser enviadas a revisión...")
        else:
            self.estado_syllabus = 'en_revision'

    #   Aplicacion de una validacion en campo estado_syllabus
    #   para cuando quiera ser rechazado deba estar previamente en revision
    def rechazo_comite(self):
        if self.estado_syllabus != 'en_revision':
            raise UserError("Solo los Syllabus marcados para revisión pueden ser rechazados...")
        else:
            self.estado_syllabus = 'nuevo'

    #   Aplicacion de una validacion en campo estado_syllabus
    #   para cuando quiera ser aprobado deba estar previamente en revision
    def aprobacion_comite(self):
        if self.estado_syllabus != 'en_revision':
            raise UserError("Solo los Syllabus marcados para revisión pueden ser aprobados...")
        else:
            self.estado_syllabus = 'aprobado'

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo seccion para que no sea negativo
    @api.constrains('seccion')
    def _check_Seccion(self):
        for record in self:
            if record.seccion < 1:
                raise ValidationError("La seccion debe ser mayor que %s" % record.seccion)