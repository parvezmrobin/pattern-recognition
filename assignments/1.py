from colorama import Fore

true, false, null = True, False, None


def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    B = [1, 9, 10, 11, 12, 13, 14, 15, 16]
    X = set(A + B)

    min_divider, max_divider = null, null
    min_mis_calc = A + B
    max_mis_calc = []
    for divider in X:
        mis_calculate = []
        for val in A:
            if val > divider:
                mis_calculate.append((val, 'A'))
        for val in B:
            if val <= divider:
                mis_calculate.append((val, 'B'))

        if len(mis_calculate) < len(min_mis_calc):
            min_mis_calc = mis_calculate
            min_divider = divider
        if len(mis_calculate) > len(max_mis_calc):
            max_mis_calc = mis_calculate
            max_divider = divider

    upside_down = false
    if (len(A + B) - len(max_mis_calc)) < len(min_mis_calc):
        upside_down = true
        min_divider = max_divider
        min_mis_calc = []
        A_with_class = [(val, 'A') for val in A]
        B_with_class = [(val, 'B') for val in B]
        for val in (A_with_class + B_with_class):
            if val not in max_mis_calc:
                min_mis_calc.append(val)

    accuracy = int(len(min_mis_calc) / len(A + B) * 100)
    summary = "{} can classify with {}% accuracy.".format(min_divider, accuracy)
    print(Fore.BLUE + summary + Fore.RESET)
    divisions = [">", min_divider, ">="] if upside_down else ["<", min_divider, "<="]
    print(Fore.GREEN + "A {} {} {} B".format(*divisions) + Fore.RESET)
    print("Misclassified: ", end='')
    for i, val in enumerate(min_mis_calc):
        print("({}: {})".format(*val), end='')
        if len(min_mis_calc) > 2 and i < len(min_mis_calc) - 2:
            print(', ', end='')
        elif i is len(min_mis_calc) - 2:
            print(' and ', end='')
    print('')


main()
