from odoo import models, fields, api

class musica(models.Model):
    _name = 'musica.task'
    name = fields.Char('Artista', required=True)
    name2 = fields.Char('Album', required=True)
    name3 = fields.Char('Año', required=True)
    name4 = fields.Integer('Número de Canciones', required=True)
    name5 = fields.Char('Carátula', help='Elija carátula')
