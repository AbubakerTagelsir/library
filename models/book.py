from odoo import api, fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Our book class'

    name = fields.Char(string='Name')
    publish_date = fields.Date("Publish Date")
    author_id = fields.Many2one('library.author', "Author")
    category_id = fields.Many2one('library.category', "Category")
    user_id = fields.Many2one('library.user', "Current User")