from plane import Plane


class AircraftCompany:
    def __init__(self, name, founded_year, address: str, planes: list):
        self.name = name
        self.founded_year = founded_year
        self.address = address
        self.planes = planes

    # aggregation
    def add_plane(self, plane: Plane):
        self.planes.append(plane)
        print(f"{plane} added!")

    def __find_plane(self, plane_aircraft_company):
        founded_plane = None
        for plane in self.planes:
            if plane.aircraft_company == plane_aircraft_company:
                founded_plane = plane
        return founded_plane

    def remove_plane(self, plane_aircraft_company):
        founded_plane = self.__find_plane(plane_aircraft_company)
        if founded_plane:
            self.planes.remove(plane_aircraft_company)
        return founded_plane

    def get_planes(self):
        return self.planes
