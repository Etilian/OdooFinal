from odoo import models, fields, api

class pelicula(models.Model):
    _name = 'pelicula.task'
    name = fields.Char('Director', required=True)
    name2 = fields.Char('Titulo', required=True)
    name3 = fields.Char('Género', required=True)
    name4 = fields.Integer('Año', required=True)
    name5 = fields.Char('Portada', help='Elija Portada')