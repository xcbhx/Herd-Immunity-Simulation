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
        self.population = self._create_population(self.pop_size, self.vacc_percentage, self.initial_infected)


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
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus_mortailty_rate, self.virus.repro_rate)

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()

        self.logger.log_infection_survival(time_step_counter, self.pop_size, len([p for p in self.population if not p.is_alive]))

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        pass

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        pass

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


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

    # sim.run()
