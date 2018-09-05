grade_value = [80,65,50,30,20]
class Student(object):
    def __init__(self,student_id,mid,final):
        self.student_id = student_id
        self.mid = mid
        self.final = final
        self.total = mid + final
        self.avg = self.total/2
    def get_grade(self):
        if self.avg > grade_value[0]:
            return "A"
        elif self.avg > grade_value[1]:
            return "B"
        elif self.avg > grade_value[2]:
            return "C"
        elif self.avg > grade_value[3]:
            return "D"
        else:
            return "F"
    def __str__(self):
        return str(self.student_id)+" | "+self.grade
# main routine
st1 = Student(20110000,80,90)
st1.grade = st1.get_grade()