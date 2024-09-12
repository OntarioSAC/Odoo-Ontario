from odoo import models, fields

class OntarioClient(models.Model):
    _name = "ontario.cliente"
    
    name = fields.char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(
        string="Gender",
        selection=[("male","Male"),("female","Female")], default='male')
    
    email = fields.Char(string='Email')
    company_id = fields.Many2one(res_model='res')