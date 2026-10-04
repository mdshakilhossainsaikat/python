# type casting

num_string ='12'
num_integer = 23
print("Type after casting: ", type(num_string))

# string -> int
num_string = int(num_string)

print("Type after casting: ", type(num_string))

num_sum = num_integer + num_string
print("sum: ", num_sum)

# float -> int
print(int(2.3))

# int -> float
print(float(5))

# string -> complex
print(complex('3+5j'))