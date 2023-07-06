Feature: sightseeing-options
  Scenario Outline: asking for sightseeing options nearby
    Given an english speaking user
      When the user says "<sightseeing options sentence>"
      Then "hotel-test" should reply with dialog from "SightseeingOptionsList"

   Examples: sightseeing options sentences
        | sightseeing options sentence |
        | Welche Sehenswürdigkeiten gibt es in der Nähe |
        | Gibt es hier irgendwelche Sehenswürdigkeiten |
        | Was sind die berühmten Attraktionen in der Nähe |
        | Hast du Empfehlungen für Sightseeing |
        | Gibt es berühmte Wahrzeichen hier? |
        | Empfohlene Orte zum Besuchen |
        | gibt mir bitte eine Liste von bemerkenswerten Orten zum Besuchen |
        | Was kann ich hier machen |
        | Was kann man in der Stadt machen |
        | Was kann man hier erkunden |
        | Was kann man in der Stadt hier sehen |
        | Was kann man hier sehen |
        | Was kann ich in der Gegend anschauen |
