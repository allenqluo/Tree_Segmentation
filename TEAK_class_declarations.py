import numpy as np

class Teak_plot:
    def __init__(self, plotid):
        self.plotid = plotid
        self.x_coord = 0
        self.y_coord = 0

        self.plot_type = "none"
        self.plot_dim = "none"
        self.crs = "none"

        self.tree_individualID = np.array([], dtype=str)
        self.tree_height_array = np.array([], dtype=float)
        self.extended_height_array = np.array([], dtype=float)
        self.Li_dz_indiv = np.array([], dtype=float)
        self.Li_dz_total = np.array([], dtype=float)
        self.acc_LAI = np.array([], dtype=float)
        self.gap = np.array([], dtype=float)
        self.waveform = np.array([], dtype=float)
        self.gsmooth_wvfm = np.array([], dtype=float)
        self.gaussian_wvfm = np.array([], dtype=float)
        self.LAI = 0

    def __str__(self):
        return f"Tree {self.tree_index}: {self.__dict__}"

    def print_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class Teak_subplot:
    def __init__(self, subplot_id):
        self.subplot_id = subplot_id
        self.x_coord = 0
        self.y_coord = 0

        self.parent_plot = "none"
        self.subplot_dim = "none"

class Tree:
    def __init__(self, individualID):
        self.individualID = individualID
        self.plot_ident = ""

        self.growthForm = "none"
        self.plantStatus = "none"
        self.stemDiameter = 0
        self.height = 0
        self.baseCrownHeight = 0
        self.crownCenterHeight = 0
        self.horiz_crown_radius = 0
        self.vert_crown_radius = 0
        self.horiz_crown_diameter = 0
        self.vert_crown_diameter = 0
        self.crown_volume = 0
        self.LAI = 0
        self.Fa = 0

        self.easting = 0
        self.northing = 0
        self.lat = 0
        self.lon = 0