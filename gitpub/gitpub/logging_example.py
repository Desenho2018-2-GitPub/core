from logging import debug

@debug
def increment_by_one(value):
    return value + 1

@debug
def increment_by_two(value):
    return value + 2

@debug
def sum_multiple_objects(*args, **kwargs):
    result = args[0]
    for each in args[1:]:
        result += each

    return result

increment_by_one(10)
increment_by_one(11)
increment_by_one(12)

increment_by_two(10)
increment_by_two(120)
increment_by_two(1330)

sum_multiple_objects(19, 20, 21)
sum_multiple_objects(19, 21, 24, 23)
sum_multiple_objects("This ", "is ", "an ", "example" )