"""Cognitive Calculator... TBD: describe the features By: Rodrigo Hurtado Molero
   - operator: add, sub, mul, div, avg
   - operands: list of numbers
"""

def main(args):
    op = args['operator']
    operands = args['operands']
    result = 0
    status = 'ok'
    if op == 'add':
        result = add(operands)
    elif op == 'sub':
        result = sub(operands)
    elif op == 'mul':
        result = mul(operands)
    elif op == 'div':
        result = div(operands)
    elif op == 'avg':
        result = avg(operands)
    else:
        status = 'Unsupported operation. Please try: add, sub, mul or div'
    #cload function retunrs a dictionary
    return {"value" : result, "status": status}    
    
def add(operands):
    """Adds the list of numbers supplied as arguments"""
    result = 0
    for num in operands:
        result += float(num)
    return result

def sub(operands):
    """Subtracts the list of numbers supplied as arguments"""
    result = None
    for num in operands:
        if result == None:
            result = float(num)
        else:
            result -= float(num)
    return result

def mul(operands):
    """Multiply the list of numbers supplied as arguments"""
    result = 1
    for num in operands:
        result *= float(num)
    return result

def div(operands):
    """Divides the list of numbers supplied as arguments"""
    result = None
    for num in operands:
        if result == None:
            result = float(num)
        else:
            result /= float(num)
    return result

def avg(operands):
    """Average the list of numbers supplied as arguments"""
    sumOfOperands = 0
    numberOfOperands = len(operands)
    for num in operands:
        sumOfOperands += float(num)
    result = float(sumOfOperands/numberOfOperands)
    return result