class student:
    
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
        
    def learn(self):
        print("수업을들어요")
    
s1 = student("김하나", 1)

s2 = student("이돌", 2)

print(s1.name)
print(s1.grade)

