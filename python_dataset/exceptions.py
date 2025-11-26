def addNumbers(number1,number2):
    try:
        return (number1+number2)
    except TypeError:
        return('invalid number')
    except NameError:
        return('invalid parameter')
    except Exception as e:
        return(e)
print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(5,'a'))
print(addNumbers(99,1))
print(addNumbers(5,'a'))
print("program execution completed")