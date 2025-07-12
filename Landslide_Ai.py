import pandas
from sklearn.model_selection import train_test_split

import sklearn.tree



data = pandas.read_csv(r'C:\Users\pries\OneDrive\Desktop\Games\PythonPrograms\Face\Flood Model\WA_Soils.csv')
flood_hazard_prediction = pandas.read_csv(r'C:\Users\pries\OneDrive\Desktop\Games\PythonPrograms\Face\Flood Model\ai_flood_predictions.csv')
data = data.sample(frac=1, random_state=13)

data = data[['SOIL_EROSION_POTNL', 'SOIL_FLOOD_HAZARD', 'SOIL_CONST_HAZARD', 'SOIL_SLP_MAX_PC', 'SOIL_PRECIP', 'SOIL_DRAIN_RATE','SOIL_LAYER_RESTR','SOIL_TXTR_MDFR','SOIL_ROOT_DPT','SOIL_ROCK_FRAG']]
data['SOIL_FLOOD_HAZARD'] = flood_hazard_prediction['SOIL_FLOOD_HAZARD']

data['SOIL_FLOOD_HAZARD'] = data['SOIL_FLOOD_HAZARD'].str.strip()
data['SOIL_EROSION_POTNL'] = data['SOIL_EROSION_POTNL'].str.strip()
data['SOIL_CONST_HAZARD'] = data['SOIL_CONST_HAZARD'].str.strip()
data['SOIL_PRECIP'] = data['SOIL_PRECIP'].str.strip()
data['SOIL_DRAIN_RATE'] = data['SOIL_DRAIN_RATE'].str.strip()
data['SOIL_LAYER_RESTR'] = data['SOIL_LAYER_RESTR'].str.strip()
data['SOIL_TXTR_MDFR'] = data['SOIL_TXTR_MDFR'].str.strip()
data['SOIL_ROOT_DPT'] = data['SOIL_ROOT_DPT'].str.strip()
data['SOIL_ROCK_FRAG'] = data['SOIL_ROCK_FRAG'].str.strip()


unique_precip = data['SOIL_PRECIP'].unique()
unique_soil_drain_rate = data['SOIL_DRAIN_RATE'].unique()
unique_soil_layer_restr = data['SOIL_LAYER_RESTR'].unique()
unique_soil_txtr_mdfr = data['SOIL_TXTR_MDFR'].unique()
unique_soil_root_dpt = data['SOIL_ROOT_DPT'].unique()
unique_rock_fragments = data['SOIL_ROCK_FRAG'].unique()

def get_first_number(s: str) -> int:
    if '>' in s:
        second_half = s.split('>')[1].strip()
        return int(second_half.split(' ')[0])
    return int(s.split('-')[0].strip())

def get_second_number(s: str) -> int:
    if '>' in s:
        second_half = s.split('>')[1].strip()
        return int(second_half.split(' ')[0])+40
    second_half = s.split('-')[1].strip()
    result = second_half.split(' ')[0].strip()
    return int(result)

def get_first_percentage(s: str) -> int:
    if '>' in s:
        second_half = s.split('>')[1].strip()
        return int(second_half.split(' ')[0])
    return int(s.split(' - ')[0].strip())

def get_second_percentage(s: str) -> int:
    if '>' in s:
        second_half = s.split('>')[1].strip()
        return int(second_half.split(' ')[0])+40
    second_half = s.split(' - ')[1].strip()
    result = second_half.split(' ')[0].strip()
    return int(result)

def remove_inches(s: str) -> int:
    return int(s.split(' ')[0])

remaped_soil_erosion_potnl = {'LOW':0,'MEDIUM':1,'HIGH':2}
remaped_soil_flood_hazard = {'SLIGHT': 0, 'MODERATE': 1, 'SEVERE': 2}
remaped_soil_const_hazard = {'SLIGHT': 0, 'MODERATE': 1, 'SEVERE': 2}

remap_precip_low = {name: get_first_number(name) for name in unique_precip if isinstance(name, str)}
remap_precip_high = {name: get_second_number(name) for name in unique_precip if isinstance(name, str)}

remap_soil_drain_rate = {value: float(idx) for idx, value in enumerate(unique_soil_drain_rate)}

remap_soil_layer_restr = {'RESTRICTION':1,'NO RESTRICT.':0}

remap_soil_root_dpt = {name: remove_inches(name) for name in unique_soil_root_dpt if isinstance(name, str)}

remap_rock_frag_high = {name: get_first_percentage(name) for name in unique_rock_fragments if isinstance(name, str)}
remap_rock_frag_low = {name: get_second_percentage(name) for name in unique_rock_fragments if isinstance(name, str)}

