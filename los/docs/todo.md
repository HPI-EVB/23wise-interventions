# ToDo's
## Data exploration
- Figures mit Verteilung
    - Geschlechter
    - Diagnosen (ICD123 ohne .X)
    - Verweildauer
    - Alter
    - vwd_investigationresults
        - welche Parameter in wie vielen Fällen vorhanden? --> welche werden standardmäßig gemacht?
    - vwd_service
        - anschauen, was hier so drin liegt, ob damit was anzufangen ist

## Data cleaning 
- Was machen wir mit Babies (& Diagnose Z38)? Sind schieinbar stark überrepräsentiert
- Report: "Wir betrachten keine manuell gelöschten Patient:innen. Es k ̈onnte sich bei diesen Patient:innen um Duplikate oder anderweitige Fehler handeln." --> ist das schon vorbereitet?
- Report: "Das derzeitige System existiert erst seit 2013. Vorherige Daten wurden im Jahr 2012 in das derzeitige System migriert, was unlogische Artefakte produziert hat. Deswegen haben wir nur Daten von nach 2013 betrachtet." --> sind Daten von vor 2013 vorhanden? Wenn ja, was für Artefakte könnten das sein?
- Sind F-Diagnosen drin? (Psychiatrie)

## Feature Selection
- ist die Verwendung von PheCodes anstelle der ICD-10 sinnvoll?
