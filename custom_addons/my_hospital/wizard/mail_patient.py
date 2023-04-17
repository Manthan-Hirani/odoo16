from odoo import api, fields, models
# from odoo.exceptions import UserError


class MailPatientWizard(models.Model):
    _name = "mail.patient.wizard"
    _inherit = ['hospital.patient', 'mail.thread', 'mail.activity.mixin']
    _description = "Mail Patient Wizard"

    # appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True)
    # select_fields = fields.Many2many("hospital.patient.fields", string="Select Fields")
    # select_fields = fields.Many2one("hospital.patient", string="Select Fields")
    # select_1 = fields.Many2many(related="selected_fields.name", tracking=True)
    # select_ids = fields.One2many('hospital.patient', 'mail_id', string="Select Fields")
    # select_ids = fields.Many2one('hospital.patient', string="Select Fields")
    # patient_id = fields.Many2one('hospital.patient', string="Patient")
    # age = fields.Integer(related="patient_id.age", string="Age")
    # email = fields.Char(related="patient_id.email", string="Email")
    # gender = fields.Selection(related="patient_id.gender", string="Gender")
    # date_of_birth = fields.Date(related="patient_id.date_of_birth", string="Date of Birth")
    # reason_send = fields.Text(string="Reason", tracking=True)
    select_fields = fields.Many2many("ir.model.fields", string="Select Fields", domain=[('model', '=', 'hospital.patient')])

    def send_btn(self):
        ctx_list = []
        context = {
            'select_fields': self.select_fields,
            'ctx_list': ctx_list
        }
        template = self.env.ref('my_hospital.mail_to_patient')
        # template.send_mail(self.env.context['active_id'], force_send=True)
        # print("Outside")
        print(context.keys())
        # print(context)
        for rec in self.select_fields:
            ctx_list.append(rec.name)
        print(ctx_list)
        mail = template.with_context(context).send_mail(self.env.context['active_id'], force_send=True)
        print(mail)

    # @api.model
    # def send_btn(self, email_to, subject, body):
    #     print(self.select_ids)
    #     print(self.reason_send)
    #     template = self.env.ref('my_hospital.hospital_patient')
    #     render_body = template.render({'body': body})
    #     email_values = {
    #         'email_to': email_to,
    #         'subject': subject,
    #         'body_html': render_body
    #     }
    #     email_msg = self.env['mail.mail'].create(email_values)
    #     email_msg.send()

    # @api.multi
    # def send_btn(self):
    #     print(self.select_ids)
    #     print(self.reason_send)
    #     mail_obj = self.env['mail.mail']
    #     recipient = 'recipient@example.com'
    #     subject = 'Test Mail'
    #     body = "Test Message Odoo"
    #     email_values = {
    #         'subject': subject,
    #         'email_to': recipient,
    #         'body_html': body,
    #     }
    #     try:
    #         mail_obj.create(email_values).send()
    #         print("True")
    #         return True
    #     except ValidationError as e:
    #         print("False")
    #         return False

    # def send_btn(self):
    #     mail_template = self.env.ref('my_hospital.report_patient_cards')
    #     if not mail_template:
    #         raise UserError("Email Not Found")
    #
    #     email_to = 'abc@example.com'
    #
    #     rendered_template = mail_template.render_template({'record': self})
    #
    #     mail_values = {
    #         'subject': 'Email Subject',
    #         'email_to': email_to,
    #         'body_html': rendered_template,
    #     }
    #
    #     try:
    #         mail_id = self.env['mail.mail'].create(mail_values)
    #         if mail_id:
    #             mail_id.send()
    #             return True
    #     except AttributeError:
    #         print("There is no such attribute")
    #         return False

    # def send_btn(self):
    #     template_id = self.env.ref('my_hospital.report_patient_cards').id
    #     template = self.env['mail.mail'].browse(template_id)
    #     template.send_mail(self.id, force_send=True)
    #     # print(template_id)
    #     # print(self.id)
    #     # print(template)

    # def send_btn(self):
    #     template = self.env.ref('my_hospital.mail_to_patient')
    #     print(template)
    #     for rec in self:
    #         template.send_mail(rec.id, force_send=True)

    # def send_btn(self):
    #     pass
