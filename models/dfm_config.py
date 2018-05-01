# -*- coding: utf-8 -*-
from base64 import b64encode, b64decode

from odoo import api, exceptions, fields, models
from odoo.tools.translate import _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    facebook_account = fields.Char(help=_('Your Facebook Account can be: Login Name / ID / Email / Phone Number.'))
    facebook_password = fields.Char(help=_('Your Facebook password.'))

    @api.model
    def encode(self, string):
        return b64encode(string.encode('ascii')) if string else False

    @api.model
    def decode(self, string):
        return b64decode(string.encode('ascii')) if string else False

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('dfm.facebook_account', self.facebook_account)
        self.env['ir.config_parameter'].sudo().set_param('dfm.facebook_password', self.encode(self.facebook_password))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        account = self.env['ir.config_parameter'].get_param('dfm.facebook_account')
        password = self.decode(self.env['ir.config_parameter'].get_param('dfm.facebook_password'))
        res.update(facebook_account=account, facebook_password=password)
        return res
