from new_package.preprocessing import num_change, need_help

def test_num_change():
    assert type(num_change(10.5 + 11.2)) == int

def test_need_help():
    assert need_help('test') == 'Good luck!'
