class UnnecessaryError(Exception):
    pass


def i_just_throw_an_exception():
    value = 1
    def some_inner_function(value):
        value += 1

    print("I don't know what you were expecting")
    # raise UnnecessaryError("You actually called this function...")
