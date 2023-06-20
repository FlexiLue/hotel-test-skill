Feature: damage-reporting
  Scenario: report damaged lamp in bathroom
    Given an German speaking user
     When the user says "die lampe im bad funktioniert nicht mehr"
     Then "hotel-test" should reply with dialog from "DamageReportingFirstQuestion"