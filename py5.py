class Person:
    def __init__(self, initialAge):
        self.my_age = initialAge
        if self.my_age < 0:
            print('Age is not valid, setting age to 0.')
            self.my_age = 0

    def amIOld(self):
        old_list = ['young.', 'a teenager.', 'old.']
        age_pos = old_list[2]
        if self.my_age < 18:
            age_pos = old_list[0] if self.my_age < 13 else  old_list[1]
        print('You are ' + age_pos)
        

    def yearPasses(self):
        self.my_age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
