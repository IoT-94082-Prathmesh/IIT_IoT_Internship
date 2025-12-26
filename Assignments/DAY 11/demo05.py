
import pandas as pd

def function1():
    p1 = {"name":"abc", "age":23, "address":"pune"}
    p2 = {"name":"xyz", "age":34, "address":"mumbai"}
    p3 = {"name":"pqr", "age":21, "address":"delhi"}

    s1 = pd.Series(p1)
    s2 = pd.Series(p2)
    s3 = pd.Series(p3)

    print(s1)
    print(s2)
    print(s3)

#function1()

def function2():
    p1 = {"name":"abc", "age":23, "address":"pune"}
    p2 = {"name":"xyz", "age":34, "address":"mumbai"}
    p3 = {"name":"pqr", "age":21, "address":"delhi"}

    s1 = pd.Series(p1)
    s2 = pd.Series(p2)
    s3 = pd.Series(p3)

    df = pd.DataFrame([s1, s2, s3])
    print(df)

function2()