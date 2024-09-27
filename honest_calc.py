from decimal import Decimal

msg_ = (
    'Enter an equation',
    'Do you even know what numbers are? Stay focused!',
    'Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?',
    'Yeah... division by zero. Smart move...',
    'Do you want to store the result? (y / n):',
    'Do you want to continue calculations? (y / n):',
    ' ... lazy',
    ' ... very lazy',
    ' ... very, very lazy',
    'You are',
    'Are you sure? It is only one digit! (y / n)',
    'Don\'t be silly! It\'s just one number! Add to the memory? (y / n)',
    'Last chance! Do you really want to embarrass yourself? (y / n)'
)


def int_or_float(user_input):
    """Return True if string is natural or decimal number, False otherwise."""
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def calculate(num1: float, operator: str, num2: float) -> float or str:
    """Return float calculation of 2 float numbers with string operator.

    Return 'Division by Zero' if second float number is zero.
    """
    if operator == '/' and num2 == 0.0:
        return 'Division by Zero'
    elif operator == '+':
        return float(Decimal(str(num1)) + Decimal(str(num2)))
    elif operator == '-':
        return float(Decimal(str(num1)) - Decimal(str(num2)))
    elif operator == '*':
        return float(Decimal(str(num1)) * Decimal(str(num2)))
    elif operator == '/':
        return float(Decimal(str(num1)) / Decimal(str(num2)))


def is_one_digit(num):
    """Return True if float num is a natural number, return False otherwise."""
    return (lambda x: True if 10 > x > -10 and x.is_integer() else False)(num)


def check(num1, num2, operator):
    """According to values float numbers and string operator print message to user."""
    msg = ''
    if is_one_digit(num1) and is_one_digit(num2):
        msg += msg_[6]
    if (num1 == 1.0 or num2 == 1.0) and operator == '*':
        msg += msg_[7]
    if (num1 == 0.0 or num2 == 0.0) and (operator == '*' or operator == '+' or operator == '-'):
        msg += msg_[8]
    if msg != '':
        msg = msg_[9] + msg
        print(msg)


def main():
    """Control flow for calculations.

    Return value:
    Empty string, end of calculations.
    """
    memory = 0
    while True:
        calc = input(f'{msg_[0]}\n')
        x, oper, y = calc.split()
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        if int_or_float(x) is False or int_or_float(y) is False:
            print(msg_[1])
            continue
        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            check(float(x), float(y), oper)
            result = calculate(float(x), oper, float(y))
            if result == 'Division by Zero':
                print(msg_[3])
                continue
            print(result)
            store_result = ''
            while store_result != 'y' and store_result != 'n':
                store_result = input(f'{msg_[4]}\n')
                if store_result == 'y':
                    msg_index = 0
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            response = input(f'{msg_[msg_index]}\n')
                            if response == 'y':
                                if msg_index < 12:
                                    msg_index += 1
                                else:
                                    memory = result
                                    break
                            elif response == 'n':
                                break
                            else:
                                continue
                    elif not is_one_digit(result) or not msg_index < 12:
                        memory = result
            continue_calc = input(f'{msg_[5]}\n')
            if continue_calc == 'y':
                continue
            elif continue_calc == 'n':
                break
        else:
            print(msg_[2])
    return ''


if __name__ == '__main__':
    main()
