import pandas as pd
import os 
import glob
from itertools import chain

source_dir = "garmin_activities_csv_files/"
output_dir = ""
csv_files = glob.glob(os.path.join(source_dir, "*.csv"))

garmin_df = {}
list_of_dates = []
for file in csv_files:
    from_date = "-".join(file.split(".")[0].split("_")[-7:-4])
    to_date = "-".join(file.split(".")[0].split("_")[-3:])
    list_of_dates.append(from_date)
    list_of_dates.append(to_date)
    garmin_df[(from_date, to_date)] = pd.read_csv(file)
start_date = pd.Series(list_of_dates).min()
end_date = pd.Series(list_of_dates).max()
output_path = f"{output_dir}garmin_activities_{start_date}_to_{end_date}.csv".replace("-", "_")

garmin_full_df = pd.concat(list(garmin_df.values())).sort_values(by="Date").drop_duplicates(subset=["Activity Type", "Date"]).reset_index(drop=True)

garmin_full_df.to_csv(output_path)
