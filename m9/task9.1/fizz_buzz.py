def get_reply(number):
    if number%3 == 0:
        if number%5 == 0: return 'FizzBuzz'
        else: return 'Fizz'
    elif number%5 == 0: return 'Buzz'
