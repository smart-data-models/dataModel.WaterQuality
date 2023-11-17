<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: WaterQualityObserved    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **수질 데이터 모델은 특정 수역(강, 호수, 바다 등) 구간에서 수질 매개변수를 표현하기 위한 모델**입니다.    
버전: 0.0.5    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `Al[number]`: 알루미늄. 알루미늄 농도  - `As[number]`: 비소. 비소 농도  - `B[number]`: 붕소. 붕소 농도  - `Ba[number]`: 바륨. 바륨 농도  - `Cd[number]`: 카드뮴. 카드뮴 농도  - `Chla[number]`: 엽록소 A의 농도  - `Cl-[number]`: 염화물 농도  - `Cr[number]`: 크롬. 크롬 농도  - `Cr-III[number]`: 크롬 III. 산화 상태에서의 크롬 농도 +3  - `Cr-VI[number]`: 크롬 VI. 산화 상태에서의 크롬 농도 +6  - `Cu[number]`: 구리. 구리 농도  - `Fe[number]`: 철분. 철분 농도  - `Hg[number]`: 수은. 수은 농도  - `N-TOT[number]`: 총 질소. 총 질소(TN)는 질산염 질소(NO3-N), 아질산염 질소(NO2-N), 암모니아 질소(NH3-N) 및 유기적으로 결합된 질소의 합입니다.  - `NH3[number]`: 암모니아 농도  - `NH4[number]`: 암모늄 농도  - `NO2[number]`: 아질산성 질소. 아질산성 질소 시료의 농도  - `NO3[number]`: 질산염 농도  - `Ni[number]`: 니켈. 니켈 농도  - `O2[number]`: 화합물이 아닌 유리 산소의 존재 수준  - `P-PO4[number]`: 인산염-인. 인산염으로서의 인의 농도  - `P-TOT[number]`: 총 인. 총 인은 용존 인과 미립자 인, 유기 인과 무기 인을 포함하여 물 속의 모든 형태의 인을 측정한 것입니다.  - `PC[number]`: 시아노박테리아 농도를 구체적으로 추정하기 위해 측정할 수 있는 색소 피코시아닌의 농도입니다.  - `PE[number]`: 시아노박테리아 농도를 구체적으로 추정하기 위해 측정할 수 있는 색소 피코에리트린의 농도  - `PO4[number]`: 인산염 농도  - `Pb[number]`: 납. 납 농도  - `Se[number]`: 셀레늄. 셀레늄 농도  - `Sn[number]`: 주석. 주석의 농도  - `THC[number]`: 총 탄화수소. 총 탄화수소 농도  - `TKN[number]`: 총 킬달 질소. 질소의 유기 및 무기 형태를 모두 결정하는 측정값입니다.  - `TO[number]`: 총 오일 함량. 오일 농도  - `Zn[number]`: 아연. 아연 농도  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alkalinity[number]`: 물의 알칼리도는 적정 가능한 모든 염기의 총합으로 구성된 산 중화 능력입니다.  - `alternateName[string]`: 이 항목의 대체 이름  - `anionic-surfactants[number]`: 음이온 계면활성제의 농도  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 생화학적 산소 요구량(BOD)은 특정 기간 동안 특정 온도에서 특정 수질 샘플에 존재하는 유기 물질을 분해하기 위해 호기성 생물체가 필요로 하는(즉, 요구되는) 용존 산소(DO)의 양입니다.  - `cationic-surfactants[number]`: 양이온성 계면활성제의 농도  - `cod[number]`: 화학적 산소 요구량(COD)은 측정된 용액에서 반응에 의해 소비될 수 있는 산소의 양을 나타내는 지표입니다.  - `conductance[number]`: 특정 컨덕턴스  - `conductivity[number]`: 전기 전도성  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateObserved[string]`: ISO8601 UTC 형식의 관측 날짜 및 시간입니다. 특정 시간 순간 또는 ISO8601 간격으로 표시할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `enterococci[number]`: 장구균 농도  - `escherichiaColi[number]`: 대장균 농도  - `flow[number]`: 물 흐름이 관찰되었습니다.  - `fluoride[number]`: 불소 농도  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `measurand[array]`: 이 관측에서 제공하는 추가 측정값에 대한 세부 정보(아래 형식 참조)가 포함된 문자열 배열입니다.  - `name[string]`: 이 항목의 이름  - `non-ionic-surfactants[number]`: 비이온성 계면활성제의 농도  - `orp[number]`: 산화-환원 잠재력  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pH[number]`: 수용액의 산도 또는 염기성  - `refPointOfInterest[*]`: 이 관찰과 관련된 관심 지점에 대한 참조입니다.  - `salinity[number]`: 물에 용해된 염분의 양  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `sulphate[number]`: 황산염 농도  - `sulphite[number]`: 아황산염 농도  - `tds[number]`: 총 용존 고형물.  - `temperature[number]`: 온도  - `total-surfactants[number]`: 총 계면활성제 농도  - `tss[number]`: 총 부유 물질  - `turbidity[number]`: 물기둥의 입자에 의해 산란되는 빛의 양  - `type[string]`: NGSI 엔티티 유형. WaterQualityObserved여야 합니다.  <!-- /30-PropertiesList -->    
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
## 페이로드 예시    
#### WaterQualityObserved NGSI-v2 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 WaterQualityObserved의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### WaterQualityObserved NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WaterQualityObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### WaterQualityObserved NGSI-LD 키 값 예제    
다음은 키 값으로 JSON-LD 형식의 WaterQualityObserved의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### WaterQualityObserved NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WaterQualityObserved의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
