# coding=utf-8

import time

from fbchat import log, Client
from fbchat.models import *
from fbchat.models import Message

from var._collect import *
from functions.response import ResponseBy


class Invite(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # Invite Mikky into chat
        if message_object.text in init_list:
            
            self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_1()), thread_id=thread_id, thread_type=thread_type)
            self.setTypingStatus(TypingStatus.STOPPED, thread_id=thread_id, thread_type=thread_type)

            self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_2()), thread_id=thread_id, thread_type=thread_type)
            self.setTypingStatus(TypingStatus.STOPPED, thread_id=thread_id, thread_type=thread_type)

            self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.welcome_word_line_3()), thread_id=thread_id, thread_type=thread_type)
            self.setTypingStatus(TypingStatus.STOPPED, thread_id=thread_id, thread_type=thread_type)
            
            # Use when long AFK
            self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
            self.send(Message(text=ResponseBy.goto_lineadd()), thread_id=thread_id, thread_type=thread_type)
            self.setTypingStatus(TypingStatus.STOPPED, thread_id=thread_id, thread_type=thread_type)
            time.sleep(1)
            # Mikky:    100006035379384
            # Pen:      100012528676832
            self.addUsersToGroup([100006035379384, ], thread_id=thread_id)
            self.markAsDelivered(thread_id, message_object.uid)
            self.markAsRead(thread_id)
