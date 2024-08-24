# exception = events detected during execution that interrupt the flow of a program


try :
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divided by: "))
    total = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can;t divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only Number please")
else:
    print(total)
finally:
    print("this is always execute")