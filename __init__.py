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
        self.log.info(message)
        self.speak_dialog('test.hotel')

    #Spiegellampe Kaputt Prozess
    @intent_handler(IntentBuilder("DamageReportingIntent").require('DamageReportingKeyword').optionally('location'))
    def handle_damage_reporting_intent(self, message):
        schaden = self.get_response('DamageReportingFirstQuestion')
        self.log.info(schaden)
    


def create_skill():
    return HotelTest()

