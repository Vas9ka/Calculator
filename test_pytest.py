from modules.operations import Operations
Op = Operations()
def test_summ():
    assert Op.Summ(2,3) == 5
def test_diff():
    assert Op.Diff(5,2) == 3
def test_comp():
    assert Op.Composition(10,2) == 20
def test_div():
    assert Op.Division(20,10) == 2

