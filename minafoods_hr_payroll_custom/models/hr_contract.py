# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

import calendar
import datetime


class HrContract(models.Model):
    _inherit = 'hr.contract'

    number_of_days = fields.Float(string='Number of Days')
    number_of_hours = fields.Float(string='Number of Hours')

    no_days_month = fields.Integer(compute='_compute_no_days_month')
    number_off_days = fields.Float(string='Number of off Days')

    def _compute_no_days_month(self):
        now = datetime.datetime.now()
        for rec in self:
            rec.no_days_month = calendar.monthrange(now.year, now.month)[1]

    # allowances
    alw_call = fields.Float(digits=dp.get_precision('Payroll'))
    alw_trans = fields.Float(digits=dp.get_precision('Payroll'))
    alw_clk = fields.Float(digits=dp.get_precision('Payroll'))
    alw_bonus = fields.Float(digits=dp.get_precision('Payroll'))
    alw_bonus1 = fields.Float(digits=dp.get_precision('Payroll'))

    # حافز إنتظام
    alw_bonus2 = fields.Float(digits=dp.get_precision('Payroll'),
                              compute='_compute_alw_bonus2')

    def _compute_alw_bonus2(self):
        for rec in self:
            if not rec.absence_days and rec.no_days_month - rec.number_off_days == rec.number_of_days:
                rec.alw_bonus2 = rec.wage / rec.no_days_month
            else:
                rec.alw_bonus2 = 0
    alw_food = fields.Float(digits=dp.get_precision('Payroll'))

    alw_add = fields.Float(digits=dp.get_precision('Payroll'))

    # Deductions
    duc_uniform = fields.Float(digits=dp.get_precision('Payroll'))
    duc_minus = fields.Float(digits=dp.get_precision('Payroll'))
    duc_loans = fields.Float(digits=dp.get_precision('Payroll'))
    duc_loans1 = fields.Float(digits=dp.get_precision('Payroll'))

    ovr_time = fields.Float()
    late_time = fields.Float()
    absence_days = fields.Float()

    alw_ovr_time = fields.Float(compute='_compute_alw_ovr_time', digits=dp.get_precision('Payroll'))
    duc_late_time = fields.Float(compute='_compute_duc_late_time', digits=dp.get_precision('Payroll'))
    duc_absence_days = fields.Float(compute='_compute_duc_absence_days', digits=dp.get_precision('Payroll'))

    no_late_days = fields.Float()
    total_late_bonus = fields.Float()

    # alw_late = حافز السهر الإضافي بعد حساب الافر تايمو
    # alw_late2 = وجبة السهر

    alw_late = fields.Float(compute='_compute_alw_late', digits=dp.get_precision('Payroll'))
    alw_late2 = fields.Float(compute='_compute_alw_late', digits=dp.get_precision('Payroll'))

    @api.depends('no_late_days', 'total_late_bonus')
    def _compute_alw_late(self):
        for rec in self:
            if rec.no_late_days and rec.total_late_bonus:
                rec.alw_late = ((rec.wage/(rec.no_days_month-rec.number_off_days)) / rec.resource_calendar_id.hours_per_day) * rec.total_late_bonus
                rec.alw_late2 = rec.no_late_days * 10
            else:
                rec.alw_late = 0
                rec.alw_late2 = 0

    @api.depends('ovr_time')
    def _compute_alw_ovr_time(self):
        for rec in self:
            if rec.ovr_time:
                rec.alw_ovr_time = ((rec.wage/(rec.no_days_month-rec.number_off_days)) / rec.resource_calendar_id.hours_per_day) * rec.ovr_time
            else:
                rec.alw_ovr_time = 0

    @api.depends('late_time')
    def _compute_duc_late_time(self):
        for rec in self:
            if rec.late_time:
                rec.duc_late_time = ((rec.wage/(rec.no_days_month-rec.number_off_days)) / rec.resource_calendar_id.hours_per_day) * rec.late_time
            else:
                rec.duc_late_time = 0

    @api.depends('absence_days')
    def _compute_duc_absence_days(self):
        for rec in self:
            if rec.absence_days:
                rec.duc_absence_days = rec.absence_days * (rec.wage/(rec.no_days_month-rec.number_off_days))
            else:
                rec.duc_absence_days = 0

    def _action_add_alw(self):
        action = self.env["ir.actions.actions"]._for_xml_id("minafoods_hr_payroll_custom.add_alw_wizard_action")
        action['context'] = repr(self.env.context)
        return action
