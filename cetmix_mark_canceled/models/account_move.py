from odoo import models, fields, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_canceled = fields.Boolean(
        string='Canceled',
        default=False,
        help="Mark this entry as canceled technically."
    )

    def post(self):
        """
        Overwrite post-method to check the field is_canceled.
        """
        for move in self:
            if move.is_canceled:
                # Raise an error that prevents saving and shows a pop-up to the user
                raise UserError(_("You cannot post an entry that is marked as canceled."))
        
        # If there is no obstacle, call the original Odoo logic (super)
        return super(AccountMove, self).post()