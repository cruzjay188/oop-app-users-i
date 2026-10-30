class User:
    def __init__(self, name, email, drivers_license, age):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def update_email(self, new_email):
        self.email = new_email

    def __str__(self):
        return f"User({self.name}, {self.email})"


# create a few users
alice = User("Alice Smith", "alice@example.com", "D1234567", 29)
bob = User("Bob Jones", "bob@example.com", "D7654321", 34)
carmen = User("Carmen Diaz", "carmen@example.com", "D1112223", 22)

print(alice.introduce())
print(bob.introduce())
print(carmen)

bob.update_email("bobby@example.com")
print(bob.email)
