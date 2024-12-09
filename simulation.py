import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []


    def _create_population(self):
        """Create a list of Person instances representing the population."""
        population = []
        for i in range(pop_size):
            if i < self.initial_infected:
                population.append(Person(i, is_vaccinated=False, infection=self.virus))
            elif random.random() < self.vacc_percentage:
                population.append(Person(i, is_vaccinated=True, infection=None))
            else:
                population.append(Person(i, is_vaccinated=False, infection=None))
        return population


    def _simulation_should_continue(self):
        """Detemines whether the simulation should cotinue."""
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                # Found at least one living, non-vaccinated person
                return True
        return False
         

    def run(self):
        """Run the simulation"""
        time_step_counter = 0
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()

        self.logger.log_infection_survival(time_step_counter, self.pop_size, len([p for p in self.population if not p.is_alive]))

    def time_step(self):
        """Simulate interactions for each infected person."""
        for person in self.population:
            if person.is_alive and person.infection:
                interactions = 0
                while interactions < 100:
                    random_person = random.choice(self.population)
                    if random_person.is_alive and random_person != person:
                        self.interaction(person, random_person)
                        interactions += 1

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        """Handles an interaction between an infected person and another."""
        if random_person.is_vaccinated or random_person.infection:
            self.logger.log_interactions(0, 1, 0)
            return
        
        if random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person._id)
            self.logger.log_interactions(0, 1, 1)

    def _infect_newly_infected(self):
        """Infect the newly infected people."""
        for person_id in self.newly_infected:
            person = self.population[person_id]
            if person.is_alive:
                person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the simulation
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
