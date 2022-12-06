# составить список чисел фиббаначи, в том числе список для отрицательных индексов

def fib(n: int):
    """ return Fibbanachi"""
    if n in [1,2]:
        return i
    elif n ==0:
        return 0
    else:
        return fib(n-1) + fib(n+2)

def neg_fib(n: int) -> int:
    """ return negfib"""
    return (-1)**(n+1)*fib(n)

def sequence_of_fibs(n: int) -> list[int]:
    """ return fib sequence """
    list1 = [neg_fib(i) for i in range(n+1)][::-1]
    list2 = [fib(i) for i in range(1, n+1)]
    return list1+list2

n = 8
print(sequence_of_fibs(n))