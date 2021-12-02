Entidad: Calidad del aguaObservada  
==================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterQuality/blob/master/WaterQualityObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **El modelo de datos de calidad del agua está destinado a representar los parámetros de calidad del agua en una determinada masa de agua (río, lago, mar, etc.) sección**  

## Lista de propiedades  

- `Chla`: Concentración de clorofila A.  - `Cl-`: Concentración de cloruros.  - `NH3`: Concentración de amoníaco.  - `NH4`: Concentración de amonio.  - `NO3`: Concentración de nitratos.  - `O2`: Nivel de oxígeno libre no compuesto presente.  - `PC`: Concentración del pigmento ficocianina que puede medirse para estimar específicamente las concentraciones de cianobacterias.  - `PE`: Concentración del pigmento ficoeritrina que puede medirse para estimar específicamente las concentraciones de cianobacterias.  - `PO4`: Concentración de fosfatos.  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `bod`: La demanda bioquímica de oxígeno (DBO) es la cantidad de oxígeno disuelto (OD) que necesitan (es decir, que demandan) los organismos biológicos aeróbicos para descomponer la materia orgánica presente en una muestra de agua determinada a cierta temperatura durante un periodo de tiempo específico  - `cod`: La demanda química de oxígeno (DQO) es una medida indicativa de la cantidad de oxígeno que pueden consumir las reacciones en una solución medida  - `conductance`: Conductancia específica.  - `conductivity`: Conductividad eléctrica.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: La fecha y la hora de esta observación en formato ISO8601 UTC. Puede ser representada por un instante de tiempo específico o por un intervalo ISO8601.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `measurand`: Una matriz de cadenas que contiene detalles (véase el formato más abajo) sobre los medidores adicionales proporcionados por esta observación.  - `name`: El nombre de este artículo.  - `orp`: Potencial de Oxidación-Reducción.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pH`: Acidez o basicidad de una solución acuosa.  - `refPointOfInterest`: Una referencia a un punto de interés asociado a esta observación.  - `salinity`: Cantidad de sales disueltas en el agua.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tds`: Sólidos disueltos totales.  - `temperature`: Temperatura  - `tss`: Sólidos suspendidos totales.  - `turbidity`: Cantidad de luz dispersada por las partículas de la columna de agua  - `type`: Tipo de entidad NGSI. Debe ser WaterQualityObserved    
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      type: Geoproperty    
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
## Ejemplo de carga útil  
#### WaterQualityObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de WaterQualityObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### WaterQualityObserved NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de WaterQualityObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### WaterQualityObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de WaterQualityObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### WaterQualityObserved NGSI-LD normalizado Ejemplo  
Este es un ejemplo de WaterQualityObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud