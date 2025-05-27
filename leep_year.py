year = int(input("Please input the year: 👇️_✅- "))

# Leap year logic:
# 1. Year divisible by 4 → possible leap year
# 2. But if divisible by 100 → not a leap year
# 3. Unless also divisible by 400 → then it's a leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
