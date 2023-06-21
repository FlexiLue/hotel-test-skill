Feature: breakfast-times
  Scenario Outline: asking for breakfast times
    Given an english speaking user
      When the user says "<breakfast times sentence>"
      Then "hotel-test" should reply with dialog from "BreakfastTimesInfo"

   Examples: breakfast times sentences
        | breakfast times sentence |
        | Wann ist morgen das Frühstück |
        | Ab wann kann ich frühstücken |
        | Ab wann ist das Frühstück morgen geöffnet |
        | Zu welchen Zeiten kann ich frühstücken |
        | Kannst du mir bitte die Frühstückszeiten sagen |
        | Wann ist morgen Frühstück |