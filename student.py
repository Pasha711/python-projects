class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def addMark(self, subj, mark):
        self.marks[subj] = mark

    def totalMarks(self):
        msum = 0
        for i in self.marks:
            msum += self.marks[i]
        return msum

    def percentage(self):
        psum = (self.totalMarks() / (len(self.marks) * 100)) * 100
        return psum


st01 = Student('John', {'Bio': 60, 'Math': 75, 'Lit': 35})
st01.addMark('Geo', 55)
print('Total Marks:', st01.totalMarks())
print('Percentage :', st01.percentage())
