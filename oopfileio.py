import csv

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = float(gpa)

    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

class StudentManager:
    def __init__(self):
        self.students = []

    def load_from_csv(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.students.append(Student(row['name'], row['gpa']))
        except Exception as e:
            print(f"Error reading file: {e}")

    def filter_by_gpa(self, min_gpa):
        return [s for s in self.students if s.gpa >= min_gpa]

    def export_to_csv(self, filename, students):
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['name', 'gpa'])
                for s in students:
                    writer.writerow([s.name, s.gpa])
        except Exception as e:
            print(f"Error writing file: {e}")

    def print_students(self, students=None):
        if students is None:
            students = self.students
        for s in students:
            print(s)

manager = StudentManager()
manager.load_from_csv('students.csv')
manager.print_students()
filtered = manager.filter_by_gpa(3.0)
manager.export_to_csv('filtered_students.csv', filtered)