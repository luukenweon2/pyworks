class student:
    
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
        
    def learn(self):
        print("수업을들어요")
    
s1 = student("김하나", 1)

s2 = student("이돌", 2)

print(s1.name, s1.grade)
print(s2.name, s2.grade)

luu= student("유근원", 5)
print(f"{luu.name} 학생은 {luu.grade} 학년입니다")