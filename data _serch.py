import pandas as pd
import numpy as np

file_name = input("Enter the file path that you want to insert or inspect:\n").strip("'\"")
try:
    df = pd.read_csv(file_name)
    print("\n\n\n")
    print("✅ The file loaded successfully!")
    print(df)
    print("\n\n\n")

except Exception as e:
    print("⚠️ ERROR:", e)
 
    #analisis of the data set 
column_name = df.select_dtypes(include=np.number).columns
print("The columns in the dataset are:",list( column_name))
#now use all the coloumn data sparety ly
for  col  in range(len(column_name)):
    print(f"\n analyzing:{column_name[col]}")
    print("the meanimum range is:",df[column_name[col]].min())
    print("the maximum range is:",df[column_name[col]].max())
    print("the average is:",df[column_name[col]].mean())
    print("the median is:",df[column_name[col]].median())








