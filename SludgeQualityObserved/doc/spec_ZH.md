<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：污泥质量观测  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/SludgeQualityObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**污泥质量数据模型旨在表示污泥质量参数。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `AOX[number]`: 可吸附有机结合卤素（AOX）的浓度  - `As[number]`: 砷。砷浓度  - `B[number]`: 硼。硼的浓度  - `Be[number]`: 铍。铍的浓度  - `C-ORG[number]`: 有机碳有机碳浓度  - `C10-C40[number]`: 碳氢化合物 C10-C40 的浓度  - `Cd[number]`: 镉。镉的浓度  - `Cr[number]`: 铬。铬的浓度  - `Cr-VI[number]`: 铬 VI。氧化态 +6 的铬浓度  - `Cu[number]`: 铜。铜的浓度  - `DEHP[number]`: 邻苯二甲酸二乙基己酯。DEHP 的浓度  - `Hg[number]`: 汞。汞浓度  - `IPA[number]`: 异丙醇含量之和 异丙醇含量之和  - `K-TOT[number]`: 总钾钾的总含量  - `N-TOT[number]`: 总氮。总氮 (TN) 是硝酸盐氮 (NO3-N)、亚硝酸盐氮 (NO2-N)、氨氮 (NH3-N) 和有机结合氮的总和。  - `Ni[number]`: 镍镍的浓度  - `P-TOT[number]`: 总磷。总磷是对水中所有形式的磷的测量，包括溶解磷和颗粒磷、有机磷和无机磷。  - `PCB[number]`: 多氯联苯 多氯联苯的浓度  - `Se[number]`: 硒。硒的浓度  - `Zn[number]`: 锌锌浓度  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[string]`: 以 ISO8601 UTC 格式表示的观测日期和时间。可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `faecal-coliforms[number]`: 粪大肠菌群浓度（每克固体的最大可能数量）  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `measurand[array]`: 一个字符串数组，包含该观测值提供的额外测量值的详细信息（格式见下文）。  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pH[number]`: 水溶液的酸碱性  - `refPointOfInterest[*]`: 与该观测点相关的兴趣点参考文献  - `salmonella[number]`: 沙门氏菌浓度（每克固体中的最大可能数量）  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `toluene[number]`: 甲苯浓度  - `type[string]`: NGSI 实体类型。必须是 SludgeQualityObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### 污泥质量观测 NGSI-v2 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 SludgeQualityObserved 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SludgeQualityObserved:001",  
    "type": "SludgeQualityObserved",  
    "dateObserved": "2023-07-02T10:30:00Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [45.51970, 12.19351]  
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
#### 污泥质量观测 NGSI-v2 归一化示例  
下面是一个以 JSON-LD 格式规范化的 SludgeQualityObserved 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
  }  
}  
```  
</details>  
#### 污泥质量观测 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 SludgeQualityObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SludgeQualityObserved:sludgequalityobserved:Venice:D1",  
    "type": "SludgeQualityObserved",  
    "dateObserved": "2023-07-02T10:30:00Z",  
    "location": {  
        "coordinates": [  
            45.51970,  
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
#### 污泥质量观测 NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的 SludgeQualityObserved 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
