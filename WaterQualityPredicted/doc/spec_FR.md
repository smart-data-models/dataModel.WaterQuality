<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WaterQualityPredicted  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityPredicted/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le modèle de données prédites de la qualité de l'eau est destiné à représenter les prédictions de la qualité de l'eau à une certaine section de la masse d'eau (rivière, lac, mer, etc.)**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `datePredicted`: La date et l'heure à partir desquelles la prédiction est valable au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `description`: Une description de cet article  - `expiryDate`: La date et l'heure à laquelle la prédiction n'est plus valable dans le format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `predictions`:   - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit être WaterQualityPredicted.  - `waterQualityPredictionValue`: Décrit un résumé de la prédiction de la qualité de l'eau.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  - `waterQualityPredictionValue`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityPredicted:    
  description: 'Water Quality Predicted data model is intended to represent predictions of water quality at a certain water mass (river,  lake, sea, etc.) section'    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    datePredicted:    
      description: The date and time from which the prediction is valid in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval.    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    expiryDate:    
      description: The date and time for when the prediction is not valid anymore in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval.    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    id:    
      anyOf: &waterqualitypredicted_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geoproperty. Geojson reference to the item. Point    
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
        - description: Geoproperty. Geojson reference to the item. LineString    
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
        - description: Geoproperty. Geojson reference to the item. Polygon    
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
        - description: Geoproperty. Geojson reference to the item. MultiPoint    
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
        - description: Geoproperty. Geojson reference to the item. MultiLineString    
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
        - description: Geoproperty. Geojson reference to the item. MultiLineString    
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
        type: Geoproperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *waterqualitypredicted_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    predictions:    
      properties:    
        value:    
          items:    
            properties:    
              percentile:    
                type: string    
              prediction:    
                type: number    
            type: object    
          type: array    
      type: object    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be WaterQualityPredicted    
      enum:    
        - WaterQualityPredicted    
      type: string    
      x-ngsi:    
        type: Property    
    waterQualityPredictionValue:    
      description: Describes a summary of the water quality prediction.    
      enum:    
        - Excellent    
        - Good    
        - Sufficient    
        - Poor    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - waterQualityPredictionValue    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityPredicted/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityPredicted/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Qualité de l'eauValeurs clés prévues par la NGSI-v2 Exemple  
Voici un exemple de WaterQualityPredicted au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "1024e64a-0283-472c-9b62-dbf77291503e",  
  "type": "WaterQualityPredicted",  
  "dateCreated": "2022-05-27T10:00:00Z",  
  "datePredicted": "2022-05-20T14:00:00",  
  "expiryDate": "2022-05-21T14:00:00",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.9159,  
      2.21228  
    ]  
  },  
  "predictions": {  
    "value": [  
      {  
        "percentile": "2.5",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "50",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "90",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "95",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "97.5",  
        "prediction": 0.3  
      }  
    ]  
  },  
  "waterQualityPredictionValue": "Excellent"  
}  
```  
#### Qualité de l'eau Prévue NGSI-v2 normalisée Exemple  
Voici un exemple de WaterQualityPredicted au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "1024e64a-0283-472c-9b62-dbf77291503e",  
  "type": "WaterQualityPredicted",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-05-27T10:00:00Z"  
  },  
  "datePredicted": {  
    "type": "DateTime",  
    "value": "2022-05-20T14:00:00"  
  },  
  "expiryDate": {  
    "type": "DateTime",  
    "value": "2022-05-21T14:00:00"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.9159,  
        2.21228  
      ]  
    }  
  },  
  "predictionValues": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "percentile": "2.5",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "50",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "90",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "95",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "97.5",  
        "prediction": 0.3  
      }  
    ]  
  },  
  "waterQualityPredictionValue": {  
    "type": "Text",  
    "value": "Excellent"  
  }  
}  
```  
#### Qualité de l'eauValeurs clés NGSI-LD prédites Exemple  
Voici un exemple de WaterQualityPredicted au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "1024e64a-0283-472c-9b62-dbf77291503e",  
  "type": "WaterQualityPredicted",  
  "dateCreated": "2022-05-27T10:00:00Z",  
  "datePredicted": "2022-05-20T14:00:00",  
  "expiryDate": "2022-05-21T14:00:00",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.9159,  
      2.21228  
    ]  
  },  
  "predictions": {  
    "value": [  
      {  
        "percentile": "2.5",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "50",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "90",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "95",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "97.5",  
        "prediction": 0.3  
      }  
    ]  
  },  
  "waterQualityPredictionValue": "Excellent",  
  cccccccc  
}  
```  
#### Qualité de l'eau Prévue NGSI-LD normalisée Exemple  
Voici un exemple de WaterQualityPredicted au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "1024e64a-0283-472c-9b62-dbf77291503e",  
  "type": "WaterQualityPredicted",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-05-27T10:00:00Z"  
    }  
  },  
  "datePredicted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-05-20T14:00:00"  
    }  
  },  
  "expiryDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-05-21T14:00:00"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.9159,  
        2.21228  
      ]  
    }  
  },  
  "predictionValues": {  
    "type": "Property",  
    "value": [  
      {  
        "percentile": "2.5",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "50",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "90",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "95",  
        "prediction": 0.3  
      },  
      {  
        "percentile": "97.5",  
        "prediction": 0.3  
      }  
    ]  
  },  
  "waterQualityPredictionValue": {  
    "type": "Property",  
    "value": "Excellent"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
  ]  
}  
```  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
