import pandas as pd
import json

# Define the path to your Excel file
excel_file = '/home/iot-2/Desktop/MyProject/automate/excelToJson.xlsx'

jsonObj = {}
rowArr = []
df = pd.read_excel(excel_file, header=None)
rowTotal = df.shape[0]
columnTotal = df.shape[1]
recipeName = ""
keyBahan = ""
keyPenyediaan = ""
keyKategori = ""

for rowName in range( 1, rowTotal ):
    cellRecipeName = df.iloc[rowName,0]
    if not pd.isna( cellRecipeName ):
        rowArr.append( rowName )

rowArr.append( rowTotal )

left = 0
right = left + 1

while right < len( rowArr ):
    for row in range( rowArr[left], rowArr[right] - 1 ):
        cellRecipeName = df.iloc[row,0]
        
        if not pd.isna( cellRecipeName ):
            recipeName = cellRecipeName
            jsonObj[recipeName] = {}
            jsonObj[recipeName]["bahan"] = {}
            jsonObj[recipeName]["penyediaan"] = {}
            jsonObj[recipeName]["kategori"] = {}

        cellBahanKey = df.iloc[row,1]
        cellBahanValue = df.iloc[row,2]

        if not pd.isna( cellBahanKey ):
            keyBahan = cellBahanKey
            jsonObj[recipeName]["bahan"][keyBahan] = []
        if not pd.isna( cellBahanValue ):
            jsonObj[recipeName]["bahan"][keyBahan].append( cellBahanValue )

        cellPenyediaanKey = df.iloc[row,3]
        cellPenyediaanValue = df.iloc[row,4]

        if not pd.isna( cellPenyediaanKey ):
            keyPenyediaan = cellPenyediaanKey
            jsonObj[recipeName]["penyediaan"][keyPenyediaan] = []
        if not pd.isna( cellPenyediaanValue ):
            jsonObj[recipeName]["penyediaan"][keyPenyediaan].append( cellPenyediaanValue )

        cellKategoriKey = df.iloc[row,5]
        cellKategoriValue = df.iloc[row,6]

        if not pd.isna( cellKategoriKey ):
            keyKategori = cellKategoriKey
            jsonObj[recipeName]["kategori"][keyKategori] = []
        if not pd.isna( cellKategoriValue ):
            jsonObj[recipeName]["kategori"][keyKategori].append( cellKategoriValue )

    left += 1
    right += 1

# Convert data to JSON
json_data = json.dumps( jsonObj, indent=4, ensure_ascii=False )
print(json_data)
# # Write JSON data to a file
# with open('output.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

# print("Excel data has been converted to JSON and saved as 'output.json'.")
