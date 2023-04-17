from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"
    _order = "emergency desc"

    name = fields.Char(string="Name", tracking=True)
    image = fields.Image(tracking=True, string="Profile Photo")
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    emergency = fields.Selection([('0', 'None'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High')],
                                 string="Emergency", default='0', tracking=True)
    # mail_patient_ids = fields.One2many('mail.patient.wizard', string="Mail to Patient")
    # today_date = fields.Date(string="Today's Date")
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_compute_age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    email = fields.Char(string="Email", tracking=True)

    # mail_id = fields.Many2one('mail.patient.wizard', string="Mail")
    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('under_observation', 'Under Observation'),
    #     ('done', 'Done')], string="Status", default='draft', required=True)

    # @api.onchange('date_of_birth')
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            # pass
            today = date.today()
            # print(rec.date_of_birth)
            # print(type(rec.date_of_birth))
            # print(today)
            # print(type(today))
            if rec.date_of_birth:
                if rec.date_of_birth and rec.date_of_birth > today:
                    raise ValidationError(_("Please Enter Valid Date of Birth"))
                else:
                    rec.age = today.year - rec.date_of_birth.year - (
                            (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 1

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            if rec.age and rec.age < 0:
                raise ValidationError(_("Please Enter Valid Age"))
        else:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    @api.model
    def test_cron_job(self):
        print("Schedule Action Triggered.")

    # def mail_btn(self):
    #     template = self.env.ref('my_hospital.mail_to_patient')
    #     print(template)
    #     for rec in self:
    #         template.send_mail(rec.id, force_send=True)
    #     template = self.env.ref('my_hospital.mail_to_patient')
    #     template.send_mail(self.id, force_send=True)
