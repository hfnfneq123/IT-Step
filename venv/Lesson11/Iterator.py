my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))

\\-------------

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)

for elem in count:
    print(elem)

\\-------------

def raise_to_the_degree(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_to_the_degree(2, 50)
print(res)

for _ in res:
    print(_)

\\-------------

def my_decorator(func):
    def wrapper():
        func()
        print("Start decorator")
        print("End decorator")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()