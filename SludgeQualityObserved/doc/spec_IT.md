<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: FanghiQualitàOsservata    
==============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/SludgeQualityObserved/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Il modello di dati della qualità dei fanghi è destinato a rappresentare i parametri di qualità dei fanghi.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `AOX[number]`: Concentrazione di alogeni organici adsorbibili (AOX)  - `As[number]`: Arsenico. Concentrazione di arsenico  - `B[number]`: Boro. Concentrazione di boro  - `Be[number]`: Berillio. Concentrazione di berillio  - `C-ORG[number]`: Carbonio organico. Concentrazione di carbonio organico  - `C10-C40[number]`: Concentrazione di idrocarburi C10-C40  - `Cd[number]`: Cadmio. Concentrazione di cadmio  - `Cr[number]`: Cromo. Concentrazione di cromo  - `Cr-VI[number]`: Cromo VI. Concentrazione di cromo allo stato di ossidazione +6  - `Cu[number]`: Rame. Concentrazione di rame  - `DEHP[number]`: Dietilesilftalato. Concentrazione di DEHP  - `Hg[number]`: Mercurio. Concentrazione di mercurio  - `IPA[number]`: Somma di alcol isopropilico Somma del contenuto di alcol isopropilico  - `K-TOT[number]`: Potassio totale. Contenuto totale di potassio  - `N-TOT[number]`: Azoto totale. L'azoto totale (TN) è la somma dell'azoto nitrico (NO3-N), dell'azoto nitritico (NO2-N), dell'azoto ammoniacale (NH3-N) e dell'azoto legato alle sostanze organiche.  - `Ni[number]`: Nichel. Concentrazione di nichel  - `P-TOT[number]`: Fosforo totale. Il fosforo totale è una misura di tutte le forme di fosforo presenti nell'acqua, compreso quello disciolto e quello particolato, organico e inorganico.  - `PCB[number]`: Bifenili policlorurati Concentrazione di bifenili policlorurati  - `Se[number]`: Selenio. Concentrazione di selenio  - `Zn[number]`: Zinco. Concentrazione di zinco  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateObserved[string]`: La data e l'ora di questa osservazione in formato ISO8601 UTC. Può essere rappresentata da un istante di tempo specifico o da un intervallo ISO8601.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `faecal-coliforms[number]`: Concentrazione di coliformi fecali (numero più probabile per grammo di solidi)  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `measurand[array]`: Una matrice di stringhe contenenti dettagli (vedi formato sotto) sui misurandi extra forniti da questa osservazione.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `pH[number]`: Acidità o basicità di una soluzione acquosa  - `refPointOfInterest[*]`: Un riferimento a un punto di interesse associato a questa osservazione.  - `salmonella[number]`: Concentrazione di Salmonella (Numero più probabile per grammo di solidi)  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `toluene[number]`: Concentrazione di toluene  - `type[string]`: Tipo di entità NGSI. Deve essere SludgeQualityObserved (Qualità dei fanghi osservata).  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SludgeQualityObserved:      
  description: Sludge Quality data model is intended to represent sludge quality parameters.      
  properties:      
    AOX:      
      description: Concentration of Adsorbable Organically bound halogens (AOX)      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    As:      
      description: Arsenic. Concentration of arsenic      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    B:      
      description: Boron. Concentration of boron      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Be:      
      description: Beryllium. Concentration of Beryllium      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    C-ORG:      
      description: Organic Carbon. Concentration of organic carbon      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: percentage of SS (min)      
    C10-C40:      
      description: Concentration of Hydrocarbons C10-C40      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Cd:      
      description: Cadmium. Concentration of cadmium      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Cr:      
      description: Chromium. Concentration of chromium      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Cr-VI:      
      description: Chromium VI. Concentration of chromium at the oxidation state +6      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Cu:      
      description: Copper. Concentration of copper      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    DEHP:      
      description: Diethylhexyl phthalate. Concentration of DEHP      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Hg:      
      description: Mercury. Concentration of mercury      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    IPA:      
      description: Sum of isopropyl alcohol Sum of content of isopropyl alcohol      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    K-TOT:      
      description: Total potassium. Total content of potassium      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: percentage of SS (min)      
    N-TOT:      
      description: 'Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: percentage of SS (min)      
    Ni:      
      description: Nickel. Concentration of Nickel      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    P-TOT:      
      description: 'Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: percentage of SS (min)      
    PCB:      
      description: Polychlorinated biphenyls Concentration of polychlorinated biphenyls      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Se:      
      description: Selenium. Concentration of selenium      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    Zn:      
      description: Zinc. Concentration of zinc      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
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
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    faecal-coliforms:      
      description: Concentration of fecal coliforms (Most Probable Number per gram solids)      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: MPN/g SS (max)      
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
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
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
        description: Every measurand provided by this observation      
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
          type: Property      
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
    salmonella:      
      description: Concentration of Salmonella (Most Probable Number per gram solids)      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: MPN/g SS (max)      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    toluene:      
      description: Concentration of Toluene      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
        units: mg/Kg SS      
    type:      
      description: NGSI Entity type. It has to be SludgeQualityObserved      
      enum:      
        - SludgeQualityObserved      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - dateObserved      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/SludgeQualityObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteWater/SludgeQualityObserved/schema.json      
  x-model-tags: B-WaterSmart      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### SludgeQualityObserved Valori-chiave NGSI-v2 Esempio    
Ecco un esempio di SludgeQualityObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SludgeQualityObserved:001",  
  "type": "SludgeQualityObserved",  
  "dateObserved": "2023-07-02T10:30:00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      45.5197,  
      12.19351  
    ]  
  },  
  "pH": 7.5,  
  "N-TOT": 0.063,  
  "P-TOT": 0.024,  
  "K-TOT": 0.002,  
  "C-ORG": 0.397,  
  "PCB": 0.0,  
  "As": 33.4,  
  "B": 50.8,  
  "Be": 0.3,  
  "Cd": 2.7,  
  "Cr": 46.7,  
  "Cr-VI": 0.05,  
  "Cu": 264.8,  
  "Hg": 1.6,  
  "Ni": 33.1,  
  "Se": 4.1,  
  "Zn": 924.8,  
  "IPA": 1.6,  
  "toluene": 0.0,  
  "AOX": 500.0,  
  "DEHP": 100.0,  
  "C10-C40": 5483.0,  
  "salmonella": 100,  
  "faecal-coliforms": 10000  
}  
```  
</details>    
#### FanghiQualitàOsservata NGSI-v2 normalizzata Esempio    
Ecco un esempio di SludgeQualityObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "sludgequalityobserved:Venice:D1",  
  "type": "SludgeQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2023-07-02T10:30:00Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        45.5197,  
        12.19351  
      ]  
    }  
  },  
  "pH": {  
    "type": "Number",  
    "value": 7.5  
  },  
  "N-TOT": {  
    "type": "Number",  
    "value": 0.063  
  },  
  "P-TOT": {  
    "type": "Number",  
    "value": 0.024  
  },  
  "K-TOT": {  
    "type": "Number",  
    "value": 0.002  
  },  
  "C-ORG": {  
    "type": "Number",  
    "value": 0.397  
  },  
  "PCB": {  
    "type": "Boolean",  
    "value": false  
  },  
  "As": {  
    "type": "Number",  
    "value": 33.4  
  },  
  "B": {  
    "type": "Number",  
    "value": 50.8  
  },  
  "Be": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "Cd": {  
    "type": "Number",  
    "value": 2.7  
  },  
  "Cr": {  
    "type": "Number",  
    "value": 46.7  
  },  
  "Cr-VI": {  
    "type": "Number",  
    "value": 0.05  
  },  
  "Cu": {  
    "type": "Number",  
    "value": 264.8  
  },  
  "Hg": {  
    "type": "Number",  
    "value": 1.6  
  },  
  "Ni": {  
    "type": "Number",  
    "value": 33.1  
  },  
  "Se": {  
    "type": "Number",  
    "value": 4.1  
  },  
  "Zn": {  
    "type": "Number",  
    "value": 924.8  
  },  
  "IPA": {  
    "type": "Number",  
    "value": 1.6  
  },  
  "toluene": {  
    "type": "Boolean",  
    "value": false  
  },  
  "AOX": {  
    "type": "Number",  
    "value": 500.0  
  },  
  "DEHP": {  
    "type": "Number",  
    "value": 100.0  
  },  
  "C10-C40": {  
    "type": "Number",  
    "value": 5483.0  
  },  
  "salmonella": {  
    "type": "Number",  
    "value": 100  
  },  
  "faecal-coliforms": {  
    "type": "Number",  
    "value": 10000  
  }  
}  
```  
</details>    
#### SludgeQualityObserved Valori-chiave NGSI-LD Esempio    
Ecco un esempio di SludgeQualityObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SludgeQualityObserved:sludgequalityobserved:Venice:D1",  
  "type": "SludgeQualityObserved",  
  "dateObserved": "2023-07-02T10:30:00Z",  
  "location": {  
    "coordinates": [  
      45.5197,  
      12.19351  
    ],  
    "type": "Point"  
  },  
  "pH": 7.5,  
  "N-TOT": 0.063,  
  "P-TOT": 0.024,  
  "K-TOT": 0.002,  
  "C-ORG": 0.397,  
  "PCB": 0.0,  
  "As": 33.4,  
  "B": 50.8,  
  "Be": 0.3,  
  "Cd": 2.7,  
  "Cr": 46.7,  
  "Cr-VI": 0.05,  
  "Cu": 264.8,  
  "Hg": 1.6,  
  "Ni": 33.1,  
  "Se": 4.1,  
  "Zn": 924.8,  
  "IPA": 1.6,  
  "toluene": 0.0,  
  "AOX": 500.0,  
  "DEHP": 100.0,  
  "C10-C40": 5483.0,  
  "salmonella": 100,  
  "faecal-coliforms": 10000,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/incubated/SMARTWATER/SludgeQualityObserved/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Qualità dei fanghiOsservati NGSI-LD normalizzati Esempio    
Ecco un esempio di SludgeQualityObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SludgeQualityObserved:sludgequalityobserved:Venice:D1",  
   "type": "SludgeQualityObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-07-02T10:30:00Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        45.51970,  
        12.19351  
      ]  
    }  
  },  
  "pH": {  
    "type": "Number",  
    "value": 7.5  
  },  
  "N-TOT": {  
    "type": "Number",  
    "value": 0.063  
  },  
  "P-TOT": {  
    "type": "Number",  
    "value": 0.024  
  },  
  "K-TOT": {  
    "type": "Number",  
    "value": 0.002  
  },  
  "C-ORG": {  
    "type": "Number",  
    "value": 0.397  
  },  
  "PCB": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "As": {  
    "type": "Number",  
    "value": 33.4  
  },  
  "B": {  
    "type": "Number",  
    "value": 50.8  
  },  
  "Be": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "Cd": {  
    "type": "Number",  
    "value": 2.7  
  },   
  "Cr": {  
    "type": "Number",  
    "value": 46.7  
  },  
  "Cr-VI": {  
    "type": "Number",  
    "value": 0.05  
  },  
  "Cu": {  
    "type": "Number",  
    "value": 264.8  
  },  
  "Hg": {  
    "type": "Number",  
    "value": 1.6  
  },  
  "Ni": {  
    "type": "Number",  
    "value": 33.1  
  },  
  "Se": {  
    "type": "Number",  
    "value": 4.1  
  },  
  "Zn": {  
    "type": "Number",  
    "value": 924.8  
  },  
  "IPA": {  
    "type": "Number",  
    "value": 1.6  
  },  
  "toluene": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "AOX": {  
    "type": "Number",  
    "value": 500.0  
  },  
  "DEHP": {  
    "type": "Number",  
    "value": 100.0  
  },  
  "C10-C40": {  
    "type": "Number",  
    "value": 5483.0  
  },  
  "salmonella": {  
    "type": "Number",  
    "value": 100  
  },  
  "faecal-coliforms": {  
    "type": "Number",  
    "value": 10000  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
