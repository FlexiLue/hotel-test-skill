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
        self.food_options = ["Schnitzel mit Pommes", "Käsespätzle", "Maultaschen mit Salat", "Chicken Nuggets"]

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

    @intent_handler(IntentBuilder("RoomServiceIntent").require("RoomServiceKeyword"))
    def handle_room_service_intent(self, message):
        self.speak("Wir haben momentan folgende Speisen auf der Karte. Wähle eine der Optionen.")
        food_option = self.ask_selection(self.food_options, "", None, 0.5, False)
        if food_option is not None:
            answer = self.ask_yesno("RoomServiceConfirmation", {"food_option": food_option})
            if answer == "yes":
                self.speak("Vielen Dank, die Bestellung ist so eben in der Küche eingegangen und wird dir bald gebracht.")
            else:
                self.speak("Falls du doch nochmal hunger hast, melde dich gerne erneut bei mir")
        else:
            self.speak("Falls du doch nochmal hunger hast, melde dich gerne erneut bei mir")

    @intent_handler(IntentBuilder("SwimmingPoolOccupancyIntent").require("SwimmingPoolKeyword"))
    def handle_swimming_pool_occupancy_intent(self, message):
        self.speak("Die momentane Auslastung ist niedrig.")

    @intent_handler(IntentBuilder("SightseeingOptionsIntent").one_of("SightseeingActionKeyword", "SightseeingKeyword"))
    def handle_sightseeing_options_intent(self, message):
        self.speak_dialog("SightseeingOptionsList")
        sightseeing_option = self.ask_selection(self.sightseeing_options, "", None, 0.5, False)
        self.log.info(sightseeing_option)
        if sightseeing_option and sightseeing_option != "Nein danke":
            self.speak_dialog(self.sightseeing_options_mappping.get(sightseeing_option))
            answer = self.ask_yesno("SightseeingTourUpSell", {"sightseeing_option": sightseeing_option})
            if answer == "yes":
                self.speak(
                    "Ok, vielen Dank. Das Ticket wird dir per im Hotel angegebener E-Mail zugesendet. Dort findest du alle weiteren Informationen. Bezahlen kannst du es am Ende des Aufenthalts.")
            if answer == "no":
                self.speak("Alles klar, wir wünschen dir viel Spaß beim Erkunden.")
        else:
            self.speak_dialog("SightseeingOptionsEndWithoutDetails")

def create_skill():
    return HotelTest()
