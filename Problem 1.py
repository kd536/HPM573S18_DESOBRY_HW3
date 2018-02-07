class Patient:
    """ base class or super class"""
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")
        # this is an abstract function that needs to be implemented in a subclass


class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return: print the name and type of patient when called
        """
        print(type(self))


class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return: print the name and type of patient when called
        """
        print(type(self))


class Hospital:
    def __init__(self, patients, cost, discharges):
        self.patients = patients
        self.cost = cost
        self.discharges = discharges

    def admit(self, patients):  # feed in the patients we're admitting
        self.patients.append(patients)
        # add individual patients and internally store them
        # what each part does:
        # self. = internally storing
        # patients. = the list it's going into
        # append() = this calls the function we're using
        # patients = what we're actually storing

    def discharge_all(self, discharges):
        self.discharges.append(discharges)
        # add individual patients and internally stores them
        # what each part does:
        # self = internally storing
        # discharges = the list it's going into
        # append = this calls the function we're using
        # patients = what we're actually storing

    def get_total_cost(self):
        """
        :return: the expected cost of this hospital day
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting this node
        i = 0  # index to iterate over probabilities
        for thisPatient in self.patients:
            if type(thisPatient) == EmergencyPatient:
                exp_cost += 1000
            elif type(thisPatient) == HospitalizedPatient:
                exp_cost += 2000
            i += 1
        return exp_cost


myHospital = Hospital() # HOW DOES THIS SECTION OF CODE EVEN ADMIT A PATIENT WITHOUT MANUALLY ENTERING IN EVERY PARAMETER?!??
Patient1 = EmergencyPatient("John", 1000, 1)
Patient2 = EmergencyPatient("Seru", 1000, 1)
Patient3 = EmergencyPatient("Aaron", 2000, 1)
Patient4 = HospitalizedPatient("Roko", 2000, 1)
Patient5 = HospitalizedPatient("Clarice", 2000, 1)

myHospital.admit(Patient1)
myHospital.admit(Patient2)
myHospital.admit(Patient3)
myHospital.admit(Patient4)
myHospital.admit(Patient5)

myHospital.discharge_all(Patient1)
myHospital.discharge_all(Patient2)
myHospital.discharge_all(Patient3)
myHospital.discharge_all(Patient4)
myHospital.discharge_all(Patient5)

print('Hospital costs for the day: ', Hospital.exp_cost())

