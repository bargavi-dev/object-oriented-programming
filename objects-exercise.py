class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.add_friend(other_person)
        other_person.add_friend(self)
    
    def print_contact_info(self):
        print(f'''
    {self.name}\'s email: {self.email} 
    {self.name}\'s phone number: {self.phone}
        ''')
    
    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)


    


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordon = Person('Jordon', 'jordon@aol.com', '495-586-3456')

print('--------------')

sonny.greet(jordon)

jordon.greet(sonny)

print(f'Sonny introduced himself {sonny.greeting_count} times')

print('--------------')

print(sonny.email, sonny.phone)

print(jordon.email, jordon.phone)

sonny.print_contact_info()


print('----Friends----')

sonny.add_friend(jordon)

print("Sonny's Friends: ")
for friend in sonny.friends:
    friend.print_contact_info()

print(f"Sonny has {sonny.num_friends()} friends")
print(f"Jordan has {jordan.num_friends()} friends")

print('---------------')