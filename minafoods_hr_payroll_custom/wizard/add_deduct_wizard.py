from odoo import fields, models, _, api


class CreateAddAlwWizard(models.TransientModel):
    _name = 'add.alw.wizard'
    _description = 'Create Add or Deduction Wizard'

    type = fields.Selection(
        [('alw_call', "بدل إتصالات"),
         ('alw_trans', "بدل موصلات"),
         ('alw_clk', "بدل كلارك"),
         ('alw_bonus', "حافز"),
         ('alw_bonus1', "بونص"),
         ('alw_bonus2', "حافز انتظام"),
         ('alw_food', "بدل وجبة"),
         ('alw_late', "بدل سهر"),
         ('alw_late2', "مصروف سهر"),
         ('alw_add', "أجر إضافي"),
         ('duc_uniform', "خصم يونيفورم"),
         ('duc_minus', "جزاءات"),
         ('duc_loans', "سلف مؤقت"),
         ('duc_loans1', "سلف دائم"),
         ])

    type_input = fields.Selection([('day', 'Day'),
                                   ('amount', 'Amount')])

    value = fields.Float()

    def _get_default_contract_ids(self):
        if self.env.context.get("active_ids"):
            return self.env.context.get("active_ids")

    contract_ids = fields.Many2many(
        'hr.contract', string="Contracts",
        default=_get_default_contract_ids,
    )

    def action_confirm(self):
        self.ensure_one()

        if self.value:
            if self.type_input == 'amount':
                for contract in self.contract_ids:
                    if self.type == 'alw_call':
                        contract.alw_call += self.value
                    if self.type == 'alw_trans':
                        contract.alw_trans += self.value
                    if self.type == 'alw_clk':
                        contract.alw_clk += self.value
                    if self.type == 'alw_bonus':
                        contract.alw_bonus += self.value
                    if self.type == 'alw_bonus1':
                        contract.alw_bonus1 += self.value
                    if self.type == 'alw_bonus2':
                        contract.alw_bonus2 += self.value
                    if self.type == 'alw_food':
                        contract.alw_food += self.value
                    if self.type == 'alw_late':
                        contract.alw_late += self.value
                    if self.type == 'alw_late2':
                        contract.alw_late2 += self.value
                    if self.type == 'alw_add':
                        contract.alw_add += self.value
                    if self.type == 'duc_uniform':
                        contract.duc_uniform += self.value
                    if self.type == 'duc_minus':
                        contract.duc_minus += self.value
                    if self.type == 'duc_loans':
                        contract.duc_loans += self.value
                    if self.type == 'duc_loans1':
                        contract.duc_loans1 += self.value
            if self.type_input == 'day':
                for contract in self.contract_ids:
                    if self.type == 'alw_call':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_call += value
                    if self.type == 'alw_trans':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_trans += value
                    if self.type == 'alw_clk':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_clk += value
                    if self.type == 'alw_bonus':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_bonus += value
                    if self.type == 'alw_bonus1':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_bonus1 += value
                    if self.type == 'alw_bonus2':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_bonus2 += value
                    if self.type == 'alw_food':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_food += value
                    if self.type == 'alw_late':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_late += value
                    if self.type == 'alw_late2':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_late2 += value
                    if self.type == 'alw_add':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.alw_add += value
                    if self.type == 'duc_uniform':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.duc_uniform += value
                    if self.type == 'duc_minus':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.duc_minus += value
                    if self.type == 'duc_loans':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.duc_loans += value
                    if self.type == 'duc_loans1':
                        value = (contract.wage / (contract.no_days_month - contract.number_off_days)) * self.value
                        contract.duc_loans1 += value

    def action_reset(self):
        self.ensure_one()
        for contract in self.contract_ids:
            contract.number_of_days = 0
            contract.number_of_hours = 0
            contract.alw_call = 0
            contract.alw_trans = 0
            contract.alw_clk = 0
            contract.alw_bonus = 0
            contract.alw_bonus1 = 0
            contract.alw_bonus2 = 0
            contract.alw_food = 0
            contract.alw_late = 0
            contract.alw_late2 = 0
            contract.alw_add = 0
            contract.duc_uniform = 0
            contract.duc_minus = 0
            contract.duc_loans = 0
            contract.duc_loans1 = 0
            contract.ovr_time = 0
            contract.late_time = 0
            contract.absence_days = 0
            contract.alw_ovr_time = 0
            contract.duc_late_time = 0
            contract.duc_absence_days = 0
