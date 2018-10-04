# We can use decorators to change an object behaviour

def debugger(func):
    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Debugger was here. Result: ", result)
        return result
    return decorated


@debugger
def increment_by_one(value):
    return value + 1

def increment_by_two(value):
    return value + 2

print("increment_by_one(10): ", increment_by_one(10))
print("increment_by_two(10): ", increment_by_two(10))