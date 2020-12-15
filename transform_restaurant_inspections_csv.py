import os.path as os
import pandas as pd
import csv

input_path = os.join(".","restaurant_inspections_original.csv")
inspection_df = pd.read_csv(input_path)
# inspection_df.head()

rename_columns = {"facility_name":"Restaurant Name", "facility_address":"Restaurant Address", "facility_city":"Restaurant City", 
           "facility_state":"Restaurant State", "facility_zip":"Restaurant ZIP", "score":"Health Inspection Score", 
           "grade":"Health Inspection Grade","record_id":"Restaurant ID"}

inspection_df = inspection_df.rename(columns=rename_columns)

columns = ["Restaurant ID", "Restaurant Name", "Restaurant Address", "Restaurant City", 
           "Restaurant State", "Restaurant ZIP", "Health Inspection Score", 
           "Health Inspection Grade"]

inspection_clean_df = inspection_df[columns].copy()

inspection_clean_df.drop_duplicates(subset="Restaurant ID", keep="first", inplace=True)

inspection_clean_df["Restaurant ZIP"] = inspection_clean_df["Restaurant ZIP"].str[:5]

output_path = os.join(".", "restaurant_inspections_clean.csv")
inspection_clean_df.to_csv(output_path, index=False)