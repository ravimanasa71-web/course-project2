

 test_grade_calculator.py
import pytest
from grade_calculator import (
    calculate_average,
    assign_grade,
    get_student_report,
    evaluate_pass_status,
)


def test_grade_s_and_a():
    assert assign_grade(95.0) == "Grade S"
    assert assign_grade(90.0) == "Grade S"
    assert assign_grade(85.5) == "Grade A"
    assert assign_grade(80.0) == "Grade A"


def test_grade_b_and_c():
    assert assign_grade(72.0) == "Grade B"
    assert assign_grade(65.0) == "Grade B"
    assert assign_grade(58.0) == "Grade C"
    assert assign_grade(50.0) == "Grade C"


def test_grade_d_and_f():
    assert assign_grade(45.0) == "Grade D"

    assert assign_grade(39.9) == "Grade F"
    assert assign_grade(20.0) == "Grade F"


def test_calculate_average():
    assert calculate_average(90, 92, 94) == 92.0
    assert calculate_average(75, 80, 70) == 75.0
    def test_get_student_report_complete():

    assert report["name"] == "manasa"
    assert report["department"] == "BCA"
    assert report["semester"] == 3
    assert report["average"] == 86.0
    assert report["grade"] == "Grade A"


def test_evaluate_pass_status():
    assert evaluate_pass_status("Grade S") == "PASS"
    assert evaluate_pass_status("Grade D") == "PASS"
    assert evaluate_pass_status("Grade F") == "FAIL"


def test_invalid_marks_out_of_range():
    with pytest.raises(ValueError):
        calculate_average(105, 80, 90)
    with pytest.raises(ValueError):
        calculate_average(70, -5, 80)


def test_invalid_student_details():
    with pytest.raises(ValueError):
        get_student_report("", "BCA", 3, [80, 80, 80])
    with pytest.raises(ValueError):
        get_student_report("manasa", "BCA", 3, [80, 85])
