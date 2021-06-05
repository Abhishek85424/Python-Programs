arr = [900,1000,1100,1200,1300,1400,1500,1600,1700,1800]
dept = [910,1010,1110,1210,1310,1410,1510,1810,1710,1810]
arr_index = 1
dept_index = 0
max_platform = 1
current_platform = 1
prev_train_dept = 0
while arr_index < len(arr) and dept_index < len(dept):
    if prev_train_dept < arr[arr_index] and prev_train_dept != 0:
        current_platform = current_platform - 1
        prev_train_dept = 0
        dept_index = dept_index + 1
    elif arr[arr_index] <= dept[dept_index]:
        current_platform = current_platform + 1
        if current_platform > 1:
            prev_train_dept = dept[arr_index]
        arr_index = arr_index + 1
    else:
        current_platform = current_platform - 1
        dept_index = dept_index + 1
    if max_platform < current_platform:
        max_platform = current_platform
print(max_platform)


