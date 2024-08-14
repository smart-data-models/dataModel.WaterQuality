from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    SludgeQualityObserved = 'SludgeQualityObserved'


class SludgeQualityObserved(BaseModel):
    AOX: Optional[confloat(ge=0.0)] = Field(
        None, description='Concentration of Adsorbable Organically bound halogens (AOX)'
    )
    As: Optional[confloat(ge=0.0)] = Field(
        None, description='Arsenic. Concentration of arsenic'
    )
    B: Optional[confloat(ge=0.0)] = Field(
        None, description='Boron. Concentration of boron'
    )
    Be: Optional[confloat(ge=0.0)] = Field(
        None, description='Beryllium. Concentration of Beryllium'
    )
    C_ORG: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        alias='C-ORG',
        description='Organic Carbon. Concentration of organic carbon',
    )
    C10_C40: Optional[confloat(ge=0.0)] = Field(
        None, alias='C10-C40', description='Concentration of Hydrocarbons C10-C40'
    )
    Cd: Optional[confloat(ge=0.0)] = Field(
        None, description='Cadmium. Concentration of cadmium'
    )
    Cr: Optional[confloat(ge=0.0)] = Field(
        None, description='Chromium. Concentration of chromium'
    )
    Cr_VI: Optional[confloat(ge=0.0)] = Field(
        None,
        alias='Cr-VI',
        description='Chromium VI. Concentration of chromium at the oxidation state +6',
    )
    Cu: Optional[confloat(ge=0.0)] = Field(
        None, description='Copper. Concentration of copper'
    )
    DEHP: Optional[confloat(ge=0.0)] = Field(
        None, description='Diethylhexyl phthalate. Concentration of DEHP'
    )
    Hg: Optional[confloat(ge=0.0)] = Field(
        None, description='Mercury. Concentration of mercury'
    )
    IPA: Optional[confloat(ge=0.0)] = Field(
        None, description='Sum of isopropyl alcohol Sum of content of isopropyl alcohol'
    )
    K_TOT: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, alias='K-TOT', description='Total potassium. Total content of potassium'
    )
    N_TOT: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        alias='N-TOT',
        description='Total Nitrogen. Total Nitrogen (TN) is the sum of nitrate-nitrogen (NO3-N), nitrite-nitrogen (NO2-N), ammonia-nitrogen (NH3-N) and organically bonded nitrogen',
    )
    Ni: Optional[confloat(ge=0.0)] = Field(
        None, description='Nickel. Concentration of Nickel'
    )
    P_TOT: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        alias='P-TOT',
        description='Total Phosphorus. Total phosphorus is a measure of all forms of phosphorus in the water, including dissolved and particulate, organic and inorganic',
    )
    PCB: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Polychlorinated biphenyls Concentration of polychlorinated biphenyls',
    )
    Se: Optional[confloat(ge=0.0)] = Field(
        None, description='Selenium. Concentration of selenium'
    )
    Zn: Optional[confloat(ge=0.0)] = Field(
        None, description='Zinc. Concentration of zinc'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[str] = Field(
        None,
        description='The date and time of this observation in ISO8601 UTCformat. It can be represented by an specific time instant or by an ISO8601 interval',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    faecal_coliforms: Optional[confloat(ge=0.0)] = Field(
        None,
        alias='faecal-coliforms',
        description='Concentration of fecal coliforms (Most Probable Number per gram solids)',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    measurand: Optional[List[str]] = Field(
        None,
        description='An array of strings containing details (see format below) about extra measurands provided by this observation',
        min_length=1,
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    pH: Optional[confloat(ge=0.0, le=14.0)] = Field(
        None, description='Acidity or basicity of an aqueous solution'
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='A reference to a point of interest associated to this observation',
    )
    salmonella: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Concentration of Salmonella (Most Probable Number per gram solids)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    toluene: Optional[confloat(ge=0.0)] = Field(
        None, description='Concentration of Toluene'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be SludgeQualityObserved'
    )
