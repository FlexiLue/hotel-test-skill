Feature: damage-reporting
  Scenario Outline: report damaged lamp in bathroom
    Given an english speaking user
      When the user says "<damage report sentences>"
      Then "hotel-test" should reply with dialog from "DamageReportingFirstQuestion"
      Then the user says "meine Lampe im bad funktioniert nicht mehr wenn ich sie anschalten möchte"
      Then "hotel-test" should reply with dialog from "DamageReportingEndSentence"

   Examples: Bathroom sentences
        | damage report sentences |
        | die lampe im bad geht nicht mehr |
        | ich würde gerne melden dass die lampe im bad nicht mehr funktioniert |
        | Das Licht im Bad funktioniert nicht mehr |
        | Die Spiegellampe ist kaputt |
        | ich habe kein Licht mehr im Bad |