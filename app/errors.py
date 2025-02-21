class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message = "Non vaccinated!"):
        super().__init__(message)
    pass


class NotWearingMaskError(VaccineError):
    def __init__(self, message="Where is your mask?"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Vaccine expired!" ):
        super().__init__(message)