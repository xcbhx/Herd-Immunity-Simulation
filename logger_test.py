import os
import pytest
from logger import Logger

@pytest.fixture
def test_file():
    """Fixture to create and clean up a temporary test file."""
    filename = "test_logger.txt"
    yield filename # This is the filename passed to the tests
    if os.path.exists(filename):
        os.remove(filename)

def test_write_metadata(test_file):
    logger = Logger(test_file)
    logger.write_metadata(100, 0.1, "HIV", 0.8, 0.035)

    with open(test_file, "r") as file:
        content = file.read()

        expected = (
            "Population Size:\t100\n"
            "Vaccination Percentage:\t0.1\n"
            "Virus Name:\tHIV\n"
            "Mortality Rate:\t0.8\n"
            "Reproduction Rate:\t0.035\n"
        )
        assert content == expected, "Metadata logging failed."

def test_log_interactions(test_file):
    logger = Logger(test_file)
    logger.log_interactions(step_number=1, number_of_interactions=50, number_of_new_infections=10)

    with open(test_file, "r") as file:
        content = file.read()

    expected = (
        "Step 1:\n"
        "Total Interactions: 50\n"
        "New Infections: 10\n\n"
    )
    assert content == expected, "Interaction logging failed."

def test_log_interactions_edge_case(test_file):
    logger = Logger(test_file)
    logger.log_interactions(step_number=2, number_of_interactions=0, number_of_new_infections=0)

    with open(test_file, "r") as file:
        content = file.read()

    expected = (
        "Step 2:\n"
        "No interactions occurred.\n\n"
    )
    assert content == expected, "Edge cases for no interactions failed."

def test_log_infection_survival(test_file):
    logger = Logger(test_file)
    logger.log_infection_survival(step_number=3, population_count=100, number_of_new_fatalities=5)

    with open(test_file, "r") as file:
        content = file.read()

        expected = (
            "Step 3:\n"
            "Population Total: 100\n"
            "New Fatalities: 5\n"
            "Surviving Population: 95\n"
        )
        assert content == expected, "Infection survival logging failed."

def test_invalid_inputs(test_file):
    logger = Logger(test_file)

    with pytest.raises(ValueError):
        logger.log_interactions(step_number=1, number_of_interactions=-10, number_of_new_infections=5)

    with pytest.raises(ValueError):
        logger.log_interactions(step_number=3, number_of_interactions=-100, number_of_new_infections=5)

    with pytest.raises(ValueError):
        logger.log_interactions(step_number=3, number_of_interactions=100, number_of_new_infections=-5)
