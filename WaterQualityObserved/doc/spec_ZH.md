<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：水质观测  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**水质数据模型用于表示某一水体（河流、湖泊、海洋等）断面的水质参数***。  
版本： 0.0.6  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `Al[number]`: 铝。铝的浓度  - `As[number]`: 砷。砷浓度  - `B[number]`: 硼。硼的浓度  - `Ba[number]`: 钡。钡的浓度  - `Cd[number]`: 镉。镉的浓度  - `Chla[number]`: 叶绿素 A 的浓度  - `Cl-[number]`: 氯化物浓度  - `Cr[number]`: 铬。铬的浓度  - `Cr-III[number]`: 铬 III。氧化态 +3 的铬浓度  - `Cr-VI[number]`: 铬 VI。氧化态 +6 的铬浓度  - `Cu[number]`: 铜。铜的浓度  - `Fe[number]`: 铁铁的浓度  - `Hg[number]`: 汞。汞浓度  - `N-TOT[number]`: 总氮。总氮 (TN) 是硝酸盐氮 (NO3-N)、亚硝酸盐氮 (NO2-N)、氨氮 (NH3-N) 和有机结合氮的总和。  - `NH3[number]`: 氨的浓度  - `NH4[number]`: 铵的浓度  - `NO2[number]`: 亚硝酸盐氮样品中亚硝酸盐氮的浓度  - `NO3[number]`: 硝酸盐浓度  - `Ni[number]`: 镍镍的浓度  - `O2[number]`: 游离非复合氧的含量  - `P-PO4[number]`: 磷酸盐-磷。磷酸盐中磷的浓度  - `P-TOT[number]`: 总磷。总磷是对水中所有形式的磷的测量，包括溶解磷和颗粒磷、有机磷和无机磷。  - `PC[number]`: 色素藻蓝蛋白的浓度，可通过测量藻蓝蛋白来估算蓝藻的具体浓度  - `PE[number]`: 色素藻红素的浓度，可通过测量藻红素来具体估算蓝藻的浓度  - `PO4[number]`: 磷酸盐浓度  - `Pb[number]`: 铅。铅含量  - `Se[number]`: 硒。硒的浓度  - `Sn[number]`: 锡。锡的浓度  - `THC[number]`: 总碳氢化合物总碳氢化合物的浓度  - `TKN[number]`: 凯氏总氮（Total Kjeldahl Nitrogen）。确定氮的有机和无机形式的测量方法  - `TO[number]`: 总油含量。油的浓度  - `Zn[number]`: 锌锌浓度  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alkalinity[number]`: 水的碱度是指水的酸中和能力，由所有可滴定碱的总和组成  - `alternateName[string]`: 该项目的替代名称  - `anionic-surfactants[number]`: 阴离子表面活性剂的浓度  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bod[number]`: 生化需氧量 (BOD) 是指在一定温度下，好氧生物在特定时间段内分解特定水样中的有机物所需的溶解氧 (DO) 量（即需求量  - `cationic-surfactants[number]`: 阳离子表面活性剂的浓缩  - `cod[number]`: 化学需氧量（COD）是测量溶液中反应可消耗氧气量的指示性指标  - `componentAnalyzed[string]`: 样品中分析的成分符号  - `componentName[string]`: 样本中分析的成分全称  - `concentration[number]`: 样品中分析成分的浓度  - `conductance[number]`: 比电导  - `conductivity[number]`: 导电性  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[string]`: 以 ISO8601 UTC 格式表示的观测日期和时间。它可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `enterococci[number]`: 肠球菌浓度  - `escherichiaColi[number]`: 大肠杆菌浓度  - `flow[number]`: 观察到的水流。  - `fluoride[number]`: 氟浓度  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `measurand[array]`: 一个字符串数组，包含该观测值提供的额外测量值的详细信息（格式见下文）。  - `name[string]`: 该项目的名称  - `non-ionic-surfactants[number]`: 非离子表面活性剂的浓度  - `orp[number]`: 氧化还原电位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一标识  - `pH[number]`: 水溶液的酸碱性  - `refPointOfInterest[*]`: 与该观测点相关的兴趣点参考文献  - `salinity[number]`: 溶解在水中的盐量  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `sulphate[number]`: 硫酸盐浓度  - `sulphite[number]`: 亚硫酸盐浓度  - `tds[number]`: 总溶解固体。  - `temperature[number]`: 温度  - `total-surfactants[number]`: 总表面活性剂的浓度  - `tss[number]`: 总悬浮固体  - `turbidity[number]`: 水体中颗粒散射的光量  - `type[string]`: NGSI 实体类型。必须是 WaterQualityObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterQualityObserved:    
  description: Water Quality data model is intended to represent water quality parameters at a certain water mass (river,  lake, sea, etc.) section    
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
      description: Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen    
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
      description: Level of free, non-compound oxygen present    
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
      description: Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic    
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
    componentAnalyzed:    
      description: The component symbol analyzed in the sample    
      type: string    
      x-ngsi:    
        type: Property    
    componentName:    
      description: The component full name analyzed in the sample    
      type: string    
      x-ngsi:    
        type: Property    
    concentration:    
      description: The concentration of the component analyzed in the sample    
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
    measurand:    
      description: An array of strings containing details (see format below) about extra measurands provided by this observation    
      items:    
        description: Every element of the array of strings containing details (see format below) about extra measurands provided by this observation    
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
          type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
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
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterQuality/WaterQualityObserved/schema.json    
  x-model-tags: NAIADES, DigitalWater.city, B-WaterSmart, Waterverse    
  x-version: 0.0.6    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 水质观测 NGSI-v2 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterQualityObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
  "Zn": 0.0,  
  "componentAnalyzed": "Cl",  
  "componentName": "Chlorine",  
  "concentration": 20  
}  
```  
</details>  
#### 水质观测 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 WaterQualityObserved 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
  },  
  "componentAnalyzed": {  
    "type": "Text",  
    "value": "Cl"  
  },  
  "componentName": {  
    "type": "Text",  
    "value": "Chlorine"  
  },  
  "concentration": {  
    "type": "Number",  
    "value": 20  
  }  
}  
```  
</details>  
#### 水质观测 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 WaterQualityObserved 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
  "componentAnalyzed": "Cl",  
  "componentName": "Chlorine",  
  "concentration": 20,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterQuality/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 水质观测 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 WaterQualityObserved 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
  "componentAnalyzed": {  
    "type": "Property",  
    "value": "Cl"  
  },  
  "componentName": {  
    "type": "Property",  
    "value": "Chlorine"  
  },  
  "concentration": {  
    "type": "Property",  
    "value": 20  
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
