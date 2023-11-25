# Mögliche Features
## Einfach (direkt abrufbar)
- Fachabteilung/Station
    - könnte sinnvoll sein, sich auf eins zu beschränken, wahrscheinlich eher Fachabteilung, da mehr Fälle pro Kategorie?
    - vielleicht aber auch nur Station, weil Fachatbeilung & Diagnose stark korrelieren
- Sex
- birth_decade
- elektiv oder notfall
    - vielleicht über Aufnahemstation oder so?

## Mittel (etwas Umwandlung)
- [Case Mix](https://github.com/HPI-EVB/seminar-starter-doku/blob/main/glossar/Case%20Mix.ipynb)
    - Schweregrad
    - weiß nicht, ob der irgendwo in der Datenbank vorberechnet verfügbar ist
    - alternativ vielleich PCCL (patient complication & comorbidity level)
- Hauptdiagnose
    - ich schlage vor die Stern/Kreuz/Ausrufezeichen-Schreibweise zu ignorieren --> wegparsen
    - könnte sinnvoll sein: mappen der ICD-Codes auf Phecodes, welche besser hierarchisch generalisierbar sind; CAVE nicht alle ICD-Codes haben korrespondierenden PheCode
    - StartDate? CreationDate?
- Nebendiagnosen
    - Anzahl?
    - Schwere nach PCCL?
- BMI
    - Größe und Gewicht möglicherweise in Tabelle vwd_observations
- Postleitzahl
    - Entfernung berechnen?
    - oder einfach häufig/selten?
    - Die Idee ist, dass Menschen, die von weiter weg ins KEVB kommen tendenziell kompliziertere Fälle sein könnten.
- vorherige Krankenhausaufenthalte
    - können wir hier vielleicht den DRG-Code bekommen? --> Vergleich zur Druchschnittsaufenthaltsdauer
    - durchschnittliche Dauer
    - Häufigkeit (in letzten 10 Jahren, älter snid die Daten scheinbar eh nicht?)
- observations
    - ALLGEMEIN
        - value/internalvalue vergleichen
        - imputation-Möglichkeiten anschauen
            - letzter Aufenthalt
            - knn
            - mean
    - Blutdruck
        - in 10 mmHg Schritten?
        - mittlerer arterieller Druck oder systolisch/diastolisch einzeln betrachten?
        - Tagesmedian
        - Veränderung zum Vorwert?
    - Puls
        - in 10/min Schritten?
        - Tagesmedian
        - Veränderung zum Vorwert?
    - Temperatur
        - auf halbe Grad gerundet (ob 37,5°C oder 38°C macht schon einen Unterschied)
        - Veränderung zum Vorwert?
    - gemessener Blutzucker (in mmol/l)
        - wie genau umerchnen? niedriger Zucker ist auf jeden Fall gefährlicher als hoher Zucker, daher reine Abweichung nach oben/unten vom Mittelwert nicht so gut vergleichbar
    - GCS (Bewusstseinszustand)
        - wird erhoben, aber haben wir die Daten?
- vwd_investigationresults
    - ALLGEMEIN
        - müssen wir uns nochmal genauer angucken die Daten
        - imputation-Möglichkeiten anschauen
            - letzter Aufenthalt
            - knn
            - mean
    - Natrium-Konzentration (Blut)
        - Abweichung vom Mittelwert
    - Kalium-Konzentration (Blut)
        - Abweichung vom Mittelwert
        - interessant vor allem Abweichung nach oben bei Nierenkranken
    - Hämoglobin Hb
        - Abweichung vom Mittelwert
        - interessant vor allem Abweichung nach unten bei Verletzung/älteren/chronisch Kranken
    - Leukozyten
        - Abweichung vom Mittelwert
        - zu hoch: Infektion oder Blutkrebs?
        - zu niedrig: Blutkrebs?
    - Trhombozyten, Quick/INR, aPTT
        - Blutgerinnungsparameter
        - oft hohe klinische Relevanz

## Schwer (fragliche Umsetzbarkeit)
- [Grenzverweildauer](https://github.com/HPI-EVB/seminar-starter-doku/blob/main/glossar/Fallpauschale.ipynb)
    - diagnosespezifische Verweildauern sind im Fallkatalog(?) geregelt
    - als Feature vielleicht sogar schon Verhältnis bilden aus bisheriger Aufenthaltsdauer und untere GVWD/durchschnittliche VD/obere GVD
    - aber Mapping ICD-10 --> DRG nötig (sehr schwer)


## Sketch
|Visit-ID   |Diagnose   |patientlocationname/unitcontactedname  |
|:--------------|:--------------|:------------|
|123456         |A90.3          |KARDIO          |