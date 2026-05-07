
import lab2.bmi as bmi

def test_bmi_normal():
    height = 1.78
    weight = 67
    anj = bmi.calculate_bmi(height, weight)
    assert(anj == 0)

def test_bmi_under():
    height = 2.01
    weight = 67
    anj = bmi.calculate_bmi(height,weight)
    assert(anj == -1)

def test_bmi_over():
    height = 1.45
    weight = 67
    anj = bmi.calculate_bmi(height, weight)
    assert(anj == 1)
print('test')