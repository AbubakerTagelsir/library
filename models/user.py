from odoo import api, fields, models


class User(models.Model):
    _name = 'library.user'
    _description = 'New Description'

    name = fields.Char(string='Name')
    address = fields.Text("Address")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    books = fields.One2many('library.book', 'user_id', "Books")