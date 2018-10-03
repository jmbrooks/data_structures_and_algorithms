# -*- coding: utf-8 -*-
from linear_data_structures import Stack


def balance_parentheses(parentheses_string: str) -> bool:
    """Takes parentheses string input and outputes True if parentheses are balanced."""
    stack = Stack()
    for character in parentheses_string:
        if character == '(':
            stack.push(character)
        elif character == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                return False
        else:
            print("invalid character, all characters must be either ( or ).")
            break

    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    ex_one = '(()()())'
    ex_two = '()((()))'
    ex_three = '())'
    ex_four = '('

    print(balance_parentheses(ex_one))
    print(balance_parentheses(ex_two))
    print(balance_parentheses(ex_three))
    print(balance_parentheses(ex_four))
