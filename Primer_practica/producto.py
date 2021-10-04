def myFunction (num1,num2,num3,num4):
    mul = num1*num2*num3*num4
    print(mul)


ingreso1 = int(input('Ingrese el primer numero: '))
ingreso2 = int(input('Ingrese el segundo numero: '))
ingreso3 = int(input('Ingrese el tercero numero: '))
ingreso4 = int(input('Ingrese el cuarto numero: '))

print(ingreso1," X ",ingreso2," X ",ingreso3," X ",ingreso4,"=", end=' ')
myFunction(ingreso1,ingreso2,ingreso3,ingreso4)