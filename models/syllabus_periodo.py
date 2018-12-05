from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SyllabusPeriodo(models.Model):
    _name = "syllabus.periodo"
    anio = fields.Integer(string="Año de Periodo")
    semestre = semestre = fields.Selection([
        ('1', '1'),
        ('2', '2'),
    ], default="1", string="Semestre")
    inicio = fields.Date(string="Fecha Inicio")
    termino = fields.Date(string="Fecha Termino")
    estado = fields.Selection([
        ('actual', 'Actual'),
        ('historico', 'Historico'),
    ], default="actual", string="Estado del Sillabus")

    #   Aplicacion de un constraint en la base de datos de tipo unique
    #   para cuando se quiera hacer un insert no haiga duplicidad de datos
    _sql_constraints = [
        ('periodo', 'unique (anio,semestre)', 'Esta Período Académico ya existe')]

    #   Aplicacion de un constraint en la base de datos para que se haga una validacion
    #   de tipo check hacia el campo anio para que no sea menor al anio de creacion de la universidad
    @api.constrains('anio')
    def _check_anio(self):
        for record in self:
            if record.anio <= 1990:
                raise ValidationError("La año debe ser superior al %s" % record.anio)

    #   Aplicacion un alter _rec_name para poder designar un nuevo tag hacia la id de la tabla,
    #   en este caso a la id se le reconoce visualmente por la concatenacion del anio y su semestre
    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, str(record.anio) + "-" + record.semestre+"° semestre"))
        return result