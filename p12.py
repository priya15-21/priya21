class Student:
    def __init__(s, name):
        s.name = name
        s.marks = []

    def add_mark(s, mark):
        if isinstance(mark, (int, float)) and 0 <= mark <= 100:
            s.marks.append(mark)
        else:
            print(f"Invalid mark {mark}. Mark must be between 0 and 100.")

    def add_marks_from_list(s, marks):
        for mark in marks:
            s.add_mark(mark)


student = Student("Priya")
student.add_marks_from_list([90, 85, 110, -5, 75, "abc"])
print(student.marks)
