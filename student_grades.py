# student_grades.py

class StudentGrades:
    def __init__(self, name):
        """Initialize the student with a name and an empty list of grades."""
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the student's record."""
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def average_grade(self):
        """Calculate and return the average grade of the student."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        """Return the highest grade."""
        if not self.grades:
            return None
        return max(self.grades)

    def lowest_grade(self):
        """Return the lowest grade."""
        if not self.grades:
            return None
        return min(self.grades)
