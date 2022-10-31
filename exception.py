my_list = []
# ✅ Ignore any exception
try:
    print(my_list[100])
except:
    # 👇️ this runs
    pass
# ✅ Ignore only IndexError exceptions
try:
    print(my_list[100])
except IndexError:
    # 👇️ this runs
    pass