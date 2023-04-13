from plane import Plane
class AircraftCompany:
    def __init__(self, name, founded_year, address: str, planes: list):
        self.name = name
        self.founded_year = founded_year
        self.address = address
        self.planes = planes

    def add_plane(self, plane: Plane):
        self.planes.append(plane)
        print(f"{plane} added!")

    def remove_plane(self, plane: Plane):
        self.planes.remove(plane)
        print(f"{plane} removed!")

    def get_planes(self):
        return self.planes

