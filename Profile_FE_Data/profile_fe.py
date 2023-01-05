import os
import pandas as pd
from pandas_profiling import ProfileReport

path = os.path.join(f"/home/stano/Project/Sensor_Gas", "Gas_Sensor/")
os.chdir(path)
files = sorted(os.listdir())


for i in range(len(files)):
    df = pd.read_csv(f'{path}/{files[i]}')
    col = {i : i.split()[0] for i in df.columns}
    df.rename(columns=col, inplace=True)
    
    
    df_actual = df[(df["Flow"] >=235) & (df["Flow"] <=246)]
    df_actual = df_actual[df_actual["Temperature"] >= 21]
    
    df_actual["Heater"] = df_actual["Heater"].apply(lambda x: round(x,1))
    df_actual["Flow"] = df_actual["Flow"].apply(lambda x: int(x))
    df_actual["Humidity"] = df_actual["Humidity"].apply(lambda x: int(x))
    df_actual.drop("Time", axis =1, inplace =True)
    
    df_actual["CO"].where(~((df["CO"]>=0) & (df["CO"]<6)),"Low", inplace=True)
    df_actual["CO"].where(~((df["CO"]>=6) & (df["CO"]<13)),"Moderate", inplace=True)
    df_actual["CO"].where(~(df["CO"]>=13),"High", inplace=True)
    
    df_actual["Sensor_1"] = (df_actual["R1"] + df_actual["R2"] + df_actual["R3"] + df_actual["R4"] + df_actual["R5"] + df_actual["R6"] + df_actual["R7"])/7
    df_actual["Sensor_2"] = (df_actual["R8"] + df_actual["R9"] + df_actual["R10"] + df_actual["R11"] + df_actual["R12"] + df_actual["R13"] + df_actual["R14"])/7
    
    df_feature_engineering = df_actual[["Humidity","Temperature", "Flow", "Heater", "Sensor_1", "Sensor_2", "CO"]]
    
    pf = ProfileReport(df_feature_engineering, title = f"Day {i+1} Feature Engineering Summary Report")
    pf.to_file(f"/home/stano/Project/Sensor_Gas/Profile_FE_Data/Day-{i+1}.html")