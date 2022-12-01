<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ水質予測  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityPredicted/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**水質予測データモデルは、ある水塊（河川、湖沼、海など）の水質予測を表現するためのものです**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

- `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `datePredicted`: ISO8601 UTCフォーマットで予測値が有効となる日付と時刻。これは、特定の時間の瞬間かISO8601の間隔で表すことができる。  - `description`: このアイテムの説明  - `expiryDate`: ISO8601 UTCフォーマットで予測値が無効になる日付と時刻。これは特定の時間の瞬間かISO8601の間隔で表すことができる。  - `id`: エンティティの一意な識別子  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name`: このアイテムの名称です。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `predictions`:   - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity タイプ。これは WaterQualityPredicted でなければならない。  - `waterQualityPredictionValue`: 水質予測の概要を記述しています。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  - `waterQualityPredictionValue`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### WaterQualityPredicted NGSI-v2 key-value の例。  
WaterQualityPredictedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### 水質予測 NGSI-v2 正規化例  
WaterQualityPredictedをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WaterQualityPredicted NGSI-LD key-value 例  
WaterQualityPredictedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### 水質予測 NGSI-LD 正規化例  
WaterQualityPredictedをJSON-LD形式で正規化した例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
