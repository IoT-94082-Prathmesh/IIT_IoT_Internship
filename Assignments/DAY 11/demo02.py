
import numpy as np

def function1():
    arr = np.array([11, 22, 33, 44, 55, 66, 77, 88])

    print(f"arr = {arr}")
    print(f"len(arr) = {len(arr)}")

#function1()

def function2():
    arr = np.array([11, 22, 33, 44, 55, 66, 77, 88])

    print(f"arr = {arr}")
    print(f"arr[0] = {arr[0]}")
    print(f"arr[1] = {arr[1]}")
    print(f"arr[2] = {arr[2]}")
    print(f"arr[-1] = {arr[-1]}")
    print(f"arr[-2] = {arr[-2]}")
    print(f"arr[3:6] = {arr[3:6]}")

#function2()

def function3():
    arr = np.array([11, 22, 33, 44, 55, 66, 77, 88])

    print("Before reshape : ")
    print(f"NDIM = {arr.ndim}")
    print(f"SHAPE = {arr.shape}")
    print(f"arr = {arr}")

    arr = arr.reshape([4,2])

    print("After reshape : ")
    print(f"NDIM = {arr.ndim}")
    print(f"SHAPE = {arr.shape}")
    print(f"arr = {arr}")

function3()