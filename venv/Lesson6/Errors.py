try:
    print("start")
    print(10 / 0)
    print("pon")
except ZeroDivisionError as error:
    print(error)
else:
    print("else")
finally:
    print("finally")

print("code")