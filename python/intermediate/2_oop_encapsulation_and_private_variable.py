class MedicalRecord:
    def __init__(self, patient_name, diagnosis=None):
        self.__patient_name = patient_name
        if diagnosis is None:
            self.__diagnosis = "Not yet diagnosed"
        else:
            self.__diagnosis = diagnosis
    
    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis

    def get_summary(self):
        print(f"Patient: {self.__patient_name}")
        print(f"Diagnosis: {self.__diagnosis}")

patient = MedicalRecord("Andrew")
patient.set_diagnosis("Influenza")
patient.get_summary()

