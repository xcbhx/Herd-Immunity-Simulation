class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        # TODO Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

    def __repr__(self):
        # Return a string representation of the Virus object
        return f'Virus (name = {self.name}, repro_rate = {self.repro_rate}, mortaility_rate = {self.mortality_rate})'

# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus_1 = Virus("E.Coli", 0.1, 0.015)
    virus_2 = Virus("Tuberculosis", 0.055, 0.65)
    virus_3 = Virus("Ebola", 0.023, 0.7)
    virus_4 = Virus("Rabies",0.014, 1)

    print(virus)
    print(virus_1)
    print(virus_2)
    print(virus_3)
    print(virus_4)
