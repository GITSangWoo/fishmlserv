from fishmlserv.curl import ans_get

def test_get():
    r = ans_get(10, 10)
    assert r == "빙어"
