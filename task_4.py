"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""
S=int(input("Введите общее количество журавликов: "))
if S%6==0:
    a=S//6
    b=S//6*2*2
    print(f"{S} -> {a} {b} {a}")
else: print ("Изготовлены не целые журавлики)))")
