class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greetingCount = 0

    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))
    
    def addFriend(self, newFriend):
        return self.friends.append(newFriend)

# I'm bending over a bit to avoid a for loop here. I might need to consider going back and making the for loop work.
    def numFriends(self):
        count = 0
        i = 0
        while(len(self.friends) > i) :
            i = i + 1
            count = count + 1
        print(count)

    def incrementgreeting(self):
        self.greetingCount = self.greetingCount +1
        return self.greetingCount
    
    def numOfGreets(self):
        return self.greetingCount


    def greetFriend(self, greetingCount, other_person):
        self.incrementgreeting()
        return "Hello, {}! I'm {}".format(other_person.name, self.name)
        


Sunny = Person("Sunny", 'Sunny@gmail.com', '495-586-3455')
Jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')

Sunny.greet(Jordan)
Jordan.greet(Sunny)
Jordan.addFriend(Sunny)

Jordan.numFriends()
Sunny.greetFriend(Jordan, Sunny)
print("The number of greets Sunny has given is = : " + str(Sunny.numOfGreets()))

print(Sunny.email +"  " + Sunny.phone)
print(Jordan.email +"  " + Jordan.phone)
print(Jordan.friends[0].name)