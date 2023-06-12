from mycroft import MycroftSkill, intent_file_handler


class HotelTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.hotel.intent')
    def handle_test_hotel(self, message):
        self.speak_dialog('test.hotel')


def create_skill():
    return HotelTest()

