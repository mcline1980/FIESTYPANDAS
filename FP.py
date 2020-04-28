import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import os
from datetime import datetime

# Import data frames using Pandas
# df_pd1 <- Presence Detected, exported from Google Drive as PD.csv
# df_pnd1 <- Presence no longer Detected, exported from Google Drive as PND.csv
# If This Then That (IFTTT) creates two unique spreadsheets in Google Drive
# this process is a work around to get both data sets into a single data frame to manipulate.

df_pd1 = pd.read_csv('PD.csv', header=None)
df_pd1.columns = ["Date", "Device"]
df_pnd1 = pd.read_csv('PND.csv', header=None)
df_pnd1.columns = ["Date", "Device"]

# Create new DFs to enumerate Home/Away status
df_pd2 = df_pd1
df_pd2['Presence'] = "Home"
df_pnd2 = df_pnd1
df_pnd2['Presence'] = "Away"

# Create the final DF to include both Home/Away statuses and retain indexing
df_p = df_pd2.append(df_pnd2, ignore_index=True)


# DT CONVERT 1
# Date and Time conversion function for the format used by IFTTT Samsung Smartthings presence detection
# to Google Sheet applet
def dt_convert_1(s2c):
    s2c = datetime.strptime(s, '%B %d, %Y at %I:%M%p')
    return s2c

# Add new column to DF to account for normalized date and normalized time information
# Use strptime to parse the date string with the following args:: '%B %d, %Y at %I:%M%p'
# Iterate over all rows in the df_p data frame, extract the string from the 'Date' column
# Run strptime against the new variable
# Drop the new datetime variable into the correct location in the data frame using LOC
loc = 0
for i in df_p.iterrows():
    s = df_p.loc[loc, 'Date']
    # s = datetime.strptime(s, '%B %d, %Y at %I:%M%p')
    s = dt_convert_1(s)
    df_p.loc[loc, 'Normalized_Time'] = s
    loc = loc + 1


# Return Unique Devices
def unique_devices():
    devices = df_pd1["Device"].unique()
    print(devices)
    return devices


# Write a data frame to a file. file_name expects string value
def write_excel_file(write_file, file_name):
    write_file.to_excel(file_name + '_xlsout.xlsx', index_label='Index', merge_cells=False)


# Summary Statistics
def summary_stats(request):
    if request == 'Device':
        print("Presence count by device type:")
        presence_count = df_p.groupby('Device')['Presence'].value_counts()
        print(presence_count)


write_excel_file(df_p, 'test_output')
