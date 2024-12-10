import pytest
from simulation import Simulation
from virus import Virus


@pytest.fixture
def setup_simulation():
    """Fixture to create a Simulation instance for testing."""
    virus = Virus("TestVirus", 0.5, 0.3)
    sim = Simulation(virus, pop_size=100, vacc_percentage=0.1, initial_infected=5)
    return sim

def test_create_population():
    pass

def test_simulation_should_continue():
    pass

def test_run():
    pass

def test_time_step():
    pass

def test_interaction():
    pass

def test_infect_newly_infected():
    pass