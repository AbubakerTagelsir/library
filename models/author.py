from odoo import api, fields, models


class Author(models.Model):
    _name = 'library.author'
    _description = 'Author Class'

    name = fields.Char(string='Name')
    bio = fields.Text(string='Biography')
    books = fields.One2many('library.book', 'author_id', "Books")