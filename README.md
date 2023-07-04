# imd-grid-data-to-CSV
Convert India Meteorological Department(IMD) grid data to .csv

## Features
- Automatic download of data from the IMD website
- Convert.GRD into .csv files
- Filter the dataset based on the coordinate location provided


Input: IMD website URL, GRD files
Output: .csv



There are two codes in this repository:
- imd_data_download.py: Based on the year selection, the selenium script will download the data from the IMD website automatically
- code.py: Converts the.GRD files into .csv and filters further if required based on the coordinates provided


Code.py was written by modifying the code from this source: https://www.youtube.com/watch?v=9b8bAdVy40Y
