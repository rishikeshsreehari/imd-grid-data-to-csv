
import imdlib as imd


start_yr = 1952 # give starting year from which you want to download/convert data: 1901 ownwards for rainfall, 1951 for tmax and tmin
end_yr = 2022 # give ending year upto which you want to download/convert data
variable = 'tmax' # give variable name (rain for rainfall at 0.25 deg, tmax or tmin for rainfall, min or max temperature at 1 deg resolution)
file_format = 'yearwise' # other option (None), which will assume deafult imd naming convention
file_dir = 'path' # this path should be same as mentioned in previous line
data = imd.open_data(variable, start_yr, end_yr,'yearwise', file_dir) # this will open the data downloaded and saved in the location mentioned in previous line
path = 'file_path'


if variable == 'rain':
    grid_size = 0.25 # grid spacing in deg
    y_count = 129 # no of grids in y direction
    x_count = 135 # no of grids in x direction
    x = 66.5 # starting longitude taken from control file (.ctl)
    y = 6.5 # starting latitude taken from control file (.ctl)
elif variable == 'tmax' or variable == 'tmin':
    grid_size = 1 # grid spacing in deg
    y_count = 31 # no of grids in y direction
    x_count = 31 # no of grids in x direction
    x = 67.5 # starting longitude taken from control file (.ctl)
    y = 7.5 # starting latitude taken from control file (.ctl)

#print(grid_size,x_count, y_count, x, y)
data
data.shape
np_array = data.data
#print(np_array[0,0,0])
#xr_objecct = data.get_xarray()
#type(xr_objecct)
#xr_objecct.mean('time').plot()
years_no = (end_yr - start_yr) + 1
#print(years_no)
day = 0
for yr in range(0,years_no):
    f = open(r"path"+str(start_yr+yr)+"_"+str(variable)+".csv",'w') # just change the path where you want to save csv file
    if ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 != 0):  # check for leap year
        days = 366
        count = yr + days
    elif ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 == 0) and ((start_yr+yr) % 400 == 0):
        days = 366
        count = yr + days
    else:
        days = 365
        count = yr + days

    day = day + days

    f.write("X,Y,")
    for d in range(0, days):
        f.write(str(d+1))
        f.write(",")
    f.write("\n")
    #print(np_array[364,0,0])
    for j in range(0, y_count):

        for i in range(0, x_count):

            f.write(str((i * grid_size) + x))
            f.write(",")
            f.write(str((j * grid_size) + y))
            f.write(",")
            time = 0
            for k in range(day-days, day):

                val = np_array[k,i,j]
                if val == 99.9000015258789 or val == -999:
                    f.write(str(-9999))
                    f.write(",")
                else:
                    f.write(str(val))
                    f.write(",")


            f.write("\n")
    print("File for " + str(start_yr + yr) + "_" + str(variable) + " is saved")
print("CSV conversion successful !")

#Data conversion Code blelow

#Maximum Combine

import pandas as pd

start_yr = 1952
end_yr = 2022

# Define the X and Y coordinates for which you want to combine the t_max values
target_x = 77.5
target_y = 13.5
city = 'Bangalore'

combined_data = pd.DataFrame(columns=['X', 'Y', 'Year'])  # Add 'Year' to the columns

# Iterate over the years and read the corresponding t_max file
for year in range(start_yr, end_yr + 1):
    filename = f"path\IMD_Grid_data{year}_tmax.csv"
    df = pd.read_csv(filename)

    # Filter the dataframe based on the target X and Y coordinates
    filtered_data = df[(df['X'] == target_x) & (df['Y'] == target_y)]

    # Add a new column 'Year' to the filtered_data and set its value to the current year
    filtered_data['Year'] = year

    # Append the filtered data to the combined dataframe
    combined_data = combined_data.append(filtered_data)

# Save the combined data to a new CSV file
output_filename = f"path\{city}_combined_tmax.csv"
combined_data.to_csv(output_filename, index=False)

print("Combined t_max values for X =", target_x, "and Y =", target_y, "are saved in", output_filename)



# Read the CSV file
df = pd.read_csv(f"path\{city}_combined_tmax.csv")



# Create a new DataFrame to store the transformed data
transformed_data = pd.DataFrame(columns=['Date', 't_max', 'X', 'Y'])

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    year = int(row['Year'])
    x = row['X']
    y = row['Y']
    print(year)
    
    # Iterate over the columns starting from the 1st index (ignoring 'X', 'Y', and 'Year')
    for i in range(3, len(row)):
        day_of_year = int(i - 2)
        date = pd.to_datetime(f"{year}-01-01") + pd.DateOffset(days=day_of_year - 1)
        formatted_date = date.strftime('%d-%m-%Y')
        t_max = row[i]
        
        # Append the new row to the transformed DataFrame
        transformed_data = transformed_data.append({'Date': formatted_date, 't_max': t_max, 'X': x, 'Y': y}, ignore_index=True)
        
# Save the transformed data to a new CSV file
transformed_data.to_csv(f'path\{city}_transformed_max.csv', index=False)

print("Data transformation complete. Saved to transformed_data.csv.")


###Minimum data

variable = 'tmin' # give variable name (rain for rainfall at 0.25 deg, tmax or tmin for rainfall, min or max temperature at 1 deg resolution)


combined_data = pd.DataFrame(columns=['X', 'Y', 'Year'])  # Add 'Year' to the columns

# Iterate over the years and read the corresponding t_max file
for year in range(start_yr, end_yr + 1):
    filename = f"path\IMD_Grid_data{year}_tmin.csv"
    df = pd.read_csv(filename)

    # Filter the dataframe based on the target X and Y coordinates
    filtered_data = df[(df['X'] == target_x) & (df['Y'] == target_y)]

    # Add a new column 'Year' to the filtered_data and set its value to the current year
    filtered_data['Year'] = year

    # Append the filtered data to the combined dataframe
    combined_data = combined_data.append(filtered_data)

# Save the combined data to a new CSV file
output_filename = f"path\{city}_combined_tmin.csv"
combined_data.to_csv(output_filename, index=False)

print("Combined t_max values for X =", target_x, "and Y =", target_y, "are saved in", output_filename)



# Read the CSV file
df = pd.read_csv(f"path\{city}_combined_tmin.csv")



# Create a new DataFrame to store the transformed data
transformed_data = pd.DataFrame(columns=['Date', 't_min', 'X', 'Y'])

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    year = int(row['Year'])
    x = row['X']
    y = row['Y']
    print(year)
    
    # Iterate over the columns starting from the 1st index (ignoring 'X', 'Y', and 'Year')
    for i in range(3, len(row)):
        day_of_year = int(i - 2)
        date = pd.to_datetime(f"{year}-01-01") + pd.DateOffset(days=day_of_year - 1)
        formatted_date = date.strftime('%d-%m-%Y')
        t_max = row[i]
        
        # Append the new row to the transformed DataFrame
        transformed_data = transformed_data.append({'Date': formatted_date, 't_min': t_max, 'X': x, 'Y': y}, ignore_index=True)
        
# Save the transformed data to a new CSV file
transformed_data.to_csv(f'path\{city}_transformed_min.csv', index=False)

print("Data transformation complete. Saved to transformed_data.csv.")


