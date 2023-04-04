from plane import Plane
class Wing:
    def __init__(self, length, width, weight, thickness, surface_area, material):
        self.length = length
        self.width = width
        self.weight = weight
        self.thickness = thickness
        self.surface_area = surface_area
        self.material = material

    def calculate_surface_area(self):
        pass

    def calculate_wing_loading(self,weight):
        pass
    def deploy_flaps(self):
        pass

    def retract_flaps(self):
        pass
