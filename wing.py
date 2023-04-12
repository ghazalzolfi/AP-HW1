from plane import Plane
class Wing:
    def __init__(self, length, width, weight, thickness, surface_area, material):
        self.length = length
        self.width = width
        self.weight = weight
        self.thickness = thickness
        self.surface_area = surface_area
        self.material = material
        self.flaps_position = None

    def calculate_surface_area(self):
        return self.length * self.width

    def calculate_wing_loading(self):
        return self.weight / self.surface_area
    def deploy_flaps(self):
        self.flaps_position = "deployed"

    def retract_flaps(self):
        self.flaps_position = "retracted"
