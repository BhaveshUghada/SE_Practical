# test_student_grades.py

import pytest
from student_grades import StudentGrades

# Test data set-up method
@pytest.fixture
def student():
    """Set up a student with some initial grades."""
    student = StudentGrades("Aditya Pawar")
    student.add_grade(85)
    student.add_grade(90)
    student.add_grade(78)
    return student

# Test adding grades
def test_add_grade(student):
    student.add_grade(92)
    assert len(student.grades) == 4
    assert student.grades[-1] == 92

# Test calculating average grade
def test_average_grade(student):
    assert round(student.average_grade(), 2) == 84.33  # (85 + 90 + 78) / 3

# Test getting the highest grade
def test_highest_grade(student):
    assert student.highest_grade() == 90

# Test getting the lowest grade
def test_lowest_grade(student):
    assert student.lowest_grade() == 78

# Test handling invalid grade
def test_invalid_grade():
    student = StudentGrades("Jane Doe")
    with pytest.raises(ValueError):
        student.add_grade(110)  # Invalid grade above 100
    with pytest.raises(ValueError):
        student.add_grade(-10)  # Invalid grade below 0
