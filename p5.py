n=int(input())
def odd_even(n):
    if n>0:
        return 'positive'
    elif n<0:
        return 'negative'
    else:
        return 'zero'

print(odd_even(n))