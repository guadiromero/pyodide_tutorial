import argparse
import geopandas as gpd
import io
import matplotlib.pyplot as plt
import pandas as pd
import requests
from shapely.geometry import Point, Polygon
import zipfile


class GeodataPlotter:
    def __init__(self, shapefile=None, data_points=None, x_coord=None, y_coord=None):
        self.shapefile = shapefile
        self.data_points = data_points
        self.x_coord = x_coord
        self.y_coord = y_coord

    def read_data_points(self, url):
        """
        Read data points from a CSV file.

        :param url: str, URL containing the CSV with the datapoints
        """
        # Load the csv file
        data_points = pd.read_csv(url, sep=";", decimal=",")

        # Keep only the columns that we need
        data_points = data_points[["XGCSWGS84",
                                   "YGCSWGS84"]]

        self.data_points = data_points
        self.x_coord = data_points["XGCSWGS84"]
        self.y_coord = data_points["YGCSWGS84"]

    def read_shapefile(self, url):
        """
        Read shapefile.

        :param url: str, URL containing a ZIP with the shapefile.
        """
        local_path = "tmp/"
        req = requests.get(url)
        zip_contents = zipfile.ZipFile(io.BytesIO(req.content))
        zip_contents.extractall(path=local_path)
        dbf, prj, shp, shx = [f for f in sorted(zip_contents.namelist()) for ending in
                              ['dbf', 'prj', 'shp', 'shx'] if f.endswith(ending)]
        shapefile = gpd.read_file(local_path + shp)

        self.shapefile = shapefile

    def plot(self):
        """
        Plot datapoints on a map.
        """
        # Plot map
        fig, ax = plt.subplots(figsize=(10, 10))
        self.shapefile.plot(ax=ax, edgecolor="k", alpha=1, linewidth=1, cmap="Set3")

        # Plot data points
        crs = {"init": "epsg:4326"}
        geometry = [Point(xy) for xy in zip(self.x_coord, self.y_coord)]

        geodata = gpd.GeoDataFrame(self.data_points, crs=crs, geometry=geometry)
        geodata.plot(ax=ax, marker=".", markersize=1, color="black")

        plt.title("Straßenverkehrsunfälle in Berlin 2021")
        plt.axis("off")
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_points", help="URL of the data points")
    parser.add_argument("shapefile", help="URL of the shapefile")
    args = parser.parse_args()

    plotter = GeodataPlotter()
    plotter.read_data_points(args.data_points)
    plotter.read_shapefile(args.shapefile)
    plotter.plot()


if __name__ == "__main__":
    main()
