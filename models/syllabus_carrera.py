from odoo import models, fields, api

class SyllabusCarrera(models.Model):
    _name = "syllabus.carrera"
    _rec_name ="nombre"

    nombre = fields.Char(string="Nombre")
    codigo = fields.Char(string="Codigo Carrera")
    creditos = fields.Integer(string="Creditos Carrera")
    director_escuela = fields.Many2one('res.users', string="Id Director de escuela", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_director_escuela" ).id )])
    comite = fields.Many2one('res.users', string="Id Comite", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_comite" ).id )])
    asesor = fields.Many2one('res.users', string="Id Asesor", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_asesor" ).id )])
    facultad = fields.Many2one('syllabus.facultad', string="Facultad")

    _sql_constraints = [
        ('codigo_facultad', 'unique (codigo,facultad)', 'Esta Carrera ya existe')]