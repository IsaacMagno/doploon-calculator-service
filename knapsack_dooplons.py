def knapsack(items, capacity):
    n = len(items)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if items[i - 1][0] <= j:
                table[i][j] = max(table[i - 1][j], table[i][j - items[i - 1][0]] + items[i - 1][1])
            else:
                table[i][j] = table[i - 1][j]
    
    result = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            result.append(items[i - 1])
            j -= items[i - 1][0]
        else:
            i -= 1
    
    return result