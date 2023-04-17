from odoo import api, fields, models
# from odoo.exceptions import ValidationError


class ProjectMilestone(models.Model):
    _name = "project.milestone.temp"
    _description = "Project Milestone"
    # _inherit = ['project.task']

    name = fields.Char(string="Milestone")
