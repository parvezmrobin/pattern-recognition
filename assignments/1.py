from math import inf

true, false, null = True, False, None


def main():
    data = {
        1: 'A', 2: 'A', 3: 'A', 4: 'A', 5: 'A', 6: 'A', 7: 'A', 8: 'A', 9: 'A', 10: 'A',
        11: 'B', 12: 'B', 13: 'B', 14: 'B', 15: 'B', 16: 'B', 17: 'B', 18: 'B', 19: 'B', 20: 'B',
    }

    min_divider, max_divider = null, null
    min_accuracy = inf
    max_accuracy = -1
    for x in data:
        mis_calculate = 0
        for val, cls in data.items():
            if val < x and cls == 'B':
                mis_calculate += 1
            elif val >= x and cls == 'A':
                mis_calculate += 1

        accuracy = 1 - (mis_calculate / len(data))
        if accuracy < min_accuracy:
            min_accuracy = accuracy
            min_divider = x
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            max_divider = x

    if (1 - min_accuracy) > max_accuracy:
        max_accuracy = 1 - min_accuracy
        max_divider = min_divider

    print("{} can classify with {}\% accuracy.".format(max_divider, int(max_accuracy * 100)))


main()
