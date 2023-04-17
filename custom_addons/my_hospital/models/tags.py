from odoo import api, fields, models


class HospitalTags(models.Model):
    _name = "hospital.tags"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Tags"
    _rec_name = "tag_name"

    tag_name = fields.Selection([
        ('kid', 'Kid'),
        ('adult', 'Adult'),
        ('senior_citizen', 'Senior Citizen')], string="Tag Name")
    color1 = fields.Integer(string="Color 1")
    # color2 = fields.Char(string="Color 2")

    _sql_constraints = [('unique_tag_name', 'unique(tag_name)', 'Tag name Must be unique')]
