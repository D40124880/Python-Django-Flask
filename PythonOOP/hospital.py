class Patient(object):
    def __init__(self, id_num, name, allergies):
        self.id_num = id_num
        self.name = name
        self.allergies = allergies
        self.bed_num = 0

class Hospital(Patient):
    def __init__(self, patients, hospital_name, capacity):
        super
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = 600
    def admit(self, name, bed_num):
        super
        self.patients.append(self.name)
        bed_num.random.randint(1, 101)
        if len(self.patients) >= self.capacity:
            print "Hospital is full"
        else:
            self.patients.append(self.name)
    def discharge(self, name, bed_num):
        super
        self.patients.remove(self.name)
        bed_num = 0