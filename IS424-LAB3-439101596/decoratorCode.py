



x = int(input("Enter a number of repetitions: "))

def repeat_call(f):
    def wrapper():
        for _ in range(x):
            f()
    return wrapper

@repeat_call
def hello():
    print('Hello')

hello()



