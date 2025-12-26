
import numpy as np

def function1():
    arr = np.arange(0,10)
    print(f"arr = {arr}")

#function1()

def function2():
    arr = np.arange(11, 21)
    print(f"arr = {arr}")

#function2()

def function3():
    arr = np.arange(11, 21, 2)
    print(f"arr = {arr}")

#function3()

def function4():
    zeros = np.zeros(5)
    print(f"zeros = {zeros}")

    ones = np.ones(10)
    print(f"ones = {ones}")

#function4()

def function5():
    random1 = np.random.random(5)
    print(f"random = {random1}")

    random2 = np.random.randint(1, 10, 4)
    print(f"random = {random2}")

#function5()


def function6():
    arr1 = np.array([10, 20, 30, 40])
    arr2 = np.array([11, 22, 33, 44])

    arr = arr1 + arr2

    print(f"arr = {arr}")
    print(f"type = {type(arr)}")

#function6()

def function7():
    arr = np.array([10, 20, 30, 40])

    print(f"arr * 5 = ", arr * 5)

function7()