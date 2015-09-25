# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Version
from twilio.rest.pricing.v1.phone_number import PhoneNumberContext
from twilio.rest.pricing.v1.voice import VoiceContext


class V1(Version):

    def __init__(self, domain):
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._phone_numbers = None
        self._voice = None

    @property
    def phone_numbers(self):
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberContext(self)
        return self._phone_numbers

    @property
    def voice(self):
        if self._voice is None:
            self._voice = VoiceContext(self)
        return self._voice

    def __repr__(self):
        return '<Twilio.Pricing.V1>'