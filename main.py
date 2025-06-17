import sys
import cmd

# Application-specific modules import
import algorithms

def getInputInRange(prompt, start=0, end=None) -> int:
    """
    Prompts the user for an integer input within a specified range.
    Args:
        prompt (str): Message to be displayed
        start (int, optional): Minimum acceptable value (inclusive) - default is 0.
        end (int, optional): Maximum acceptable value. If None, no limit is enforced

    Returns:
        int: Integer input provided by the user

    Raises:
        ValueError: If start is greater than or equal to end when both are specified.
    """
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
    """
    Prompts the user to enter 'value' and 'weight' for n items.
    Args:
        n (int): Number of items to be entered.

    Returns:
        dict: A dictionary of items where keys are item IDs and values are dictionaries with 'value' and 'weight' keys.
            Example: {0: {'value': 60, 'weight': 10}, ...}
    
    Raises:
        ValueError: If n is less than or equal to zero.
    """
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
