try:
    num=20
    den=int(input("enter denominator:"))
    print(num/den)

except ZeroDivisionError as e:
    print("den cant be zero:")
except ValueError as e:
    print("only integers")
