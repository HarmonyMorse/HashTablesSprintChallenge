def get_indices_of_item_weights(weights, length, limit):
    table = {}

    for i in range(0, length):
        if weights[i] in table:
            table[weights[i]].append(i)
        else:
            table[weights[i]] = [i]

    for weight in weights:
        temp = limit - weight
        if temp in table:
            if temp * 2 == limit and len(table[weight]) > 1:
                return table[weight][1], table[weight][0]
            else:
                return table[temp][0], table[weight][0]
