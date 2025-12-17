# List of List

def function1():
    l1 = [
        [1, 2, 3, 4],
        [10, 20, 30, 40],
        [11, 22, 33, 44]
    ]

    #print(l1)

    #for l in l1:
    #    print(l)

    print("l1 :")
    for l in l1:
        for e in l:
            print(e, end=" ")
        print("")

#function1()

def function2():
    students = [
        [12, "abc", 98.5],
        [10, "xyz", 87.6],
        [13, "mno", 90.0]
    ]

    #print(students)
    
    #for student in students:
    #    print(student)

    #for student in students:
    #    print(f"rollno = {student[0]}, name = {student[1]}, marks = {student[2]}")

    for rollno, name, marks in students:
        print(f"rollno = {rollno}, name = {name}, marks = {marks}")

function2()
