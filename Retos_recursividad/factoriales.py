def factorial_recusivo (n : int) :
    if(n > 0) :
        return n * factorial_recusivo (n - 1)
    else :
        return 1


n = 5 
n_fact = factorial_recusivo(n)

print(f'{n}! es {n_fact}')
