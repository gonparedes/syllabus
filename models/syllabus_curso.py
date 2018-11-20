from odoo import models, fields, api, exceptions

class SyllabusCurso(models.Model):
    _name = "syllabus.curso"

    _rec_name = "nombre"

    codigo = fields.Char(string="Codigo")
    nombre = fields.Char(string="Nombre")
    #semestre = fields.Integer(string="Semestre")
    #anio = fields.Integer(string="Año")
    #Seccion = fields.Integer(string="Seccion")
    creditos = fields.Integer(string="Creditos")
    horas_pre = fields.Integer(string="Horas Presenciales")
    horas_auto = fields.Integer(string="Horas Autonomas")
    #profesor = fields.Many2one('res.users', string="Profesor", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_profesor" ).id )])
    #syllabus = fields.Binary()
    #estado_syllabus = fields.Selection([
    #    ('nuevo', 'Nuevo'),
    #    ('en_revision', 'En Revision'),
    #    ('aprobado', 'Aprobado'),
    #    ('rechazado', 'Rechazado'),
    #], default="nuevo", string="Estado del Sillabus")
    malla = fields.Char(string="Malla")
    #observacion_syllabus = fields.Html(string="Observacion Syllabus")
    carrera = fields.Many2one('syllabus.carrera', string="Carrera")