remap_texture = {
    'SILT LOAM': 'SILT LOAM',
    'V.COBBLY LOAM': 'LOAM',
    'STONY LOAM': 'LOAM',
    'F.SANDY.LOAM': 'SANDY LOAM',
    'CLAY LOAM': 'CLAY LOAM',
    'GRAVELLY LOAMY SAND': 'LOAMY SAND',
    'LOAM': 'LOAM',
    'GRAVELLY SILT LOAM': 'SILT LOAM',
    'SANDY LOAM': 'SANDY LOAM',
    'GRAVELLY LOAM': 'LOAM',
    'GRAVELLY SANDY LOAM': 'SANDY LOAM',
    'STONY SANDY LOAM': 'SANDY LOAM',
    'V.STONY SILT LOAM': 'SILT LOAM',
    'COBBLY LOAMY SAND': 'LOAMY SAND',
    'VARIABLE SAND': 'SAND',
    'V.STONY LOAM': 'LOAM',
    'LOAMY SAND': 'LOAMY SAND',
    'V.CINDERY LOAMY SAND': 'LOAMY SAND',
    'NO DATA': 'UNKNOWN',
    'VARIABLE VARIABLE': 'UNKNOWN',
    'SHALY LOAM': 'LOAM',
    'COBBLY LOAM': 'LOAM',
    'COBBLY SILT LOAM': 'SILT LOAM',
    'STONY SILT LOAM': 'SILT LOAM',
    'SLT.CLY.LOAM': 'CLAY LOAM',
    'LOAMY.FN.SND': 'LOAMY SAND',
    'XTR.GRAVELLY SANDY LOAM': 'SANDY LOAM',
    'GRAVELLY F.SANDY.LOAM': 'SANDY LOAM',
    'V.COBBLY SILT LOAM': 'SILT LOAM',
    'V.GRAVELLY SILT LOAM': 'SILT LOAM',
    'MUCK': 'ORGANIC',
    'VF.SNDY.LOAM': 'SANDY LOAM',
    'ROCKY SILT LOAM': 'SILT LOAM',
    'V.GRAVELLY LOAMY SAND': 'LOAMY SAND',
    'SILTY CLAY': 'CLAY',
    'XTR.STONY SILT LOAM': 'SILT LOAM',
    'V.GRAVELLY LOAM': 'LOAM',
    'XTR.STONY LOAM': 'LOAM',
    'PEAT': 'ORGANIC',
    'V.GRAVELLY SANDY LOAM': 'SANDY LOAM',
    'V.GRAVELLY LOAMY.FN.SND': 'LOAMY SAND',
    'XTR.STONY SANDY LOAM': 'SANDY LOAM',
    'SAND': 'SAND',
    'XTR.STONY CLAY LOAM': 'CLAY LOAM',
    'CINDERY SANDY LOAM': 'SANDY LOAM',
    'V.CINDERY SANDY LOAM': 'SANDY LOAM',
    'V.BOULDERY LOAM': 'LOAM',
    'V.STONY LOAMY SAND': 'LOAMY SAND',
    'V.COBBLY SANDY LOAM': 'SANDY LOAM',
    'STONY CLAY LOAM': 'CLAY LOAM',
    'V.STONY SANDY LOAM': 'SANDY LOAM',
    'SILT': 'SILT LOAM',
    'V.ROCKY SANDY LOAM': 'SANDY LOAM',
    'GRAVELLY CLAY LOAM': 'CLAY LOAM',
    'CINDERY LOAM': 'LOAM',
    'V.ROCKY LOAMY SAND': 'LOAMY SAND',
    'BOULDERY SANDY LOAM': 'SANDY LOAM',
    'VARIABLE LOAM': 'LOAM',
    'STONY F.SANDY.LOAM': 'SANDY LOAM',
    'MUCKY LOAM': 'ORGANIC',
    'XTR.GRAVELLY LOAMY SAND': 'LOAMY SAND',
    'MUCKY PEAT': 'ORGANIC',
    'OTHER MUCK': 'ORGANIC',
    'BOULDERY LOAM': 'LOAM',
    'CINDERY LOAMY SAND': 'LOAMY SAND',
    'XTR.COBBLY LOAM': 'LOAM',
    'COBBLY SANDY LOAM': 'SANDY LOAM',
    'MUCKY SILT LOAM': 'SILT LOAM',
    'GRAVELLY CRS.SND.LOAM': 'SANDY LOAM',
    'MUCKY SLT.CLY.LOAM': 'CLAY LOAM',
    'V.ROCKY SILT LOAM': 'SILT LOAM',
    'COBBLY VARIABLE': 'UNKNOWN',
    'ROCKY SANDY LOAM': 'SANDY LOAM',
    'VARIABLE': 'UNKNOWN',
    'GRAVELLY SLT.CLY.LOAM': 'CLAY LOAM',
    'XTR.CINDERY LOAMY SAND': 'LOAMY SAND',
    'STONY OTHER': 'OTHER',
    'LOAM.CRS.SND': 'LOAMY SAND',
    'SHOTTY LOAM': 'LOAM',
    'XTR.GRAVELLY LOAM': 'LOAM',
    'BOULDERY F.SANDY.LOAM': 'SANDY LOAM',
    'CRS.SND.LOAM': 'SANDY LOAM',
    'V.GRAVELLY SLT.CLY.LOAM': 'CLAY LOAM',
    'BOULDERY SILT LOAM': 'SILT LOAM',
    'V.COBBLY LOAMY SAND': 'LOAMY SAND',
    'XTR.COBBLY SANDY LOAM': 'SANDY LOAM',
    'SANDY CLAY': 'CLAY',
    'V.BOULDERY SANDY LOAM': 'SANDY LOAM',
    'CLAY': 'CLAY',
    'V.BOULDERY F.SANDY.LOAM': 'SANDY LOAM',
    'STONY LOAMY SAND': 'LOAMY SAND',
    'V.CINDERY LOAM': 'LOAM',
    'V.STONY SLT.CLY.LOAM': 'CLAY LOAM',
    'CINDERY F.SANDY.LOAM': 'SANDY LOAM',
    'STONY VARIABLE': 'UNKNOWN',
    'V.BOULDERY SILT LOAM': 'SILT LOAM',
    'STONY SAND': 'SAND',
    'V.BOULDERY LOAMY SAND': 'LOAMY SAND',
    'SHOTTY CLAY LOAM': 'CLAY LOAM',
    'COBBLY F.SANDY.LOAM': 'SANDY LOAM'
}
data['SOIL_TXTR_MDFR'] = data['SOIL_TXTR_MDFR'].str.upper().map(remap_texture)
unique_soil_txtr_mdfr = data['SOIL_TXTR_MDFR'].unique()
remap_soil_txtr_mdfr = {value: float(idx) for idx, value in enumerate(unique_soil_txtr_mdfr)}

