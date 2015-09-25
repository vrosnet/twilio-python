# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Domain
from twilio.rest.conversations.v1 import V1


class Conversations(Domain):

    def __init__(self, twilio):
        super(Conversations, self).__init__(twilio)
        
        self.base_url = 'https://conversations.twilio.com'
        """ :type : str """
        self._v1 = None
        """ :type : twilio.rest.conversations.v1.V1 """

    @property
    def v1(self):
        """
        :returns: Version v1 of conversations
        :rtype: twilio.rest.conversations.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def conversations(self):
        """
        :rtype: twilio.rest.conversations.v1.conversation.ConversationContext
        """
        return self.v1.conversations

    def __repr__(self):
        return '<Twilio.Conversations>'