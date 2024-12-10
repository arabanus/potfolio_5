from main import fair_sharer

def test_fair_sharer():
    # 1 iteration
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    # 2 iterations
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    # no iterations
    assert fair_sharer([0, 1000, 800, 0], 0) == [0, 1000, 800, 0]
    # equal values
    assert fair_sharer([500, 500, 500, 500], 1) == [500, 500, 500, 500]
    # two entries
    assert fair_sharer([1000, 200], 1) == [800, 400]
    
if __name__ == "__main__":
    test_fair_sharer()