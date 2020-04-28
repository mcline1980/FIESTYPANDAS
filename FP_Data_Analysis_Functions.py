import pandas as pd
from datetime import datetime
from FP import df_p

print(df_p.head())


# Return Unique Devices
def unique_devices():
    devices = df_pd1["Device"].unique()
    print(devices)
    return devices


# Summary Statistics by column
def summary_stats(request, data_frame):
    print("Presence count by " + request + " type:")
    presence_count = data_frame.groupby(request)['Presence'].value_counts()
    print(presence_count)
