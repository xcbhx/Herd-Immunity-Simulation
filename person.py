import random
random.seed(42)
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, is_alive=True, infection = None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = is_alive
        self.infection = infection

    def did_survive_infection(self):
        if self.infection:
            virus_random = random.uniform(0.0, 1.0)
            if virus_random < self.infection.mortality_rate:
                self.is_alive = False
            else:
                self.is_vaccinated = True
                self.infection = None
            return self.is_alive


        

if __name__ == "__main__":
    # Create a vaccinated person and check their attributes
    vaccinated_person = Person(1, True, True, None)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False, True, None)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

  
    # Create a Person object and give them the virus infection
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, True, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus


    # Define infections
    infections = {
        "Bubonic Plague": Virus("Bubonic Plague", 0.6, 0.01),
        "MERS": Virus("MERS", 0.45, 0.005),
        "Polio": Virus("Polio", 0.2, 0.06),
        "MRSA": Virus("MRSA", 0.25, 0.015),
        "Swine Flu": Virus("Swine Flu", 0.001, 0.015)
    }

    # Create groups of people
    people_groups = {}
    for virus_name, virus in infections.items():
        group = [Person(i, False, True, virus) for i in range(1, 101)]
        people_groups[virus_name] = group

    # Process survival stats for each group
    results = {}
    for virus_name, group in people_groups.items():
        survived = 0
        did_not_survive = 0
        for person in group:
            if person.did_survive_infection():
                survived += 1
            else: 
                did_not_survive += 1
        results[virus_name] = {"survived": survived, "did_not_survive": did_not_survive}

    for virus_name, stats in results.items():
        print(f'\n{virus_name}')
        print(f'Survived: {stats["survived"]}')
        print(f'Did not survive: {stats["did_not_survive"]}')
        print(f'Actual mortality rate: {(stats["did_not_survive"] / 100) * 100}%')
            




    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.