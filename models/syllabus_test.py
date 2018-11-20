from odoo.osv import fields, orm, osv, api, exceptions
#from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError

class SyllabusTest(orm.Model):

    def _get_selection(self,cr,uid,context):

        comite = context.get('comite',[])
        cr.execute("""
            SELECT c. comite
            FROM syllabus_carrera as ca
            JOIN (
                SELECT t.carrera
                FROM syllabus_curso as cu
                JOIN syllabus_test as t
                ON cu.id = t.name
                )
            ON ca.id = ic.carrera
        """,(comite))

        return cr.fetchall()

    _name = "syllabus.test"

    _rec_name = "nombre"

    nombre = fields.Many2one('syllabus.curso', string="Curso")
    carrera = fields.Many2one('syllabus.carrera', string="Carrera")
    semestre = fields.Integer(string="Semestre")
    anio = fields.Integer(string="Año")
    Seccion = fields.Integer(string="Seccion")
    profesor = fields.Many2one('res.users', string="Profesor", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_profesor" ).id )])
    syllabus = fields.Binary(string="Archivo de Syllabus")
    estado_syllabus = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_revision', 'En Revision'),
        ('aprobado', 'Aprobado'),
    ], default="nuevo", string="Estado del Sillabus")
    observacion_syllabus = fields.Html(string="Observacion Syllabus")

    _sql_constraints = [
        ('instancia_curso', 'unique (nombre,semestre,seccion,anio)', 'Este elemento ya existe, cree uno nuevo.')]

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