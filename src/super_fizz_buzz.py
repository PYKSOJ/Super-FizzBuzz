def super_fizz_buzz(number):
    symbol = []
    if number % 3 == 0 :
        symbol.append('Fizz')
        if number % 9 == 0:
            symbol.append('Fizz')
            if number % 25 == 0:
                symbol.append('BuzzBuzz')
        elif number % 5 == 0:
            symbol.append('Buzz')
    elif number % 5 == 0 :
        symbol.append('Buzz')
        if number % 25 == 0:
            symbol.append('Buzz')
    else:
        symbol = ['NoFizzBuzz']
    tmp = ''.join(map(str, symbol))
    
    return (tmp)
# def super_fizz_buzz(number):
#     symbol = []
#     if number % 9 == 0 and number % 25 == 0 :
#         symbol.append('FizzFizzBuzzBuzz')
#     elif number % 3 == 0 and number % 5 == 0 :
#         symbol.append('FizzBuzz')
#     elif number % 9 == 0 :
#         symbol.append('FizzFizz')
#     elif number % 3 == 0 :
#         symbol.append('Fizz')
#     elif number % 25 == 0 :
#         symbol.append('BuzzBuzz')
#     elif number % 5 == 0 :
#         symbol.append('Buzz')
#     else:
#         symbol.append('NoFizzBuzz')
#     tmp = ''.join(map(str, symbol))
#     return(tmp)
