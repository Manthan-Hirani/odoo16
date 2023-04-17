from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"
    _rec_name = "doctor_id"

    # name = fields.Char(related="doctor_id.name", string="Name", tracking=True)
    # name = fields.Many2one(comodel_name="res.users", string="Name", tracking=True)
    doctor_id = fields.Many2one("res.users", string="Name", tracking=True)
    image = fields.Image(related="doctor_id.image_1920", string="Image", tracking=True)
    experience = fields.Integer(string="Experience", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    expertise = fields.Char(string="Expertise", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
