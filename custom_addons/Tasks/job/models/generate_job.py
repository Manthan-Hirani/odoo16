from odoo import api, fields, models
from odoo.exceptions import ValidationError
import random


class GenerateJob(models.Model):
    _name = 'generate.job'
    _description = 'Generate Job'

    name = fields.Char(string="Opening Kick-off ", help="Enter Your Name !!!!")
    skills = fields.Many2many('hr.applicant.category', string="Skills")
    min_exp_req = fields.Integer(string="Minimum Exp. Req.", default="0", help="Enter Exp. Of Year !!!!")
    max_exp_req = fields.Integer(string="Maximum Exp. Req.", default="0", help="Enter Exp. Of Year !!!!")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Required Priority', tracking=True)
    open_date = fields.Date(string="Opened Date", default=fields.Date.context_today)
    expected_end_date = fields.Date(string="Expected End Date")
    expected_new_employee = fields.Integer(string="Expected New Employee", default="1")
    approver = fields.Many2one('res.users', string="Approver")
    description = fields.Text(string="Job Description")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted')], default='draft', string='Status', required=True)

    # ***************** This function is run when the button is click **************** #
    def action_create_job(self):
        # print(self.state)
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'submitted'
        # print(self.state)

        candidate_record = self.env['recruitment.candidate'].search([])
        hr_applicant = self.env['hr.applicant'].search([])
        # print(self.env['hr.applicant'].search([]))
        # print(candidate_record)
        # print(job_record)
        for cr in candidate_record:  # 4
            # print(self.skills.id)
            # print(cr.skills.id)
            # print(cr)
            # print(self.min_exp_req, cr.current_experience)
            # print(self.max_exp_req, cr.current_experience)
            # print(self.skills, cr.skills)
            a = []
            b = []
            for i in self.skills:
                a.append(i.id)
            for j in cr.skills:
                b.append(j.id)

            a = set(a)
            b = set(b)

            if (self.min_exp_req <= cr.current_experience) and (self.max_exp_req >= cr.current_experience) and (
                    a.issubset(b)):
                count = 0
                # print("Yes")
                # print(cr.skills)
                for hra in hr_applicant:  # 17
                    # print(hra)

                    if hra.partner_name != cr.name:
                        # print("IN hra break")
                        count = 0

                    else:
                        count = 1
                        break

                if count == 0:
                    self.env['hr.applicant'].create(
                        {'partner_name': cr.name, 'partner_mobile': cr.mobile, 'salary_expected': cr.expected_salary,
                         'categ_ids': cr.skills, 'job_id': cr.applied_job, 'name': self.name,
                         'priority': self.priority, 'email_from': cr.email})

            # else:
            #     print("NO")

        return {
            'effect': {
                'fadeout': 'medium',
                'message': 'Job Created',
                'type': 'rainbow_man',
            }
        }

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = "draft"
    #
    # def action_submiteed(self):
    #     for rec in self:
    #         rec.state = "submiteed"
    #
    # def action_approved(self):
    #     for rec in self:
    #         rec.state = "approved"
    #     return {
    #         'effect': {
    #             'fadeout': 'slow',
    #             'message': "Approved !!!",
    #             'type': 'rainbow_man',
    #         }
    #     }
    #
    # def action_refuced(self):
    #     for rec in self:
    #         rec.state = "refuced"
