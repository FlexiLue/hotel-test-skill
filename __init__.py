from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class HotelTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # @intent_file_handler('test.hotel.intent')
    # def handle_test_hotel(self, message):
    #     self.speak_dialog('test.hotel')

    @intent_handler(IntentBuilder('BreakfastTimeIntent').require('BreakfastTimesKeyword'))
    def handle_breakfast_times_intent(self, message):
        self.speak_dialog('test.hotel.dialog')


def create_skill():
    return HotelTest()

