class Wing:
    def __init__(self, length, width, thickness, material):
        self.length = length
        self.width = width
        self.thickness = thickness
        self.surface_area = None
        self.material = material
        self.flaps_position = None

    def calculate_surface_area(self):
        self.surface_area = self.length * self.width
        return self.surface_area

    def deploy_flaps(self):
        self.flaps_position = "deployed"

    def retract_flaps(self):
        self.flaps_position = "retracted"
