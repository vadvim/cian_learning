class Entry:

    def __init__(self, name, address, lastname, phone, email, job):
        self.name = name
        self.address = address
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.job = job

    def to_dict( self):
        return {"name": self.name, "address": self.address, "lastname": self.lastname, "email": self.email,
              "phone": self.phone, "job": self.job}