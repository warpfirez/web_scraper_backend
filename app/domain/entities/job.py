from dataclasses import dataclass

@dataclass(eq=True)
class Job:
    """ Business logic class containing unified job information """
    id: str
    title: str
    company: str | None = None
    location: str | None = None
    description: str | None = None
    minSalary: int | None = None
    maxSalary: int | None = None
    somethingTest: bool = True
    

