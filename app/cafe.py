from datetime import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        today = datetime.date.today()
        expiration_date = datetime["visitor"]["expiration_date"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor doesn`t vaccinated")
        elif "vaccine":
            if expiration_date < today:
                raise OutdatedVaccineError("Vaccine expired")
            elif visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError
        return "Welcome to {cafe.name}"
