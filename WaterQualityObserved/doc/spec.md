<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: WaterQualityObserved  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section**  
version: 0.0.5  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `Al[number]`: Aluminium. Concentration of aluminium  - `As[number]`: Arsenic. Concentration of arsenic  - `B[number]`: Boron. Concentration of boron  - `Ba[number]`: Barium. Concentration of barium  - `Cd[number]`: Cadmium. Concentration of cadmium  - `Chla[number]`: Concentration of chlorophyll A  - `Cl-[number]`: Concentration of chlorides  - `Cr[number]`: Chromium. Concentration of chromium  - `Cr-III[number]`: Chromium III. Concentration of chromium at the oxidation state +3  - `Cr-VI[number]`: Chromium VI. Concentration of chromium at the oxidation state +6  - `Cu[number]`: Copper. Concentration of copper  - `Fe[number]`: Iron. Concentration of iron  - `Hg[number]`: Mercury. Concentration of mercury  - `N-TOT[number]`: Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen  - `NH3[number]`: Concentration of ammonia  - `NH4[number]`: Concentration of ammonium  - `NO2[number]`: Nitrite nitrogen. Concentration of a sample in nitrite nitrogen  - `NO3[number]`: Concentration of nitrates  - `Ni[number]`: Nickel. Concentration of Nickel  - `O2[number]`: Level of free, non-compound oxygen present  - `P-PO4[number]`: Phosphate-phosphorus. Concentration of phosphorus as phosphate  - `P-TOT[number]`: Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic  - `PC[number]`: Concentration of pigment phycocyanin which can be measured to estimate cyanobacteria concentrations specifically  - `PE[number]`: Concentration of pigment phycoerythrin which can be measured to estimate cyanobacteria concentrations specifically  - `PO4[number]`: Concentration of phosphates  - `Pb[number]`: Lead. Concentration of lead  - `Se[number]`: Selenium. Concentration of selenium  - `Sn[number]`: Tin. Concentration of tin  - `THC[number]`: Total hydrocarbon. Concentration of total hydrocarbon  - `TKN[number]`: Total Kjeldahl Nitrogen. A measure that determines both the organic and the inorganic forms of nitrogen  - `TO[number]`: Total oil content. Concentration of oil  - `Zn[number]`: Zinc. Concentration of zinc  - `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alkalinity[number]`: The alkalinity of water is its acid-neutralizing capacity comprised of the total of all titratable bases  - `alternateName[string]`: An alternative name for this item  - `anionic-surfactants[number]`: Concentration of anionic surfactants  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: Biochemical oxygen demand (BOD) is the amount of dissolved oxygen (DO) needed (i.e. demanded) by aerobic biological organisms to break down organic material present in a given water sample at certain temperature over a specific time period  - `cationic-surfactants[number]`: Concentrtation of cationic surfactants  - `cod[number]`: Chemical oxygen demand (COD) is an indicative measure of the amount of oxygen that can be consumed by reactions in a measured solution  - `conductance[number]`: Specific Conductance  - `conductivity[number]`: Electrical Conductivity  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateObserved[string]`: The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: A description of this item  - `enterococci[number]`: Concentration of Enterococci  - `escherichiaColi[number]`: Concentration of Escherichia coli  - `flow[number]`: Water Flow observed.   - `fluoride[number]`: Concentration of fluoride  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `measurand[array]`: An array of strings containing details (see format below) about extra measurands provided by this observation  - `name[string]`: The name of this item  - `non-ionic-surfactants[number]`: Concentration of non-ionic surfactants  - `orp[number]`: Oxidation-Reduction potential  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pH[number]`: Acidity or basicity of an aqueous solution  - `refPointOfInterest[*]`: A reference to a point of interest associated to this observation  - `salinity[number]`: Amount of salts dissolved in water  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `sulphate[number]`: Concentration of sulfate  - `sulphite[number]`: Concentration of sulfite  - `tds[number]`: Total dissolved solids.   - `temperature[number]`: Temperature  - `total-surfactants[number]`: Concentration of total surfactants  - `tss[number]`: Total suspended solids  - `turbidity[number]`: Amount of light scattered by particles in the water column  - `type[string]`: NGSI Entity type. It has to be WaterQualityObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### WaterQualityObserved NGSI-v2 key-values Example    
Here is an example of a WaterQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "waterqualityobserved:Sevilla:D1",  
    "type": "WaterQualityObserved",  
    "dateObserved": "2017-01-31T06:45:00Z",  
    "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
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
#### WaterQualityObserved NGSI-v2 normalized Example    
Here is an example of a WaterQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
    "type": "array",  
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
    "type": "Number",  
    "value": 1.0  
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
    "type": "Number",  
    "value": 0.0  
  },  
  "B": {  
    "type": "Number",  
    "value": 0.2  
  },  
  "Ba": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Cd": {  
    "type": "Number",  
    "value": 0.001  
  },  
  "Cr": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Cr-III": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Cr-VI": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Cu": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Fe": {  
    "type": "Number",  
    "value": 7.4  
  },  
  "fluoride": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Hg": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "THC": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Ni": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "TO": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "Pb": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Se": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "Sn": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "sulphate": {  
    "type": "Number",  
    "value": 143.3  
  },  
  "sulphite": {  
    "type": "Number",  
    "value": 0.0  
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
    "type": "Number",  
    "value": 0.0  
  }  
}  
```  
</details>  
#### WaterQualityObserved NGSI-LD key-values Example    
Here is an example of a WaterQualityObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### WaterQualityObserved NGSI-LD normalized Example    
Here is an example of a WaterQualityObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
