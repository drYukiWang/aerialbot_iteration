from math import cos, pi
import numpy as np 
import pandas as pd 
from pathlib import Path

class iterGPS:
    """
    to be able to iterate a list of GPS coordinates for `point`
    """

    def compute_gps_df(self, clat, clon, dist, num):
        """
        to approximately compute the list of gps coordinates of a dist km X dist km area divided by num by num grid cells, given the (clat, clon) pair of the central point of interest
        
        Parameters
        ----------
        clat: lat of the central reference point
        clon: lon of the central reference point
        dist: length of the area of interest
        num: number of cell divisions in one direction, eg. num=10, means 10 X 10 grid cells; we aim to keep each grid cell at 0.5km X 0.5km

        Returns
        -------
        df_gps: contains all 400 gps coordinates in the 10km X 10km region

        """
        alpha = (180/pi) * (dist/6370)

        phi = alpha * cos(clat * (pi/180))

        min_lat = clat - alpha / 2
        max_lat = clat + alpha / 2
        min_lon = clon - phi / 2 
        max_lon = clon + phi / 2

        # generate num X num grid cells
        lat_arr = np.linspace(min_lat, max_lat, num)
        lon_arr = np.linspace(min_lon, max_lon, num)

        gps_list = []
        for lat in lat_arr:
            for lon in lon_arr:
                latlon_dict = {"lat": lat, "lon": lon}
                gps_list.append(latlon_dict)

        df_gps = pd.DataFrame(gps_list)

        return df_gps

    def write_to_csv(self, df, trgPath, filename):
        Path(trgPath).mkdir(parents=True, exist_ok=True)
        df.to_csv(Path(trgPath, filename), index=False)

    def get_coords_list(self, df_gps):
        """
        to get the coordinates list from dataframe `df_gps`
        """
        coords_list = []
        for row in range(df_gps.shape[0]):
            lat = df_gps.iloc[row]['lat']
            lon = df_gps.iloc[row]['lon']
            coord = (lat, lon)
            coords_list.append(coord)
        
        return coords_list


        

        

