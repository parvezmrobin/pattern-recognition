"""
Given a list of numbers A and B
the assignment is to find a threshold t
such that A lies on the one side of t
and B lies on the other side, and t
minimizes the number of mis-classifications.
"""

from colorama import Fore

true, false, null = True, False, None


def main():
    # A = [1.3, -.5, 2.3, 5.1, 8.2, -.4, 10.5, 2.5, -4.2, -3.1, 1.7, 2.8, 4.6, 3.0, 10.1, 2.5, .8, 8.1, 2.7, -6.5, ]
    # B = [-2.7, -3.2, -5.4, -10.8, -1.1, -3.4, .7, -5.0, -7.1, -10.0]
    A = [1.3, -.5, 2.3, 5.1, 8.2, -.4, 10.5, 2.5, -4.2, -3.1, 1.7, 2.8, 4.6, 3.0, 10.1, 2.5, .8, 8.1, 2.7, -6.5, ]
    B = [-2.7, -3.2, -5.4, -10.8, -1.1, -3.4, .7, -5.0, -7.1, -10.0, .9, 1.2, -4.9, -6.2, 1.3, -1.9, -8.7, -7.4, .9,
         -10.3, ]
    # X is the set of probable dividers
    # This can be any value from A or B
    X = set(A + B)

    min_divider, max_divider = null, null
    min_mis_calc = A + B
    max_mis_calc = []

    A_with_class = [(val, 'A') for val in A]
    B_with_class = [(val, 'B') for val in B]
    Data = A_with_class + B_with_class
    for thresh in X:
        mis_calculate = []
        for val, cls in Data:
            # We assume, A is in lower side of thresh
            # and B is in the upper side
            # If any value doesn't follow this,
            # count it as mis-classification
            if (val > thresh and cls == 'A') or (val <= thresh and cls == 'B'):
                mis_calculate.append((val, cls))

        if len(mis_calculate) < len(min_mis_calc):
            min_mis_calc = mis_calculate
            min_divider = thresh
        if len(mis_calculate) > len(max_mis_calc):
            max_mis_calc = mis_calculate
            max_divider = thresh

    # Check if we can achieve better accuracy by
    # Putting A on the upper side and B on the lower
    upside_down = false
    if (len(Data) - len(max_mis_calc)) < len(min_mis_calc):
        upside_down = true
        min_divider = max_divider
        min_mis_calc = [x for x in Data if x not in max_mis_calc]

    # Show Accuracy
    accuracy = round(100 - (len(min_mis_calc) / len(Data) * 100), 2)
    summary = "{} can classify with {}% accuracy.".format(min_divider, accuracy)
    print(Fore.BLUE + summary + Fore.RESET)
    # Show decision regions
    divisions = [">", min_divider, ">="] if upside_down else ["<", min_divider, "<="]
    print(Fore.GREEN + "A {} {} {} B".format(*divisions) + Fore.RESET)
    # Show mis-classifications
    print(Fore.RED + "Misclassified: " + Fore.RESET, end='')
    for i, x in enumerate(min_mis_calc):
        print("({}: {})".format(*x), end='')
        if len(min_mis_calc) > 2 and i < len(min_mis_calc) - 2:
            print(', ', end='')
        elif i is len(min_mis_calc) - 2:
            print(' and ', end='')
    print('')


main()
