<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: WaterQualityObserved  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell für die Wasserqualität dient der Darstellung von Wasserqualitätsparametern in einem bestimmten Gewässerabschnitt (Fluss, See, Meer usw.)**  
Version: 0.0.6  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `Al[number]`: Aluminium. Konzentration von Aluminium  - `As[number]`: Arsen. Arsenkonzentration  - `B[number]`: Bor. Die Konzentration von Bor  - `Ba[number]`: Barium. Konzentration von Barium  - `Cd[number]`: Cadmium. Konzentration von Cadmium  - `Chla[number]`: Konzentration von Chlorophyll A  - `Cl-[number]`: Konzentration von Chloriden  - `Cr[number]`: Chrom. Die Konzentration von Chrom  - `Cr-III[number]`: Chrom III. Konzentration von Chrom in der Oxidationsstufe +3  - `Cr-VI[number]`: Chrom VI. Konzentration von Chrom in der Oxidationsstufe +6  - `Cu[number]`: Kupfer. Die Konzentration von Kupfer  - `Fe[number]`: Eisen. Konzentration von Eisen  - `Hg[number]`: Quecksilber. Die Quecksilberkonzentration  - `N-TOT[number]`: Gesamt-Stickstoff. Gesamtstickstoff (TN) ist die Summe aus Nitrat-Stickstoff (NO3-N), Nitrit-Stickstoff (NO2-N), Ammoniak-Stickstoff (NH3-N) und organisch gebundenem Stickstoff  - `NH3[number]`: Ammoniak-Konzentration  - `NH4[number]`: Ammonium-Konzentration  - `NO2[number]`: Nitrit-Stickstoff. Konzentration einer Probe in Nitrit-Stickstoff  - `NO3[number]`: Konzentration von Nitraten  - `Ni[number]`: Nickel. Konzentration von Nickel  - `O2[number]`: Gehalt an freiem, nicht gebundenem Sauerstoff  - `P-PO4[number]`: Phosphat-Phosphor. Konzentration von Phosphor als Phosphat  - `P-TOT[number]`: Gesamtphosphor. Der Gesamtphosphor ist ein Maß für alle Formen von Phosphor im Wasser, einschließlich gelöster und partikulärer, organischer und anorganischer  - `PC[number]`: Konzentration des Pigments Phycocyanin, das gemessen werden kann, um die spezifische Konzentration von Cyanobakterien abzuschätzen  - `PE[number]`: Konzentration des Pigments Phycoerythrin, das gemessen werden kann, um die spezifische Konzentration von Cyanobakterien abzuschätzen  - `PO4[number]`: Konzentration von Phosphaten  - `Pb[number]`: Blei. Konzentration von Blei  - `Se[number]`: Selen. Die Selenkonzentration  - `Sn[number]`: Zinn. Die Konzentration von Zinn  - `THC[number]`: Gesamter Kohlenwasserstoff. Konzentration von Gesamtkohlenwasserstoff  - `TKN[number]`: Kjeldahl-Stickstoff insgesamt. Ein Maß, das sowohl die organischen als auch die anorganischen Formen von Stickstoff bestimmt  - `TO[number]`: Gesamtölgehalt. Konzentration des Öls  - `Zn[number]`: Zink. Die Konzentration von Zink  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alkalinity[number]`: Die Alkalinität von Wasser ist sein Säureneutralisationsvermögen, das sich aus der Summe aller titrierbaren Basen zusammensetzt  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `anionic-surfactants[number]`: Konzentration der anionischen Tenside  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Der biochemische Sauerstoffbedarf (BSB) ist die Menge an gelöstem Sauerstoff (DO), die von aeroben biologischen Organismen benötigt (d. h. gefordert) wird, um das in einer bestimmten Wasserprobe vorhandene organische Material bei einer bestimmten Temperatur über einen bestimmten Zeitraum abzubauen.  - `cationic-surfactants[number]`: Konzentrierung von kationischen Tensiden  - `cod[number]`: Der chemische Sauerstoffbedarf (CSB) ist ein indikatives Maß für die Menge an Sauerstoff, die durch Reaktionen in einer gemessenen Lösung verbraucht werden kann.  - `componentAnalyzed[string]`: Das in der Probe analysierte Komponentensymbol  - `componentName[string]`: Der vollständige Name der in der Probe analysierten Komponente  - `concentration[number]`: Die Konzentration der analysierten Komponente in der Probe  - `conductance[number]`: Spezifische Leitfähigkeit  - `conductivity[number]`: Elektrische Leitfähigkeit  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateObserved[string]`: Das Datum und die Uhrzeit dieser Beobachtung im ISO8601 UTC-Format. Sie können durch einen bestimmten Zeitpunkt oder durch ein ISO8601-Intervall dargestellt werden  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Eine Beschreibung dieses Artikels  - `enterococci[number]`: Konzentration von Enterokokken  - `escherichiaColi[number]`: Konzentration von Escherichia coli  - `flow[number]`: Wasserdurchfluss beobachtet.  - `fluoride[number]`: Konzentration von Fluorid  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `measurand[array]`: Ein Array von Strings mit Details (siehe Format unten) über zusätzliche Messwerte, die von dieser Beobachtung geliefert werden  - `name[string]`: Der Name dieses Artikels  - `non-ionic-surfactants[number]`: Konzentration der nichtionischen Tenside  - `orp[number]`: Oxidations-Reduktionspotential  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pH[number]`: Azidität oder Basizität einer wässrigen Lösung  - `refPointOfInterest[*]`: Ein Verweis auf ein mit dieser Beobachtung verbundenes Sonderziel  - `salinity[number]`: Menge der im Wasser gelösten Salze  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `sulphate[number]`: Sulfat-Konzentration  - `sulphite[number]`: Sulfit-Konzentration  - `tds[number]`: Gelöste Feststoffe insgesamt.  - `temperature[number]`: Temperatur  - `total-surfactants[number]`: Konzentration der gesamten Tenside  - `tss[number]`: Schwebende Feststoffe insgesamt  - `turbidity[number]`: Menge des von den Partikeln in der Wassersäule gestreuten Lichts  - `type[string]`: NGSI-Entitätstyp. Es muss WaterQualityObserved sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section    
  properties:    
    Al:    
      description: Aluminium. Concentration of aluminium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    As:    
      description: Arsenic. Concentration of arsenic    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    B:    
      description: Boron. Concentration of boron    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Ba:    
      description: Barium. Concentration of barium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Cd:    
      description: Cadmium. Concentration of cadmium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Chla:    
      description: Concentration of chlorophyll A    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    Cl-:    
      description: Concentration of chlorides    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    Cr:    
      description: Chromium. Concentration of chromium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Cr-III:    
      description: Chromium III. Concentration of chromium at the oxidation state +3    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Cr-VI:    
      description: Chromium VI. Concentration of chromium at the oxidation state +6    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Cu:    
      description: Copper. Concentration of copper    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Fe:    
      description: Iron. Concentration of iron    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Hg:    
      description: Mercury. Concentration of mercury    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    N-TOT:    
      description: Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    NH3:    
      description: Concentration of ammonia    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    NH4:    
      description: Concentration of ammonium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    NO2:    
      description: Nitrite nitrogen. Concentration of a sample in nitrite nitrogen    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    NO3:    
      description: Concentration of nitrates    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    Ni:    
      description: Nickel. Concentration of Nickel    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    O2:    
      description: Level of free, non-compound oxygen present    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    P-PO4:    
      description: Phosphate-phosphorus. Concentration of phosphorus as phosphate    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    P-TOT:    
      description: Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    PC:    
      description: Concentration of pigment phycocyanin which can be measured to estimate cyanobacteria concentrations specifically    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    PE:    
      description: Concentration of pigment phycoerythrin which can be measured to estimate cyanobacteria concentrations specifically    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    PO4:    
      description: Concentration of phosphates    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    Pb:    
      description: Lead. Concentration of lead    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Se:    
      description: Selenium. Concentration of selenium    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Sn:    
      description: Tin. Concentration of tin    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    THC:    
      description: Total hydrocarbon. Concentration of total hydrocarbon    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    TKN:    
      description: Total Kjeldahl Nitrogen. A measure that determines both the organic and the inorganic forms of nitrogen    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    TO:    
      description: Total oil content. Concentration of oil    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    Zn:    
      description: Zinc. Concentration of zinc    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alkalinity:    
      description: The alkalinity of water is its acid-neutralizing capacity comprised of the total of all titratable bases    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    anionic-surfactants:    
      description: Concentration of anionic surfactants    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bod:    
      description: Biochemical oxygen demand (BOD) is the amount of dissolved oxygen (DO) needed (i.e. demanded) by aerobic biological organisms to break down organic material present in a given water sample at certain temperature over a specific time period    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    cationic-surfactants:    
      description: Concentrtation of cationic surfactants    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    cod:    
      description: Chemical oxygen demand (COD) is an indicative measure of the amount of oxygen that can be consumed by reactions in a measured solution    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    componentAnalyzed:    
      description: The component symbol analyzed in the sample    
      type: string    
      x-ngsi:    
        type: Property    
    componentName:    
      description: The component full name analyzed in the sample    
      type: string    
      x-ngsi:    
        type: Property    
    concentration:    
      description: The concentration of the component analyzed in the sample    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    conductance:    
      description: Specific Conductance    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    conductivity:    
      description: Electrical Conductivity    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    enterococci:    
      description: Concentration of Enterococci    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: Total number of bacteria/100mL    
    escherichiaColi:    
      description: Concentration of Escherichia coli    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: Total number of bacteria/100mL    
    flow:    
      description: 'Water Flow observed. '    
      type: number    
      x-ngsi:    
        type: Property    
        units: cubic meters/hour    
    fluoride:    
      description: Concentration of fluoride    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    measurand:    
      description: An array of strings containing details (see format below) about extra measurands provided by this observation    
      items:    
        description: Every element of the array of strings containing details (see format below) about extra measurands provided by this observation    
        type: string    
        x-ngsi:    
          type: Property    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    non-ionic-surfactants:    
      description: Concentration of non-ionic surfactants    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    orp:    
      description: Oxidation-Reduction potential    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    pH:    
      description: Acidity or basicity of an aqueous solution    
      maximum: 14    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: A reference to a point of interest associated to this observation    
      x-ngsi:    
        type: Relationship    
    salinity:    
      description: Amount of salts dissolved in water    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    sulphate:    
      description: Concentration of sulfate    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    sulphite:    
      description: Concentration of sulfite    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    tds:    
      description: 'Total dissolved solids. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Temperature    
      type: number    
      x-ngsi:    
        type: Property    
    total-surfactants:    
      description: Concentration of total surfactants    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    tss:    
      description: Total suspended solids    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    turbidity:    
      description: Amount of light scattered by particles in the water column    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be WaterQualityObserved    
      enum:    
        - WaterQualityObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityObserved/schema.json    
  x-model-tags: NAIADES, DigitalWater.city, B-WaterSmart, Waterverse    
  x-version: 0.0.6    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### WaterQualityObserved NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel eines WaterQualityObserved im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "measurand": [  
    "NO3, 0.01, M1, Concentration of Nitrates"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "temperature": 24.4,  
  "conductivity": 0.005,  
  "pH": 7.4,  
  "NO3": 0.01,  
  "flow": 127.53,  
  "alkalinity": 0.1,  
  "TKN": 1.0,  
  "NO2": 0.09,  
  "N-TOT": 6.0,  
  "P-TOT": 0.6,  
  "P-PO4": 0.5,  
  "Al": 0.01,  
  "As": 0.0,  
  "B": 0.2,  
  "Ba": 0.0,  
  "Cd": 0.001,  
  "Cr": 0.0,  
  "Cr-III": 0.0,  
  "Cr-VI": 0.0,  
  "Cu": 0.0,  
  "Fe": 0.0,  
  "fluoride": 0.1,  
  "Hg": 0.0,  
  "THC": 0.0,  
  "Ni": 0.0,  
  "TO": 0.01,  
  "Pb": 0.0,  
  "Se": 0.0,  
  "Sn": 0.0,  
  "sulphate": 143.3,  
  "sulphite": 0.0,  
  "anionic-surfactants": 0.3,  
  "cationic-surfactants": 0.2,  
  "non-ionic-surfactants": 0.1,  
  "total-surfactants": 0.3,  
  "Zn": 0.0,  
  "componentAnalyzed": "Cl",  
  "componentName": "Chlorine",  
  "concentration": 20  
}  
```  
</details>  
#### WaterQualityObserved NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein WaterQualityObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2017-01-31T06:45:00Z"  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 24.4  
  },  
  "NO3": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.993307,  
        37.362882  
      ]  
    }  
  },  
  "pH": {  
    "type": "Number",  
    "value": 7.4  
  },  
  "measurand": {  
    "type": "StructuredValue",  
    "value": [  
      "NO3, 0.01, M1, Concentration of Nitrates"  
    ]  
  },  
  "conductivity": {  
    "type": "Number",  
    "value": 0.005  
  },  
  "flow": {  
    "type": "Number",  
    "value": 127.53  
  },  
  "alkalinity": {  
    "type": "Number",  
    "value": 0.1  
  },  
  "TKN": {  
    "type": "Boolean",  
    "value": true  
  },  
  "NO2": {  
    "type": "Number",  
    "value": 0.09  
  },  
  "N-TOT": {  
    "type": "Number",  
    "value": 6.0  
  },  
  "P-TOT": {  
    "type": "Number",  
    "value": 0.6  
  },  
  "P-PO4": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "Al": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "As": {  
    "type": "Boolean",  
    "value": false  
  },  
  "B": {  
    "type": "Number",  
    "value": 0.2  
  },  
  "Ba": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Cd": {  
    "type": "Number",  
    "value": 0.001  
  },  
  "Cr": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Cr-III": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Cr-VI": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Cu": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Fe": {  
    "type": "Number",  
    "value": 7.4  
  },  
  "fluoride": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Hg": {  
    "type": "Boolean",  
    "value": false  
  },  
  "THC": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Ni": {  
    "type": "Boolean",  
    "value": false  
  },  
  "TO": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "Pb": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Se": {  
    "type": "Boolean",  
    "value": false  
  },  
  "Sn": {  
    "type": "Boolean",  
    "value": false  
  },  
  "sulphate": {  
    "type": "Number",  
    "value": 143.3  
  },  
  "sulphite": {  
    "type": "Boolean",  
    "value": false  
  },  
  "anionic-surfactants": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "cationic-surfactants": {  
    "type": "Number",  
    "value": 0.2  
  },  
  "non-ionic-surfactants": {  
    "type": "Number",  
    "value": 0.1  
  },  
  "total-surfactants": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "Zn": {  
    "type": "Boolean",  
    "value": false  
  },  
  "componentAnalyzed": {  
    "type": "Text",  
    "value": "Cl"  
  },  
  "componentName": {  
    "type": "Text",  
    "value": "Chlorine"  
  },  
  "concentration": {  
    "type": "Number",  
    "value": 20  
  }  
}  
```  
</details>  
#### WaterQualityObserved NGSI-LD key-values Beispiel  
Hier ist ein Beispiel eines WaterQualityObserved im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "NO3": 0.01,  
  "conductivity": 0.005,  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "location": {  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ],  
    "type": "Point"  
  },  
  "measurand": [  
    "NO3, 0.01, M1, Concentration of Nitrates"  
  ],  
  "pH": 7.4,  
  "temperature": 24.4,  
  "flow": 127.53,  
  "alkalinity": 0.1,  
  "TKN": 1.0,  
  "NO2": 0.09,  
  "N-TOT": 6,  
  "P-TOT": 0.6,  
  "P-PO4": 0.5,  
  "Al": 0.01,  
  "As": 0.0,  
  "B": 0.2,  
  "Ba": 0.0,  
  "Cd": 0.001,  
  "Cr": 0.0,  
  "Cr-III": 0.0,  
  "Cr-VI": 0.0,  
  "Cu": 0.0,  
  "Fe": 0.0,  
  "fluoride": 0.1,  
  "Hg": 0.0,  
  "THC": 0.0,  
  "Ni": 0.0,  
  "TO": 0.01,  
  "Pb": 0.0,  
  "Se": 0.0,  
  "Sn": 0.0,  
  "sulphate": 143.3,  
  "sulphite": 0,  
  "anionic-surfactants": 0.3,  
  "cationic-surfactants": 0.2,  
  "non-ionic-surfactants": 0.1,  
  "total-surfactants": 0.3,  
  "Zn": 0.0,  
  "componentAnalyzed": "Cl",  
  "componentName": "Chlorine",  
  "concentration": 20,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### WaterQualityObserved NGSI-LD normalized Beispiel  
Hier ist ein Beispiel für ein WaterQualityObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "NO3": {  
    "type": "Property",  
    "value": 0.01  
  },  
  "conductivity": {  
    "type": "Property",  
    "value": 0.005  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-31T06:45:00Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.993307,  
        37.362882  
      ]  
    }  
  },  
  "measurand": {  
    "type": "Property",  
    "value": [  
      "NO3, 0.01, M1, Concentration of Nitrates"  
    ]  
  },  
  "pH": {  
    "type": "Property",  
    "value": 7.4  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 24.4  
  },  
  "flow": {  
    "type": "Property",  
    "value": 127.53  
  },  
  "alkalinity": {  
    "type": "Property",  
    "value": 0.1  
  },  
  "TKN": {  
    "type": "Property",  
    "value": 1.0  
  },  
  "NO2": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "N-TOT": {  
    "type": "Property",  
    "value": 6.0  
  },  
  "P-TOT": {  
    "type": "Property",  
    "value": 0.6  
  },  
  "P-PO4": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "Al": {  
    "type": "Property",  
    "value": 0.01  
  },   
  "As": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "B": {  
    "type": "Property",  
    "value": 0.2  
  },  
  "Ba": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Cd": {  
    "type": "Property",  
    "value": 0.001  
  },  
  "Cr": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Cr-III": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Cr-VI": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Cu": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Fe": {  
    "type": "Property",  
    "value": 7.4  
  },  
  "fluoride": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Hg": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "THC": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Ni": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "TO": {  
    "type": "Property",  
    "value": 0.01  
  },  
  "Pb": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Se": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "Sn": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "sulphate": {  
    "type": "Property",  
    "value": 143.3  
  },  
  "sulphite": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "anionic-surfactants": {  
    "type": "Property",  
    "value": 0.3  
  },  
  "cationic-surfactants": {  
    "type": "Property",  
    "value": 0.2  
  },  
  "non-ionic-surfactants": {  
    "type": "Property",  
    "value": 0.1  
  },  
  "total-surfactants": {  
    "type": "Property",  
    "value": 0.3  
  },  
  "Zn": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "componentAnalyzed": {  
    "type": "Property",  
    "value": "Cl"  
  },  
  "componentName": {  
    "type": "Property",  
    "value": "Chlorine"  
  },  
  "concentration": {  
    "type": "Property",  
    "value": 20  
  },  
   "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
