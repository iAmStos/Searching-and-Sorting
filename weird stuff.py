import copy
import matplotlib

array = [1,2,3,4,5,6,7,8,9]
array_2 = copy.deepcopy(array)

array.append(10)

print(array)
print(array_2)