input_var = int(input("Please input the year: 👇️_✅- "))

# Leap year logic:
# 1. Year divisible by 4 → possible leap year
# 2. But if divisible by 100 → not a leap year
# 3. Unless also divisible by 400 → then it's a leap year

if (input_var % 4 == 0 and input_var % 100 != 0) or (input_var % 400 == 0):
    print(input_var, "is a leap year.")
else:
    print(input_var, "is not a leap year.")
