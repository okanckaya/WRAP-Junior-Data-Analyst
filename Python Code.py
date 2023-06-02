import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df_raw = pd.read_excel("/Users/okan/Documents/Projects/WRAP/rawdata.xlsx", sheet_name = 1)

df_raw = df_raw[['Local Authority', 'District',
                 'Date Period', 'QuestionNumber', 'QuestionText', 'Items', 'ColText',
                 'Tonnes collected', 'Material Group']]

df_raw = df_raw.rename(columns={'Local Authority': 'Local_Authority',
                                'Date Period': 'Date_Period',
                                'Tonnes collected': 'Tonnes_Collected',
                                'Material Group ': 'Material_Group'})

df_raw['Tonnes_Collected'] = df_raw['Tonnes_Collected'].replace("-", 0)

# Task I: Tonnes of waste by Material Group

df_material_by_tonnes = df_raw.groupby('Material Group').Tonnes_Collected.agg(['sum']).sort_values(by= 'sum', ascending=False)
df_material_by_tonnes['Material Group'] = df_material_by_tonnes.index
df_material_by_tonnes = df_material_by_tonnes.reset_index(drop="True")

df_material_by_tonnes = df_material_by_tonnes.rename(columns={'sum': 'Tonnes Collected'})

df_material_by_tonnes.columns

## Visuals for Task I

plt.figure(figsize=(40,30))
plt.bar(df_material_by_tonnes['Material Group'], df_material_by_tonnes['Tonnes Collected'])
plt.xlabel('Material Group', fontsize = 34)
plt.ylabel('Tonnes', fontsize = 34)
plt.title('Tonnes of Waste Collected by Material Groups', fontsize = 34)
plt.xticks(rotation=70, fontsize = 24)
plt.show()

# Task II: Which three Local Authorities collected the most waste?

df_loc_aut_by_tonnes = df_raw.groupby('Local_Authority').Tonnes_Collected.agg(['sum']).sort_values(by= 'sum', ascending=False)
df_loc_aut_by_tonnes['Local_Authority'] = df_loc_aut_by_tonnes.index
df_loc_aut_by_tonnes = df_loc_aut_by_tonnes.reset_index(drop="True")
df_loc_aut_by_tonnes = df_loc_aut_by_tonnes.rename(columns={'sum': 'Tonnes Collected'})
df_loc_aut_by_tonnes = df_loc_aut_by_tonnes.head(3)
df_loc_aut_by_tonnes

## Visuals for Task II

plt.figure(figsize=(20,15))
plt.bar(df_loc_aut_by_tonnes['Local_Authority'], df_loc_aut_by_tonnes['Tonnes Collected'])
plt.xlabel('Local_Authority', fontsize = 24)
plt.ylabel('Tonnes', fontsize = 24)
plt.title('Top Three Local Authorities with Collected the Most Waste', fontsize = 24)
plt.xticks(fontsize = 24)
plt.show()

# Task III: Which Local Authorities collect aluminium cans?

df_aluminium = df_raw[df_raw['Items'].isin(["Aluminium cans"]) & df_raw['Tonnes_Collected']>0]
df_aluminium_la = df_aluminium["Local_Authority"].unique()
df_aluminium_la
