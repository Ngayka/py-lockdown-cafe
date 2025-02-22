class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Non vaccinated!") -> None:
        super().__init__(message)
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message="Where is your mask?") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Vaccine expired!") -> None:
        super().__init__(message)
