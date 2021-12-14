from n1_dz8 import Human

class student(Human):
    def __init__(self, age,  gender, name, _PhoneNumber, wildness, species, voice, dangerous, count_submitted_homework):
        super().__init__(age, gender, name, _PhoneNumber, wildness, species, voice, dangerous)
        self.count = count_submitted_homework
    
    def HelloFriend(self, txt):
        print(f'Привет, я {self.name}, я сделал {self.count} Домашних работ. {txt}')

    # def __cmp__(self, other):
    #     if self.count < Student.count:
    #         return -1
    #     elif self.count > Student.count:
    #         return 1
    #     else:
    #         return 0
    def __gt__(self, stud):
       return self.count > stud.count

    def __lt__(self, stud):
       return self.count < stud.count

    def __le__(self, stud):
       return self.count <= stud.count

    def __ge__(self, stud):
       return self.count >= stud.count

    def __eq__(self, stud):
       return self.count == stud.count

    def __ne__(self, stud):
       return self.count != stud.count
       
student1 = student(20, 'male', 'Dmitriy', '88005552535', '', '', '', 3, int(8))
student2 = student(22, 'male', 'Ivan', '77 77 02', '', '', '', 10, int(2))
student1.HelloFriend('')
student2.HelloFriend('')
print(f'{student2 > student1}')
print(f'{student2 < student1}')
print(f'{student2 >= student1}')
print(f'{student2 <= student1}')
print(f'{student2 == student1}')
print(f'{student2 != student1}')

