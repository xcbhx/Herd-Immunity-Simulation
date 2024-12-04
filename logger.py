class Logger(object):
    def __init__(self, filename):
        """Initialize the Logger with a filename for the log."""
        self.filename = filename


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        """
        Write metadata about the simulation to the log file.

        Args:
        pop_size (int): Total population size.
        vacc_percentage (float): Percentage of the population.
        virus_name (str): Name of the virus.
        mortality_rate (float): Mortality rate of the virus.
        basic_repro_num (float): Basic reproduction number of the virus.
        """
        with open(self.filename, "w") as outfile:
            metadata_lines = [
                f"Population Size:\t{pop_size}\n", 
                f"Vaccination Percentage:\t{vacc_percentage}\n", 
                f"Virus Name:\t{virus_name}\n", 
                f"Mortality Rate:\t{mortality_rate}\n", 
                f"Reproduction Rate:\t{basic_repro_num}\n"
                ]
            outfile.writelines(metadata_lines)


    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """
        Log interactions for a specific step of simulation.

        Args:
        step_number (int): The current step of the simulation.
        number_of_interactions (int): Total number of interactions in this step.
        number_of_new_infections (int): Total number of new infections in this step. 
        """
        if number_of_interactions < 0 or number_of_new_infections < 0:
            raise ValueError("Interaction and infection counts cannot be negative.")

        # Check edge cases and format the log entry
        if number_of_interactions == 0:
            log_entry = f"Step {step_number}:\nNo interactions occured.\n"
        elif number_of_new_infections == 0:
            log_entry = f"Step {step_number}:\nNo new infections occured.\n"
        else:
            log_entry = f"Step {step_number}:\n"
            log_entry += f"Total Interactions:{number_of_interactions}\n"
            log_entry += f"New Infections: {number_of_new_infections}\n"

        # Write to the log file
        with open(self.filename, "a") as outfile:
            outfile.write(log_entry + "\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        # 
        pass


if __name__ == "__main__":
    logger = Logger("logger_test.txt")
    logger.write_metadata(100, 0.1, 'HIV', 0.8, 0.035)
    logger.log_interactions(step_number=1, number_of_interactions=10, number_of_new_infections=2)
    logger.log_interactions(step_number=2, number_of_interactions=0, number_of_new_infections=0)