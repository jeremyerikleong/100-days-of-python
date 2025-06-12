import random
import test_module

random_integer = random.randint(1, 10)
print(random_integer)
print("test module", test_module.testing_number)

# print Head or Tail
result = random.random()

if result >= 0.5:
    print("Head")
else:
    print("Tail")