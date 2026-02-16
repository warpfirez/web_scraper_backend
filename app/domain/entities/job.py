from dataclasses import dataclass

# suppress auto __init__ generation
@dataclass(init=False, eq=True)
class Job:
    """ Business logic class containing unified job information """
    id: str
    title: str
    company: str
    location: str
    description: str
    minSalary: int | None = None
    maxSalary: int | None = None
    somethingTest: bool = True
    
    def __init__(self, id, title, company, location, desctiption, minSalary, maxSalary, somethingTest):
        self.id = id
        self.title = title
        self.company = company
        self.location = location
        self.description = desctiption
        self.minSalary = minSalary
        self.maxSalary = maxSalary
        self.somethingTest = somethingTest
