# -*- coding: utf-8 -*-
from fbchat import Client, log
from . import dfm_message


class Dlient(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        message_object.text = ' '.join(message_object.text.split()[::-1])
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)
        env = dfm_message.Message.get_env(self)
        print(env['dfm.message'].search([]).mapped('name'))