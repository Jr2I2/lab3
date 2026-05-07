import price_info as info

def test_total_cost():
    assert(info.total_cost_shopping() == 46.75)

def test_fruit_normal():
    cost = info.cost_of_fruits('apple',10)
    assert(cost == 12.0)