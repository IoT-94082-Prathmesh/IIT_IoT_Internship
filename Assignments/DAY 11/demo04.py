
import pandas as pd
import numpy as np
def function1():
    l1 = [11, 22, 33, 44, 55]
    print(f"l1 = {l1}, type = {type(l1)}")

    arr = np.array([11, 22, 33, 44, 55])
    print(f"arr = {arr}, type = {type(arr)}")

    series = pd.Series([11, 22, 33, 44, 55])
    print(f"series = {series}, type = {type(series)}")

#function1()

def function2():
    series = pd.Series([11, 22, 33, 44, 55])
    print(series)

    print(f"Type = {type(series)}")
    print(f"Dtype = {series.dtype}")
    print(f"Size = {series.size}")
    print(f"NDIM = {series.ndim}")
    print(f"NBYTES = {series.nbytes}")
    print(f"Shape = {series.shape}")
    
#function2()

def function3():
    n_series = pd.Series([11, 22, 33, 44, 55, 66])

    print(f"keys = {n_series.keys()}")
    print(f"values = {n_series.values}")

#function3()

def function4():
    s1 = pd.Series({"name":"abc", "rollno":12, "marks":98.5})

    print(s1)
    print(f"s1['name'] = {s1['name']}")
    #print(f"s1[0] = {s1[0]}")

#function4()

def function5():
    studs = pd.Series(["s1", "s2", "s3", "s4", "s5"])
    marks = pd.Series([24, 21, 25, 23, 22])

    print(studs)
    print(marks)

#function5()

def function6():
    studs = pd.Series(["s1", "s2", "s3", "s4", "s5"])
    marks = pd.Series([24, 21, 25, 23, 22], index=studs)

    print(marks)    

function6()