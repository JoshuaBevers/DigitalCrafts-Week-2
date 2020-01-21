class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))

Sunny = Person("Sunny", 'Sunny@gmail.com', '495-586-3455')
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')

Sunny.greet(Jordan)
Jordan.greet(Sunny)

print(Sunny.email +"  " + Sunny.phone)
print(Jordan.email +"  " + Jordan.phone)