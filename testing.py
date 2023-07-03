# Testing
# We can lots of errors- we eant to test to save time and money
# types of test:
# functional tests = unit tests/ integration testing/ user-acceptance testing.
# non -functional performance, scalaibity, usuability. 
# pytest
# pip install pytest

#def func(num):
#    return num * 2

#def test_answer(): # name the test test_.....
#    assert func(6) == 12



def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1 
    return sum 

def test_count_int():
    assert count([1,2,2,4,5,2],2) == 3
    assert count([],2) == 0
    assert count([99, 88, 77, 206, 77], 77) == 2

def test_count_str():
    assert count(["apple", "orange", "apple", "apple"], "apple") == 3
    assert count (["apple", "apple", "orange"], "pear") == 0