from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True, domain=[('state', '=', 'draft')])
    # appointment_id = fields.Many2one('hospital.appointment', string="Appointment", tracking=True)
    reason_cansel = fields.Char(string="Reason", tracking=True)
    # state = fields.Selection(related='appointment_id.state')
    # print(state)

    def action_cancel(self):
        today = date.today()
        cancel_day = self.env['ir.config_parameter'].get_param('my_hospital.cancel_days')
        # print(cancel_day)
        allowed_date = today + relativedelta.relativedelta(days=int(cancel_day))
        # print(type(allowed_date))
        # print(type(self.appointment_id.booking_date))
        if self.appointment_id.booking_date < allowed_date:
            raise ValidationError(_("You can't cancel this appointment"))

        # if self.appointment_id.booking_date == today:
        #     raise ValidationError(_("You can't cancel today's appointment"))
        else:
            self.appointment_id.state = "cancel"
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }


