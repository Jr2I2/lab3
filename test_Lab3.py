import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_max_desc():
    input_arr = [1,2,3,4,5,6,7,123,34,324,54,19]
    anj = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert(anj == 1)

def test_bubble_sort_max_asc():
    input_arr = [1,2,3,4,5,6,7,123,34,324,54,19]
    anj = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(anj == 1)

def test_bubble_sort_empty_desc():
    input_arr = []
    anj = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert(anj == 0)

def test_bubble_sort_empty_asc():
    input_arr = []
    anj = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(anj == 0)

def test_bubble_sort_nonnumeric_paraone():
    input_arr = ['23','hi',2.3,123]
    anj = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert(anj == 2)

def test_bubble_sort_nonnumeric_paratwo():
    input_arr = [4,6,23,123]
    anj = Lab3.bubble_sort(input_arr, 'hii')

    assert(anj == 2)