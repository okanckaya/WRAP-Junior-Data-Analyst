-- Load data from Excel file
SELECT * INTO df_raw
FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0',
'Excel 12.0;Database=/Users/okan/Documents/Projects/WRAP/rawdata.xlsx;HDR=YES',
'SELECT * FROM [Sheet2$]');

-- Select specific columns and rename them
SELECT [Local Authority] AS Local_Authority,
       [District],
       [Date Period] AS Date_Period,
       [QuestionNumber],
       [QuestionText],
       [Items],
       [ColText],
       [Tonnes collected] AS Tonnes_Collected,
       [Material Group] AS Material_Group
INTO df_raw
FROM df_raw;

-- Replace "-" with 0 in Tonnes_Collected column
UPDATE df_raw
SET Tonnes_Collected = 0
WHERE Tonnes_Collected = '-';

-- Task I: Tonnes of waste by Material Group
SELECT Material_Group, SUM(Tonnes_Collected) AS sum
INTO df_material_by_tonnes
FROM df_raw
GROUP BY Material_Group
ORDER BY sum DESC;

-- Task II: Which three Local Authorities collected the most waste?
SELECT TOP 3 Local_Authority, SUM(Tonnes_Collected) AS sum
INTO df_loc_aut_by_tonnes
FROM df_raw
GROUP BY Local_Authority
ORDER BY sum DESC;

-- Task III: Which Local Authorities collect aluminium cans?
SELECT DISTINCT Local_Authority
INTO df_aluminium_la
FROM df_raw
WHERE Items = 'Aluminium cans' AND Tonnes_Collected > 0;
