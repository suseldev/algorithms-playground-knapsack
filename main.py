import sys
import cmd

# Application-specific modules import
import algorithms

def getInputInRange(prompt, start=0, end=None) -> int:
    if not end is None and start >= end:
        raise ValueError("Range beginning cannot be larger than its end!")
    givenInput = input(prompt)
    try:
        givenInput = int(givenInput)
        if givenInput < start:
            raise ValueError("Input too small")
        if not (end is None) and givenInput > end:
            raise ValueError("Input too large")
        return givenInput
    except ValueError as e:
        print(f"Invalid input: {e}")
        return getInputInRange(prompt, start=start, end=end)

def promptItems(n) -> dict:
    itemList = {}
    if n <= 0:
        raise ValueError("Invalid items count!")
    for i in range(n):
        print(f"Item {i}: ")
        value = getInputInRange("value > ")
        weight = getInputInRange("weight > ")
        itemList[i] = {'weight': weight, 'value': value}
    return itemList

def main():
    # Sorry, too lazy to use argparse :p 
    if len(sys.argv) != 2 or sys.argv[1] not in ['--dynamic', '--bruteforce']:
        print(f"Usage: python3 {sys.argv[0]} [--dynamic | --bruteforce]")
        sys.exit(1)

    solveUsingDynamic = sys.argv[1] == '--dynamic'

    n = getInputInRange("n (items count) > ") 
    items = promptItems(n)
    capacity = getInputInRange("Backpack capacity > ")

    if(solveUsingDynamic):
        maxValue, itemsId = algorithms.dynamicSolver(items, capacity)
    else:
        maxValue, itemsId = algorithms.bruteForceSolver(items, capacity)

    print(f'== SOLUTION == \nMax value: {maxValue}\nTaken items: {itemsId}')

if __name__ == "__main__":
    main()
