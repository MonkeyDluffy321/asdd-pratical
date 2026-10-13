from grade_calculator import calculate_grade

def test_grade_a():
    assert calculate_grade([85,78,92,88,75]) == (418,83.6,"A")

def test_grade_c():
    assert calculate_grade([50,50,50,50,50]) == (250,50.0,"C")
