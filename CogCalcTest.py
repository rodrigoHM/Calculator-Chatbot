import CogCalc

result = CogCalc.main({"operator":"add", "operands":['2','3','5']})
print(f"2 + 3 + 5 = {result['value']} with status {result['status']}")

result = CogCalc.main({"operator":"sub", "operands":['10','3','4']})
print(f"10 - 3 - 4 = {result['value']} with status {result['status']}")

result = CogCalc.main({"operator":"div", "operands":['16','2','2']})
print(f"16 / 2 / 2 = {result['value']} with status {result['status']}")

result = CogCalc.main({"operator":"mul", "operands":['16','2','2']})
print(f"16 * 2 * 2 = {result['value']} with status {result['status']}")

result = CogCalc.main({"operator":"avg", "operands":['300','15','15']})
print(f"average is = {result['value']} with status {result['status']}")