data['SOIL_EROSION_POTNL'] = data['SOIL_EROSION_POTNL'].map(remaped_soil_erosion_potnl)
data['SOIL_FLOOD_HAZARD'] = data['SOIL_FLOOD_HAZARD'].map(remaped_soil_flood_hazard)
data['SOIL_CONST_HAZARD'] = data['SOIL_CONST_HAZARD'].map(remaped_soil_const_hazard)

data['SOIL_LANDSLIDE_HAZARD'] = ((data['SOIL_EROSION_POTNL'] > 1)|(data['SOIL_FLOOD_HAZARD'] > 1)|(data['SOIL_CONST_HAZARD'] > 1)).astype(int)

data.drop(columns=["SOIL_EROSION_POTNL"], inplace=True)
data.drop(columns=["SOIL_FLOOD_HAZARD"], inplace=True)
data.drop(columns=["SOIL_CONST_HAZARD"], inplace=True)

data["SOIL_PRECIP_LOW"] = data["SOIL_PRECIP"].map(remap_precip_low)
data["SOIL_PRECIP_HIGH"] = data["SOIL_PRECIP"].map(remap_precip_high)
data.drop(columns=["SOIL_PRECIP"], inplace=True)

data["SOIL_DRAIN_RATE"] = data["SOIL_DRAIN_RATE"].map(remap_soil_drain_rate)
data['SOIL_LAYER_RESTR'] = data["SOIL_LAYER_RESTR"].map(remap_soil_layer_restr)
data['SOIL_ROOT_DPT'] = data['SOIL_ROOT_DPT'].map(remap_soil_root_dpt)
data['SOIL_ROCK_FRAG_HIGH'] = data['SOIL_ROCK_FRAG'].map(remap_rock_frag_high)
data['SOIL_ROCK_FRAG_LOW'] = data['SOIL_ROCK_FRAG'].map(remap_rock_frag_low)
data.drop(columns=["SOIL_ROCK_FRAG"], inplace=True)

data['SOIL_TXTR_MDFR'] = data['SOIL_TXTR_MDFR'].map(remap_soil_txtr_mdfr)

print(data['SOIL_TXTR_MDFR'].unique())
print(data['SOIL_ROCK_FRAG_LOW'].unique())
print(data['SOIL_ROCK_FRAG_HIGH'].unique())
print(data['SOIL_LAYER_RESTR'].unique())
print(data['SOIL_DRAIN_RATE'].unique())
print(data['SOIL_PRECIP_HIGH'].unique())
print(data['SOIL_PRECIP_LOW'].unique())


X = data.drop(columns=['SOIL_LANDSLIDE_HAZARD'])  # Inputs
y = data['SOIL_LANDSLIDE_HAZARD']                # Target

# Split into training and testing sets (80/20 split is common)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
model = sklearn.tree.DecisionTreeClassifier()
model.fit(X_train, y_train)
# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")
