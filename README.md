# Pyodide Tutorial mit Datensätze aus Berlin

Diese Arbeit basiert auf diesem 
[Pyodide-Tutorial](https://testdriven.io/blog/build-spa-with-python-part-1/#pandas-data-manipulation) 
und verwendet [einen Datensatz von Open Data Berlin](https://daten.berlin.de/datensaetze/stra%C3%9Fenverkehrsunf%C3%A4lle-nach-unfallort-berlin-2021).
Wir berechnen die Anzahl der Unfälle pro Bezirk in der Stadt Berlin für das Jahr 2021.
Um die Tabelle zu sehen, öffnen Sie bitte `index.html` in Ihrem Browser.

Zusätzlich präsentieren wir eine Karte von Berlin mit allen Unfallorten.

![](https://github.com/guadiromero/pyodide_tutorial/blob/main/plot.png)

Die Karte kann mit dem folgenden Befehl gezeichnet werden.

```
python script_plot.py [DATENSATZ] [SHAPEFILE]
```

Zum Beispiel:

```
python script_plot.py https://raw.githubusercontent.com/guadiromero/pyodide_tutorial/main/berlin_unfaelle_2021.csv https://raw.githubusercontent.com/guadiromero/pyodide_tutorial/main/bezirksgrenzen.shp.zip
```
