from file import return_hi
def test_func():
    assert return_hi() == "hi"
    print("test passed")
    
    
test_func()