import os
import pandas as pd
from pandas_profiling import ProfileReport

path = os.path.join(f"/home/stano/Project/Sensor_Gas", "Gas_Sensor/")
os.chdir(path)
files = sorted(os.listdir())


for i in range(0,13):
    df = pd.read_csv(f"{path}/{files[i]}")
    pf = ProfileReport(df, title = f"Day {i+1} Summary Report")
    pf.to_file(f"/home/stano/Project/Sensor_Gas/Profiling_Actual_Data/Day-{i+1}.html")