# Error Handling:
# try (try something that might cause an error)
# except (do this if there was an error)
# else (do this if there were no errors)
# finally (do this no matter what)

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "Value"}
    print(a_dictionary['asdasd'])
except FileNotFoundError:
    print("There was a file not found error. Creating file.")
    file = open("a_file.txt", mode="w")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
else:
    print("There were no errors")
finally:
    print("Finishing Program")
    file.close()

height = float(input("Height in meters: "))
weight = int(input("Weight in kg: "))

if height > 3:
    raise ValueError("Height shouldn't be more than 3m")

bmi = weight / height ** 2
print (f"BMI is {bmi}.")
