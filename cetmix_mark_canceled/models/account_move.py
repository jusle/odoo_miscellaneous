from odoo import models, fields, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_canceled = fields.Boolean(
        string='Canceled',
        default=False,
        help="Mark this entry as canceled technically."
    )
