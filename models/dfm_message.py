# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from .dfm import Dlient

CLIENT, ENV, LISTENING = None, None, False


class Message(models.Model):
    _name = 'dfm.message'

    @api.model
    def get_env(self):
        global ENV
        return ENV

    @api.model
    def listen_to_message(self):
        global CLIENT
        global ENV
        global LISTENING
        if not LISTENING:
            CLIENT = Dlient(
                self.env['ir.config_parameter'].get_param('dfm.facebook_account'),
                base64.b64decode(self.env['ir.config_parameter'].get_param('dfm.facebook_password').encode('ascii'))
                    .decode('utf-8'))
            ENV = self.env
            LISTENING = True
            CLIENT.listen()
        return LISTENING

    name = fields.Char()
    message = fields.Text()
    user = fields.Text()

    @api.multi
    def get_message(self):
        return True
        # users = [(user.uid, user.name) for user in client.fetchThreadList()]
        # messages = client.fetchThreadMessages(users[0][0], limit=1000)
        # for rec in self:
        #     rec.user = users
        #     rec.name = users[0][1]
        #     rec.message = '\n-'.join([str(m.text) for m in messages])



