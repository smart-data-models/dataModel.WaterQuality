/* (Beta) Export of data model WaterQualityObserved of the subject dataModel.WaterQuality for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WaterQualityObserved_type AS ENUM ('WaterQualityObserved');
CREATE TABLE WaterQualityObserved (Al NUMERIC, As NUMERIC, B NUMERIC, Ba NUMERIC, Cd NUMERIC, Chla NUMERIC, Cl- NUMERIC, Cr NUMERIC, Cr-III NUMERIC, Cr-VI NUMERIC, Cu NUMERIC, Fe NUMERIC, Hg NUMERIC, N-TOT NUMERIC, NH3 NUMERIC, NH4 NUMERIC, NO2 NUMERIC, NO3 NUMERIC, Ni NUMERIC, O2 NUMERIC, P-PO4 NUMERIC, P-TOT NUMERIC, PC NUMERIC, PE NUMERIC, PO4 NUMERIC, Pb NUMERIC, Se NUMERIC, Sn NUMERIC, THC NUMERIC, TKN NUMERIC, TO NUMERIC, Zn NUMERIC, address JSON, alkalinity NUMERIC, alternateName TEXT, anionic-surfactants NUMERIC, areaServed TEXT, bod NUMERIC, cationic-surfactants NUMERIC, cod NUMERIC, conductance NUMERIC, conductivity NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, dateObserved TEXT, description TEXT, enterococci NUMERIC, escherichiaColi NUMERIC, flow NUMERIC, fluoride NUMERIC, measurand JSON, name TEXT, non-ionic-surfactants NUMERIC, orp NUMERIC, owner JSON, pH NUMERIC, salinity NUMERIC, source TEXT, sulphate NUMERIC, sulphite NUMERIC, tds NUMERIC, temperature NUMERIC, total-surfactants NUMERIC, tss NUMERIC, turbidity NUMERIC, type WaterQualityObserved_type);