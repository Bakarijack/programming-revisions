student = {'bakari':25,'Kilu':26}

def test(student):
    new = {'Mtua':27}
    student.update(new)
    #student = {'Mtua':27}
    print("Inside the function : ",student)
    return
test(student)
print("Outside the function : ",student)