# 1: Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

spam = 9
try:
    assert spam > 9
except AssertionError:
    print ("Assertion (1) was triggered")


# 2: Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings 
#    that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered 
#    the same, and 'goodbye' and 'GOODbye' are also considered the same).

eggs = "Hello, World!"
bacon = "HeLlO, wORlD!"


try:
    if isinstance(eggs, str) and isinstance(bacon, str):                                # check if they are a both containing strings, though 
        assert (not (bacon.lower() == eggs.lower()))                                    # .lower() would trigger an error if it wasn't a string
except AssertionError:
    print ("Assertion (2) was triggered")


# 3: Write an assert statement that always triggers an AssertionError.

assert False