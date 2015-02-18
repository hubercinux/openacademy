# -*- coding: utf-8 -*-
from openerp import fields, models

class partner(models.Model):
	_inherit = 'res.partner'

	#nuevas columnas
	instructor = fields.Boolean("Instructor", default=False)

	session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
