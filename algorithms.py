import itertools

def bruteForceSolver(items:dict, capacity: int) -> tuple[int, list[int]]:
      """
    Solves the knapsack problem using brute force method.

    Args:
        items (dict): Dictionary where keys are item IDs and values are dictionary with 'value' and 'weight' keys.
            Example: {0: {'value': 60, 'weight': 10}, ...}

        capacity (int): Maximum weight capacity of the knapsack.

    Returns:
        tuple[int, list[int]]: A tuple containing maximum total value achievable and list of item IDs included in the optimal solution
    """
    itemIds = list(items.keys())
    n = len(items)

    bestValue = 0
    bestCombination = [] 
    for size in range(1, n+1):
        for subset in itertools.combinations(itemIds, size):
            totalWeight = sum(items[i]['weight'] for i in subset)
            totalValue = sum(items[i]['weight'] for i in subset)

            if totalWeight <= capacity and totalValue > bestValue:
                bestValue = totalValue
                bestCombination = list(subset)

    return bestValue, bestCombination

def dynamicSolver(items:dict, capacity:int) -> tuple[int, list[int]]:
    """
    Solves the knapsack problem using dynamic programing.

    Args:
        items (dict): Dictionary where keys are item IDs and values are dictionary with 'value' and 'weight' keys.
            Example: {0: {'value': 60, 'weight': 10}, ...}

        capacity (int): Maximum weight capacity of the knapsack.

    Returns:
        tuple[int, list[int]]: A tuple containing maximum total value achievable and list of item IDs included in the optimal solution
    """
    n = len(items)
    # make the dp array
    dp = [0] * (capacity + 1)

    itemIds = list(items.keys())

    itemsTaken = [[False]*(capacity+1) for _ in range (n+1)]

    # take first n elements
    for i in range(1, n+1):
        itemId = itemIds[i-1]
        value = items[itemId]['value']
        weight = items[itemId]['weight']
        for w in range(capacity, weight - 1, -1):
            if w >= weight and dp[w] < dp[w - weight] + value:
                dp[w] = dp[w - weight] + value
                itemsTaken[i][w] = True
            else:
                itemsTaken[i][w] = itemsTaken[i-1][w]

    # check which items were used
    restoredItems = []
    w = capacity
    for i in range(n, 0, -1):
        if itemsTaken[i][w]:
            itemId = itemIds[i-1]
            restoredItems.append(itemId)
            w -= items[itemId]['weight']

    return dp[capacity], restoredItems[::-1]
