[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ水質観測  
==========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**水質データモデルは、ある水塊（河川、湖沼、海など）の水質パラメータを表現するためのものである。  
バージョン: 0.0.4  

## プロパティ一覧  

- `Chla`: クロロフィルAの濃度。  - `Cl-`: 塩化物の濃度  - `NH3`: アンモニアの濃度  - `NH4`: アンモニウムの濃度  - `NO3`: 硝酸塩の濃度  - `O2`: 遊離した非複合酸素の存在レベル。  - `PC`: 藍藻の濃度を具体的に推定するために測定することができる色素フィコシアニンの濃度。  - `PE`: 藍藻の濃度を具体的に推定するために測定することができる色素フィコエリトリン濃度。  - `PO4`: リン酸塩の濃度  - `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `bod`: 生物化学的酸素要求量（BOD）とは、ある温度で一定時間、ある水試料中の有機物を分解するために好気性生物によって必要とされる（すなわち要求される）溶存酸素の量のことである  - `cod`: 化学的酸素要求量（COD）は、測定された溶液中の反応によって消費されうる酸素の量を示す指標である  - `conductance`: 比誘電率。  - `conductivity`: 電気伝導度。  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved`: この観測の日付と時刻をISO8601 UTCフォーマットで表したもの。これは、特定の時間の瞬間、またはISO8601の間隔で表すことができます。  - `description`: このアイテムの説明  - `enterococci`: 腸球菌の濃度  - `escherichiaColi`: 大腸菌の濃度  - `id`: エンティティの一意な識別子  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `measurand`: この観測で得られた追加の測定値に関する詳細（以下の形式を参照）を含む文字列の配列。  - `name`: このアイテムの名称です。  - `orp`: 酸化還元電位。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `pH`: 水溶液の酸性度または塩基性度。  - `refPointOfInterest`: この観測に関連する注目点への参照。  - `salinity`: 水に溶けている塩の量。  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tds`: 総溶解固形分。  - `temperature`: 温度  - `tss`: 総浮遊物質量。  - `turbidity`: 水柱中の粒子によって散乱される光の量  - `type`: NGSI Entity タイプ。これは WaterQualityObserved でなければならない。    
必要なプロパティ  
- `dateObserved`  - `id`  - `location`  - `type`  ## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: 'Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section'    
  properties:    
    Chla:    
      description: 'Concentration of chlorophyll A.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    Cl-:    
      description: 'Concentration of chlorides.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    NH3:    
      description: 'Concentration of ammonia.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    NH4:    
      description: 'Concentration of ammonium.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    NO3:    
      description: 'Concentration of nitrates.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    O2:    
      description: 'Level of free, non-compound oxygen present.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    PC:    
      description: 'Concentration of pigment phycocyanin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    PE:    
      description: 'Concentration of pigment phycoerythrin which can be measured to estimate cyanobacteria concentrations specifically.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    PO4:    
      description: 'Concentration of phosphates.'    
      minimum: 0    
      type: number    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bod:    
      description: 'Biochemical oxygen demand (BOD) is the amount of dissolved oxygen (DO) needed (i.e. demanded) by aerobic biological organisms to break down organic material present in a given water sample at certain temperature over a specific time period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    cod:    
      description: 'Chemical oxygen demand (COD) is an indicative measure of the amount of oxygen that can be consumed by reactions in a measured solution'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: mg/l    
    conductance:    
      description: 'Specific Conductance.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    conductivity:    
      description: 'Electrical Conductivity.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    enterococci:    
      description: 'Concentration of Enterococci'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'Total number of bacteria/100mL'    
    escherichiaColi:    
      description: 'Concentration of Escherichia coli'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'Total number of bacteria/100mL'    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    measurand:    
      description: 'An array of strings containing details (see format below) about extra measurands provided by this observation.'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    orp:    
      description: 'Oxidation-Reduction potential.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterqualityobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pH:    
      description: 'Acidity or basicity of an aqueous solution.'    
      maximum: 14    
      minimum: 0    
      type: number    
      x-ngsi:    
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
      x-ngsi:    
        type: Relationship    
    salinity:    
      description: 'Amount of salts dissolved in water.'    
      minimum: 0    
      type: number    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
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
    tss:    
      description: 'Total suspended solids.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    turbidity:    
      description: 'Amount of light scattered by particles in the water column'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WaterQualityObserved'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.4    
```  
</details>    
## ペイロードの例  
#### WaterQualityObserved NGSI-v2 key-value の例。  
WaterQualityObservedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### WaterQualityObserved NGSI-v2 正規化例  
WaterQualityObservedをJSON-LD形式で正規化した例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### WaterQualityObserved NGSI-LD key-value 例  
WaterQualityObservedをJSON-LD形式でkey-valuesとした例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
    ]  
}  
```  
#### 水質観測 NGSI-LD 正規化例  
WaterQualityObservedをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
