from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SyllabusCarrera(models.Model):
    _name = "syllabus.carrera"
    _rec_name ="carrera"

    carrera = fields.Char(string="Nombre")
    codigo = fields.Char(string="Codigo Carrera")
    creditos = fields.Integer(string="Creditos Carrera")
    director_escuela = fields.Many2one('res.users', string="Id Director de escuela", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_director_escuela" ).id )])
    comite = fields.Many2one('res.users', string="Id Comite", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_comite" ).id )])
    asesor = fields.Many2one('res.users', string="Id Asesor", domain=lambda self: [( "groups_id", "=", self.env.ref( "syllabus.group_asesor" ).id )])
    facultad = fields.Many2one('syllabus.facultad', string="Facultad")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [
        ('codigo_facultad', 'unique (carrera,codigo,director_escuela,comite,asesor)', 'Esta Carrera ya existe')]

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo creditos para que no sea negativo
    @api.constrains('creditos')
    def _check_creditos(self):
        for record in self:
            if record.creditos <= 0:
                raise ValidationError("La carrera debe tener un creditaje superior al %s" % record.creditos)