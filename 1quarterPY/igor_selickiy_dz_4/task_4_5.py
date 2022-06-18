import sys

from utils import currency_rates

if len(sys.argv) == 1:
    print('Please write Currency')
elif len(sys.argv) == 2 or 3:
    if len(sys.argv[1]) != 3:
        print('wrong input')
    elif len(sys.argv) == 3 and sys.argv[2] == 'cool':
        print(currency_rates(code=sys.argv[1], cool_vision=True))
    else:
        print(currency_rates(sys.argv[1]))

