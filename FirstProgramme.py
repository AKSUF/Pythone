a=0
b=2
try:
  print("resource open")
  print(a/b)
  k=int(input("Enter a number"))
  print(k)
except ZeroDivisionError as e:
    print("Hey,you can not divide a number")
except ValueError as e:
    print("Invalid input")
except Exception as e:
  print("Hey ,you can not divide a Number by Zero",e)
finally:
    print("resource closed")




