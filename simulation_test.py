import pytest
from simulation import Simulation
from virus import Virus


@pytest.fixture
def setup_simulation():
    """Fixture to create a Simulation instance for testing."""
    virus = Virus("TestVirus", 0.5, 0.3)
    sim = Simulation(virus, pop_size=100, vacc_percentage=0.1, initial_infected=5)
    return sim

def test_create_population(setup_simulation):
    sim = setup_simulation
    population = sim.population

    assert len(population) == sim.pop_size, "Population size does not match expected value."

    infected_count = sum(1 for person in population if person.infection is not None)
    assert infected_count == sim.initial_infected, "Initial infected count is incorrect."

    vaccinated_count = sum(1 for person in population if person.is_vaccinated)
    assert vaccinated_count <= int(sim.pop_size * sim.vacc_percentage), "Too many vaccinated people."

def test_simulation_should_continue(setup_simulation):
    sim = setup_simulation

    assert sim._simulation_should_continue(), "Simulation should continue at the start."

    for person in sim.population:
        person.is_alive = False

    assert not sim._simulation_should_continue(), "Simulation should not continue when everyone is dead."

def test_run():
    pass

def test_time_step():
    pass

def test_interaction():
    pass

def test_infect_newly_infected():
    pass