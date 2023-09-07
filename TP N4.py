#Ejercicio 1
x = 0

while x < 30:
    if x == 15:
        print(f'The execution of the loop was broken when x was {x}.')
        break
    elif x == 4 or x==6 or x==10:
        print(f'The value {x} of x was skipped')
        x+=1
        continue
    else :
        print(x)
    x+=1
