import os
import pandas as pd
import glob

all_files = glob.glob(f".\output\**\*.csv", recursive=True)

writer = pd.ExcelWriter('Consolidated_Output.xlsx')

for csvfilename in all_files:
    df = pd.read_csv(csvfilename)
    df.to_excel(writer, sheet_name=csvfilename.split("\\")[-1].rstrip(".csv"))

writer.save()
