def sumar(num1, num2):
    return num1+num2
def restar(num1, num2):
    return num1-num2

def multi(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        return num1/ num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")