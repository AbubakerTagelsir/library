from odoo import api, fields, models


class Category(models.Model):
    _name = 'library.category'
    _description = 'New Description'

    name = fields.Char(string='Name')
    description = fields.Text("Description")
    parent_id = fields.Many2one('library.category', "Parent")
    books = fields.One2many('library.book', 'category_id', "Books")


