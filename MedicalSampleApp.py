# File: MedicalSampleApp.py

# Class to store patient information
class Patient:
    # Constructor to initialize patient details
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinicals = []  # List to store clinical data

    # Method to add clinical data to the patient
    def add_clinical_data(self, clinical_data):
        self.clinicals.append(clinical_data)


# Class to store clinical data information
class Clinical:
    # Constructor to initialize clinical data details
    def __init__(self, component_name, component_value):
        self.component_name = component_name
        self.component_value = component_value


# Creating a Patient object
p1 = Patient(name="John", age=40)

# Adding clinical data for the patient
c1 = Clinical(component_name="Blood Pressure", component_value="80/120")
p1.add_clinical_data(c1)

c2 = Clinical(component_name="Heart Rate", component_value="80 bpm")
p1.add_clinical_data(c2)

# Displaying patient information
print("Patient Name:", p1.name)
print("Patient Age:", p1.age)

# Looping through and displaying the clinical data for the patient
print("\nClinical Data:")
for clinical in p1.clinicals:
    print(f"- {clinical.component_name}: {clinical.component_value}")
