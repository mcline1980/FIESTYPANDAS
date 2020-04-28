import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import os

# Import data frames using Pandas
# df_pd1 <- Presence Detected
# df_pnd1 <- Presence no longer Detected
# If This Then That creates two unique spreadsheets in Google Drive and does not allow for merging.
# this process is a work around to get both data sets into a single object to manipulate.

df_pd1 = pd.read_csv('PD.csv', header=None)
df_pd1.columns = ["Date", "Device"]
df_pnd1 = pd.read_csv('PND.csv', header=None)
df_pnd1.columns = ["Date", "Device"]

# Create new DFs to enumerate Home/Away status
df_pd2 = df_pd1
df_pd2['Presence'] = "Home"
df_pnd2 = df_pnd1
df_pnd2['Presence'] = "Away"

# Create new DF to include both Home/Away statuses
frames = [df_pd2, df_pnd2]
df_p = pd.concat(frames)


# Return Unique Devices
def unique_devices():
    devices = df_pd1["Device"].unique()
    print(devices)
    return devices


# Write a data frame to a file. file_name expects string value
def write_excel_file(write_file, file_name):
    write_file.to_excel(file_name + '_xlsout.xlsx', index_label='Index', merge_cells=False)


# Summary Statistics
print("Presence count by device type:")
presence_count = df_p.groupby('Device')['Presence'].value_counts()
print(presence_count)
print(" ")

