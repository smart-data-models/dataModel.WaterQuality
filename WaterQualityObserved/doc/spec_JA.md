<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ水質観測    
==========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**水質データモデルは、ある水塊（河川、湖沼、海など）の水質パラメータを表現するためのものである。    
バージョン: 0.0.5    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `Al[number]`: アルミニウムアルミニウムの濃度  - `As[number]`: ヒ素ヒ素の濃度  - `B[number]`: ホウ素ホウ素の濃度  - `Ba[number]`: バリウムバリウムの濃度  - `Cd[number]`: カドミウムカドミウムの濃度  - `Chla[number]`: クロロフィルA濃度  - `Cl-[number]`: 塩化物の濃度  - `Cr[number]`: クロムクロム濃度  - `Cr-III[number]`: クロムIII。酸化状態+3のクロム濃度。  - `Cr-VI[number]`: 六価クロム。酸化状態+6のクロム濃度。  - `Cu[number]`: 銅銅の濃度  - `Fe[number]`: 鉄鉄の濃度  - `Hg[number]`: 水銀水銀の濃度  - `N-TOT[number]`: 全窒素。全窒素（TN）は、硝酸性窒素（NO3-N）、亜硝酸性窒素（NO2-N）、アンモニア性窒素（NH3-N）、有機結合窒素の合計である。  - `NH3[number]`: アンモニア濃度  - `NH4[number]`: アンモニウムの濃度  - `NO2[number]`: 亜硝酸性窒素。試料の亜硝酸性窒素濃度  - `NO3[number]`: 硝酸塩濃度  - `Ni[number]`: ニッケルニッケル濃度  - `O2[number]`: 化合物でない遊離酸素の存在レベル  - `P-PO4[number]`: リン酸塩-リン。リン酸塩としてのリンの濃度  - `P-TOT[number]`: 全リン。全リンとは、溶存リン、粒子状リン、有機リン、無機リンを含む、水中のあらゆる形態のリンを測定したものである。  - `PC[number]`: シアノバクテリアの濃度を推定するために測定できる色素フィコシアニンの濃度。  - `PE[number]`: シアノバクテリアの濃度を推定するために測定できる色素フィコエリトリンの濃度  - `PO4[number]`: リン酸塩濃度  - `Pb[number]`: 鉛鉛の濃度  - `Se[number]`: セレンセレンの濃度  - `Sn[number]`: スズスズの濃度  - `THC[number]`: 全炭化水素総炭化水素の濃度  - `TKN[number]`: 全ケルダール窒素。有機態窒素と無機態窒素の両方を測定する指標。  - `TO[number]`: 全油分油の濃度  - `Zn[number]`: 亜鉛亜鉛の濃度  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alkalinity[number]`: 水のアルカリ度は、すべての滴定塩基の合計で構成される酸中和能である。  - `alternateName[string]`: この項目の別名  - `anionic-surfactants[number]`: 陰イオン界面活性剤の濃度  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 生物化学的酸素要求量（BOD）とは、ある水試料中に存在する有機物を、ある温度で、ある時間にわたって分解するために、好気性生物によって必要とされる（すなわち要求される）溶存酸素（DO）の量のことである。  - `cationic-surfactants[number]`: カチオン界面活性剤の濃縮  - `cod[number]`: 化学的酸素要求量（COD）は、測定された溶液中の反応によって消費される酸素の量を示す指標である。  - `conductance[number]`: 比コンダクタンス  - `conductivity[number]`: 電気伝導率  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ISO8601 UTCフォーマットによる観測日時。特定の時刻を表すことも、ISO8601のインターバルで表すこともできます。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: この商品の説明  - `enterococci[number]`: 腸球菌の濃度  - `escherichiaColi[number]`: 大腸菌濃度  - `flow[number]`: 水流が観測された。  - `fluoride[number]`: フッ化物濃度  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `measurand[array]`: このオブザベーションが提供する追加測定値に関する詳細(以下のフォーマットを参照)を含む文字列の配列。  - `name[string]`: このアイテムの名前  - `non-ionic-surfactants[number]`: 非イオン界面活性剤の濃度  - `orp[number]`: 酸化還元電位  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pH[number]`: 水溶液の酸性度または塩基性度  - `refPointOfInterest[*]`: この観測に関連する注目点への参照。  - `salinity[number]`: 水に溶けている塩の量  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `sulphate[number]`: 硫酸塩の濃度  - `sulphite[number]`: 亜硫酸塩の濃度  - `tds[number]`: 総溶解固形物。  - `temperature[number]`: 温度  - `total-surfactants[number]`: 全界面活性剤の濃度  - `tss[number]`: 総懸濁物質  - `turbidity[number]`: 水柱の粒子によって散乱される光の量  - `type[string]`: NGSI エンティティタイプ。これは WaterQualityObserved でなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### WaterQualityObserved NGSI-v2 キー値の例    
以下はWaterQualityObservedをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### 水質観測 NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の WaterQualityObserved の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
#### WaterQualityObserved NGSI-LD キー値の例    
以下はWaterQualityObservedをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### 水質観測 NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の WaterQualityObserved の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
