from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class HotelTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.sightseeing_options = ["Altstadt Bad Wimpfen", "Salzbergwerk", "Burg Hornberg", "Burg Guttenberg", "Experimenta", "Nein danke"]
        self.sightseeing_options_mappping = {
            "Altstadt Bad Wimpfen": "AltstadtBadWimpfenInfo",
            "Salzbergwerk": "SalzbergwerkInfo",
            "Burg Hornberg": "BurgHornbergInfo",
            "Burg Guttenberg": "BurgGuttenbergInfo",
            "Experimenta": "ExperimentaInfo"
        }

    def sightseeing_options_validator(self, response):
        requested_sightseeing_options = []
        for sightseeing_option in self.sightseeing_options:
            if sightseeing_option in response:
                requested_sightseeing_options(sightseeing_option)
        return requested_sightseeing_options

    @intent_handler(IntentBuilder('BreakfastTimeIntent').require('BreakfastTimesKeyword'))
    def handle_breakfast_times_intent(self, message):
        self.log.info(message)
        self.speak_dialog('BreakfastTimesInfo')

    @intent_handler(IntentBuilder("DamageReportingIntent").require("DamageReportingKeyword").optionally("location"))
    def handle_damage_reporting_intent(self, message):
        schaden = self.get_response('DamageReportingFirstQuestion')
        self.log.info(schaden)
        self.speak_dialog("DamageReportingEndSentence")

    @intent_handler(IntentBuilder("SightseeingOptionsIntent").one_of("SightseeingActionKeyword", "SightseeingKeyword"))
    def handle_sightseeing_options_intent(self, message):
        self.speak_dialog("SightseeingOptionsList")
        sightseeing_option = self.ask_selection(self.sightseeing_options, "", None, 0.5, False)
        self.log.info(sightseeing_option)
        if sightseeing_option and sightseeing_option != "Nein danke":
            self.speak_dialog(self.sightseeing_options_mappping.get(sightseeing_option))
            answer = self.ask_yesno("SightseeingTourUpSell", {"sightseeing_option": sightseeing_option})
            if answer == "yes":
                self.speak("Ok, vielen Dank. Das Ticket wird dir per im Hotel angegebener E-Mail zugesendet. Bezahlen kannst du es am Ende des Aufenthalts.")
            if answer == "no":
                self.speak("Alles klar, wir wünschen dir viel Spaß beim Erkunden.")
        else:
            self.speak_dialog("SightseeingOptionsEndWithoutDetails")

    @intent_handler(IntentBuilder("SwimmingPoolOccupancyIntent").require("SwimmingPoolKeyword"))
    def handle_swimming_pool_occupancy_intent(self, message):
        self.speak("Die momentane Auslastung ist niedrig.")


def create_skill():
    return HotelTest()
