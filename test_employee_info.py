import employee_info as info

def test_avgsal():
    assert(info.calculate_average_salary() == 60166)

def test_getdept():
    fellows = info.get_employees_by_dept("sales")
    assert(fellows == [info.employee_data[0],info.employee_data[5]])

def test_agerange():
    fellows = info.get_employees_by_age_range(22, 32)
    assert(fellows == [info.employee_data[0], info.employee_data[1], info.employee_data[2]])