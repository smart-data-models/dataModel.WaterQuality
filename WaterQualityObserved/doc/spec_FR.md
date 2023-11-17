<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Qualité de l'eau observée    
==================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Le modèle de données sur la qualité de l'eau est destiné à représenter les paramètres de qualité de l'eau dans une certaine section de la masse d'eau (rivière, lac, mer, etc.).    
version : 0.0.5    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `Al[number]`: Aluminium. Concentration d'aluminium  - `As[number]`: Arsenic. Concentration d'arsenic  - `B[number]`: Bore. Concentration de bore  - `Ba[number]`: Baryum. Concentration de baryum  - `Cd[number]`: Cadmium. Concentration de cadmium  - `Chla[number]`: Concentration de chlorophylle A  - `Cl-[number]`: Concentration de chlorures  - `Cr[number]`: Le chrome. Concentration de chrome  - `Cr-III[number]`: Chrome III. Concentration de chrome à l'état d'oxydation +3  - `Cr-VI[number]`: Chrome VI. Concentration de chrome à l'état d'oxydation +6  - `Cu[number]`: Cuivre. Concentration de cuivre  - `Fe[number]`: Le fer. Concentration en fer  - `Hg[number]`: Le mercure. Concentration de mercure  - `N-TOT[number]`: Azote total. L'azote total (AT) est la somme de l'azote nitrique (NO3-N), de l'azote nitrique (NO2-N), de l'azote ammoniacal (NH3-N) et de l'azote lié aux composés organiques.  - `NH3[number]`: Concentration d'ammoniac  - `NH4[number]`: Concentration d'ammonium  - `NO2[number]`: Azote nitrique. Concentration d'un échantillon en azote nitrique  - `NO3[number]`: Concentration de nitrates  - `Ni[number]`: Nickel. Concentration de nickel  - `O2[number]`: Niveau d'oxygène libre et non composé présent  - `P-PO4[number]`: Phosphate-phosphore. Concentration de phosphore sous forme de phosphate  - `P-TOT[number]`: Phosphore total. Le phosphore total est une mesure de toutes les formes de phosphore dans l'eau, y compris le phosphore dissous et particulaire, organique et inorganique.  - `PC[number]`: Concentration du pigment phycocyanine qui peut être mesurée pour estimer les concentrations de cyanobactéries de manière spécifique.  - `PE[number]`: Concentration du pigment phycoérythrine qui peut être mesurée pour estimer spécifiquement les concentrations de cyanobactéries  - `PO4[number]`: Concentration de phosphates  - `Pb[number]`: Plomb. Concentration de plomb  - `Se[number]`: Sélénium. Concentration de sélénium  - `Sn[number]`: L'étain. Concentration d'étain  - `THC[number]`: Hydrocarbures totaux. Concentration d'hydrocarbures totaux  - `TKN[number]`: Azote Kjeldahl total. Mesure qui détermine à la fois les formes organiques et inorganiques de l'azote.  - `TO[number]`: Teneur en huile totale. Concentration de l'huile  - `Zn[number]`: Le zinc. Concentration de zinc  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alkalinity[number]`: L'alcalinité de l'eau est sa capacité de neutralisation des acides, qui correspond à la somme de toutes les bases titrables.  - `alternateName[string]`: Un nom alternatif pour ce poste  - `anionic-surfactants[number]`: Concentration des agents de surface anioniques  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: La demande biochimique en oxygène (DBO) est la quantité d'oxygène dissous (OD) nécessaire (c'est-à-dire demandée) par les organismes biologiques aérobies pour décomposer la matière organique présente dans un échantillon d'eau donné, à une certaine température et sur une période de temps spécifique.  - `cationic-surfactants[number]`: Concentration d'agents de surface cationiques  - `cod[number]`: La demande chimique en oxygène (DCO) est une mesure indicative de la quantité d'oxygène qui peut être consommée par les réactions dans une solution mesurée  - `conductance[number]`: Conductance spécifique  - `conductivity[number]`: Conductivité électrique  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateObserved[string]`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant spécifique ou par un intervalle ISO8601.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Une description de l'article  - `enterococci[number]`: Concentration d'entérocoques  - `escherichiaColi[number]`: Concentration d'Escherichia coli  - `flow[number]`: Débit d'eau observé.  - `fluoride[number]`: Concentration de fluorure  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `measurand[array]`: Un tableau de chaînes contenant des détails (voir le format ci-dessous) sur les mesurandes supplémentaires fournis par cette observation.  - `name[string]`: Le nom de cet élément  - `non-ionic-surfactants[number]`: Concentration d'agents de surface non ioniques  - `orp[number]`: Potentiel d'oxydation-réduction  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pH[number]`: Acidité ou basicité d'une solution aqueuse  - `refPointOfInterest[*]`: Une référence à un point d'intérêt associé à cette observation  - `salinity[number]`: Quantité de sels dissous dans l'eau  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `sulphate[number]`: Concentration de sulfate  - `sulphite[number]`: Concentration de sulfite  - `tds[number]`: Total des solides dissous.  - `temperature[number]`: Température  - `total-surfactants[number]`: Concentration des agents de surface totaux  - `tss[number]`: Total des solides en suspension  - `turbidity[number]`: Quantité de lumière diffusée par les particules de la colonne d'eau  - `type[string]`: Type d'entité NGSI. Il doit s'agir de WaterQualityObserved  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WaterQualityObserved:      
  description: 'Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section'      
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
      description: 'Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen'      
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
      description: 'Level of free, non-compound oxygen present'      
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
      description: 'Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic'      
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
        type: string      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityObserved/schema.json      
  x-model-tags: 'NAIADES, DigitalWater.city, B-WaterSmart'      
  x-version: 0.0.5      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### WaterQualityObserved Valeurs clés de l'INSIG-v2 Exemple    
Voici un exemple de WaterQualityObserved au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
  "Zn": 0.0  
}  
```  
</details>    
#### WaterQualityObserved NGSI-v2 normalisé Exemple    
Voici un exemple de WaterQualityObserved au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
  }  
}  
```  
</details>    
#### WaterQualityObserved Valeurs clés de l'INS-LD Exemple    
Voici un exemple de WaterQualityObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WaterQualityObserved NGSI-LD normalisé Exemple    
Voici un exemple de WaterQualityObserved au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
   "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
