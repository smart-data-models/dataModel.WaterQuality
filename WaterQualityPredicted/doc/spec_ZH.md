<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：水质预测  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityPredicted/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**水质预测数据模型旨在表示某一水体（河流、湖泊、海洋等）断面的水质预测**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `datePredicted[string]`: 以 ISO8601 UTC 格式表示的预测有效日期和时间。它可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `expiryDate[string]`: 以 ISO8601 UTC 格式表示的预测不再有效的日期和时间。它可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一标识  - `predictions[object]`: 水质预测清单  	- `value`:     
- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 WaterQualityPredicted  - `waterQualityPredictionValue[string]`: 描述水质预测摘要  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  - `waterQualityPredictionValue`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityPredicted:    
  description: Water Quality Predicted data model is intended to represent predictions of water quality at a certain water mass (river,  lake, sea, etc.) section    
  properties:    
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
    datePredicted:    
      description: The date and time from which the prediction is valid in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval    
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
      description: The date and time for when the prediction is not valid anymore in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    predictions:    
      description: List of predictions for water quality    
      properties:    
        value:    
          description: Each one of the predictions for water quality    
          items:    
            description: Object describing the predictions for water quality    
            properties:    
              percentile:    
                description: Percentile of the predictions for water quality    
                type: string    
                x-ngsi:    
                  type: Property    
              prediction:    
                description: Actual value of the prediction for water quality    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
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
    type:    
      description: NGSI Entity type. It has to be WaterQualityPredicted    
      enum:    
        - WaterQualityPredicted    
      type: string    
      x-ngsi:    
        type: Property    
    waterQualityPredictionValue:    
      description: Describes a summary of the water quality prediction    
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
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityPredicted/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityPredicted/schema.json    
  x-model-tags: NAIADES    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 水质预测 NGSI-v2 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterQualityPredicted 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### 水质预测值 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的水质预测示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### 水质预测 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterQualityPredicted 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 水质预测值 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的水质预测示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
