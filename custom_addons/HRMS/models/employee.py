from odoo import api, fields, models


class Employee(models.Model):
    _name = "hrms.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "HRMS Employee"

    name = fields.Char(string="Name")
    image = fields.Image(string="Image")
    employee_type = fields.Selection([('trainee', 'Trainee'), ('permanante_employee', 'Permanante Employee'), ('consultant', 'Consultant'), ('temporary_employee', 'Temporary Employee'), ('client', 'Client')], string="Employee Type")
    designation = fields.Char(string="Designation")
    employee_no = fields.Integer(string="Employee No")

    # Experience
    relative_experience = fields.Char(string="Relative Experience")
    actual_experience = fields.Char(string="Actual Experience")
    experience_from_graduation = fields.Char(string="Experience From Graduation")

    # age = fields.Integer(string="Age", tracking=True, compute="_compute_age")
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    # active = fields.Boolean(string="Active", default=True, tracking=True)
    # email = fields.Char(string="Email", tracking=True)
