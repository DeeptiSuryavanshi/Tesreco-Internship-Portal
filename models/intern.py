class Intern:
    def __init__(self, id, name, email, phone, address, domain):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.domain = domain

    def __str__(self):
        return f"{self.name} - {self.domain}"