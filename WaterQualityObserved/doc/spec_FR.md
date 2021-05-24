Entité : WaterQualityObserved  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données sur la qualité de l'eau est destiné à représenter les paramètres de la qualité de l'eau dans une certaine section de la masse d'eau (rivière, lac, mer, etc.)**.  

## Liste des propriétés  

- `Chla`: Concentration de la chlorophylle A.  - `Cl-`: Concentration de chlorures.  - `NH3`: Concentration d'ammoniac.  - `NH4`: Concentration d'ammonium.  - `NO3`: Concentration de nitrates.  - `O2`: Niveau d'oxygène libre, non composé, présent.  - `PC`: Concentration du pigment phycocyanine qui peut être mesurée pour estimer spécifiquement les concentrations de cyanobactéries.  - `PE`: Concentration du pigment phycoérythrine qui peut être mesurée pour estimer spécifiquement les concentrations de cyanobactéries.  - `PO4`: Concentration de phosphates.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `bod`: La demande biochimique en oxygène (DBO) est la quantité d'oxygène dissous (DO) nécessaire (c'est-à-dire demandée) par les organismes biologiques aérobies pour décomposer la matière organique présente dans un échantillon d'eau donné, à une certaine température et pendant une période spécifique.  - `cod`: La demande chimique en oxygène (DCO) est une mesure indicative de la quantité d'oxygène qui peut être consommée par les réactions dans une solution mesurée.  - `conductance`: Conductance spécifique.  - `conductivity`: Conductivité électrique.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `measurand`: Un tableau de chaînes de caractères contenant des détails (voir le format ci-dessous) sur les mesurandes supplémentaires fournis par cette observation.  - `name`: Le nom de cet élément.  - `orp`: Potentiel d'oxydation-réduction.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pH`: Acidité ou basicité d'une solution aqueuse.  - `refPointOfInterest`: Une référence à un point d'intérêt associé à cette observation.  - `salinity`: Quantité de sels dissous dans l'eau.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tds`: Solides dissous totaux.  - `temperature`: Température  - `tss`: Total des solides en suspension.  - `turbidity`: Quantité de lumière diffusée par les particules dans la colonne d'eau  - `type`: Type d'entité NGSI. Il doit s'agir de WaterQualityObserved.    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: 'Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section'    
  properties:    
    Chla:    
      description: 'Concentration of chlorophyll A.'    
      minimum: 0    
      type: Property    
    Cl-:    
      description: 'Concentration of chlorides.'    
      minimum: 0    
      type: Property    
    NH3:    
      description: 'Concentration of ammonia.'    
      minimum: 0    
      type: Property    
    NH4:    
      description: 'Concentration of ammonium.'    
      minimum: 0    
      type: Property    
    NO3:    
      description: 'Concentration of nitrates.'    
      minimum: 0    
      type: Property    
    O2:    
      description: 'Level of free, non-compound oxygen present.'    
      minimum: 0    
      type: Property    
    PC:    
      description: 'Concentration of pigment phycocyanin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: Property    
    PE:    
      description: 'Concentration of pigment phycoerythrin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: Property    
    PO4:    
      description: 'Concentration of phosphates.'    
      minimum: 0    
      type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    bod:    
      description: 'Biochemical oxygen demand (BOD) is the amount of dissolved oxygen (DO) needed (i.e. demanded) by aerobic biological organisms to break down organic material present in a given water sample at certain temperature over a specific time period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: mg/l    
    cod:    
      description: 'Chemical oxygen demand (COD) is an indicative measure of the amount of oxygen that can be consumed by reactions in a measured solution'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: mg/l    
    conductance:    
      description: 'Specific Conductance.'    
      minimum: 0    
      type: Property    
    conductivity:    
      description: 'Electrical Conductivity.'    
      minimum: 0    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
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
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    measurand:    
      description: 'An array of strings containing details (see format below) about extra measurands provided by this observation.'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    orp:    
      description: 'Oxidation-Reduction potential.'    
      minimum: 0    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pH:    
      description: 'Acidity or basicity of an aqueous solution.'    
      maximum: 14    
      minimum: 0    
      type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to a point of interest associated to this observation.'    
      type: Relationship    
    salinity:    
      description: 'Amount of salts dissolved in water.'    
      minimum: 0    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    tds:    
      description: 'Total dissolved solids. '    
      minimum: 0    
      type: Property    
    temperature:    
      description: Temperature    
      type: Property    
    tss:    
      description: 'Total suspended solids.'    
      minimum: 0    
      type: Property    
    turbidity:    
      description: 'Amount of light scattered by particles in the water column'    
      minimum: 0    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WaterQualityObserved'    
      enum:    
        - WaterQualityObserved    
      type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Valeurs clés de la NGSI-v2 WaterQualityObserved Exemple  
Voici un exemple d'une WaterQualityObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec la NGSI-v2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "measurand": ["NO3, 0.01, M1, Concentration of Nitrates"],  
  "location": {  
    "type": "Point",  
    "coordinates": [-5.993307, 37.362882]  
  },  
  "temperature": 24.4,  
  "conductivity": 0.005,  
  "pH": 7.4,  
  "NO3": 0.01  
}  
```  
#### WaterQualityObserved NGSI-v2 normalisé Exemple  
Voici un exemple d'un WaterQualityObserved au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2017-01-31T06:45:00Z"  
  },  
  "temperature": {  
    "value": 24.4  
  },  
  "NO3": {  
    "value": 0.01  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-5.993307, 37.362882]  
    }  
  },  
  "pH": {  
    "value": 7.4  
  },  
  "measurand": {  
    "value": ["NO3, 0.01, M1, Concentration of Nitrates"]  
  },  
  "conductivity": {  
    "value": 0.005  
  }  
}  
```  
#### Qualité de l'eau observée Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une WaterQualityObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "NO3": 0.01,  
  "conductivity": 0.005,  
  "dateObserved": "2017-01-31T06:45:00Z",  
  "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
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
  "type": "WaterQualityObserved"  
}  
```  
#### Qualité de l'eau observée NGSI-LD normalisée Exemple  
Voici un exemple d'un WaterQualityObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1",  
  "type": "WaterQualityObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-01-31T06:45:00Z"  
    }  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 24.4  
  },  
  "NO3": {  
    "type": "Property",  
    "value": 0.01  
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
  "pH": {  
    "type": "Property",  
    "value": 7.4  
  },  
  "measurand": {  
    "type": "Property",  
    "value": [  
      "NO3, 0.01, M1, Concentration of Nitrates"  
    ]  
  },  
  "conductivity": {  
    "type": "Property",  
    "value": 0.005  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
