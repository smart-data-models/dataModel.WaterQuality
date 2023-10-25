<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 슬러지 품질 관찰됨  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/SludgeQualityObserved/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **슬러지 품질 데이터 모델은 슬러지 품질 매개변수를 나타내기 위한 것입니다.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `AOX[number]`: 흡착성 유기 결합 할로겐(AOX) 농도  - `As[number]`: 비소. 비소 농도  - `B[number]`: 붕소. 붕소 농도  - `Be[number]`: 베릴륨. 베릴륨 농도  - `C-ORG[number]`: 유기 탄소. 유기 탄소 농도  - `C10-C40[number]`: 탄화수소 C10-C40의 농도  - `Cd[number]`: 카드뮴. 카드뮴 농도  - `Cr[number]`: 크롬. 크롬 농도  - `Cr-VI[number]`: 크롬 VI. 산화 상태에서의 크롬 농도 +6  - `Cu[number]`: 구리. 구리 농도  - `DEHP[number]`: 디에틸헥실프탈레이트. DEHP 농도  - `Hg[number]`: 수은. 수은 농도  - `IPA[number]`: 이소프로필 알코올의 합계 이소프로필 알코올의 함량 합계  - `K-TOT[number]`: 총 칼륨. 칼륨의 총 함량  - `N-TOT[number]`: 총 질소. 총 질소(TN)는 질산염 질소(NO3-N), 아질산염 질소(NO2-N), 암모니아 질소(NH3-N) 및 유기적으로 결합된 질소의 합입니다.  - `Ni[number]`: 니켈. 니켈 농도  - `P-TOT[number]`: 총 인. 총 인은 용존 인과 미립자 인, 유기 인과 무기 인을 포함하여 물 속의 모든 형태의 인을 측정한 것입니다.  - `PCB[number]`: 폴리염화비페닐 폴리염화비페닐의 농도  - `Se[number]`: 셀레늄. 셀레늄 농도  - `Zn[number]`: 아연. 아연 농도  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateObserved[string]`: ISO8601 UTC 형식의 관측 날짜 및 시간입니다. 특정 시간 순간 또는 ISO8601 간격으로 표시할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `faecal-coliforms[number]`: 분변 대장균 농도(고형물 그램당 최대 가능 수)  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `measurand[array]`: 이 관측에서 제공하는 추가 측정값에 대한 세부 정보(아래 형식 참조)가 포함된 문자열 배열입니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pH[number]`: 수용액의 산도 또는 염기성  - `refPointOfInterest[*]`: 이 관찰과 관련된 관심 지점에 대한 참조입니다.  - `salmonella[number]`: 살모넬라균 농도(고형물 1g당 최대 가능 수)  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `toluene[number]`: 톨루엔 농도  - `type[string]`: NGSI 엔티티 유형. SludgeQualityObserved여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### SludgeQualityObserved NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 슬러지 품질 관찰의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SludgeQualityObserved NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SludgeQualityObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SludgeQualityObserved NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 슬러지 품질 관찰의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SludgeQualityObserved NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SludgeQualityObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
