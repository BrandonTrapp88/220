def fibonacci(n):
    if n < 1:
        return None
    ticker = 0
    blank = [1,1]
    answer = 0
    while ticker <= n:
        answer = blank[ticker] +blank[ticker+1]
        blank.append(answer)
        ticker+=1
    return blank[n-1]



def double_investment(principle, rate):
    answer =principle
    years = 0
    while answer <= principle*2:
        answer = answer *(1+rate)

        years +=1
    return years

def syracuse(n):
    ticker = 0
    answer = 0
    number_list = [n]

    while number_list[-1] != 1:
        if number_list[ticker] % 2 == 0:
           answer = number_list[ticker]/2
           number_list.append(answer)
           ticker+=1
        elif number_list[ticker] % 2 ==1:
             answer = (3* number_list[ticker])+1
             number_list.append(answer)
             ticker+=1
    return number_list

def goldbach(n):
    number = 0
    new_number = 0

    ticker = 0
    num_list = []
    if n % 2 == 0:
        number = n - 2
        new_number = n - number
        num_list.append(number)
        num_list.append(new_number)
        return num_list
    else:
        return None





