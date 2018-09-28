"""
Naive Bayes classification using histogram
"""

A = [
    21.5473, 27.0135, 29.8611, 35.4697, 36.8878, 38.0212, 39.4082, 41.1395, 45.5574, 49.0956, 51.6582,
    52.6409, 53.0567, 53.1624, 53.4761, 55.8833, 57.1591, 63.8259, 64.2501, 65.4979, 65.7157, 69.4580,
    81.0208, 81.5276, 84.7873, 85.7744, 89.0037, 91.1380, 91.4641, 93.8168, 93.9471, 96.0843, 96.0848,
    100.0858, 105.1627, 108.3613, 110.8800, 117.6647, 117.9848, 118.4360, 121.2917, 125.8570, 128.0077,
    129.2932, 135.8174, 139.2352, 140.8043, 141.4214, 144.7079, 144.7667
]

B = [
    25.6024, 34.8757, 35.1628, 35.8968, 35.9767, 38.8649, 41.0315, 42.6889, 43.8441, 43.9201, 44.8091,
    46.0837, 46.5343, 48.6401, 48.9080, 54.7670, 56.1891, 56.1938, 58.7832, 59.1863, 59.2944, 65.4580,
    70.6238, 76.9717, 77.2350, 81.0838, 82.5482, 83.5704, 91.7224, 93.7093, 94.9845, 96.4818, 100.3616,
    103.2577, 105.8672, 110.0303, 114.5979, 122.2597, 125.7384, 128.2570, 129.0089, 131.2494, 132.3562,
    135.8940, 137.9303, 138.0080, 143.3842, 143.7339, 150.0468, 154.4975
]

A = sorted(A)
B = sorted(B)

BIN_SIZE = 10
TOTAL_SAMPLE = len(A) + len(B)
minimum, maximum = 20, 160

bin_A = [0] * 14
bin_B = [0] * 14

bin_i = 0
bin_max = minimum + BIN_SIZE
for a in A:
    if a >= bin_max:
        bin_max += BIN_SIZE
        bin_i += 1
    bin_A[bin_i] += 1

bin_i = 0
bin_max = minimum + BIN_SIZE
for b in B:
    if b >= bin_max:
        bin_max += BIN_SIZE
        bin_i += 1
    bin_B[bin_i] += 1

for query_val in [55, 101, 136]:
    query_bin = int((query_val - minimum) / BIN_SIZE)
    p_query_given_A = bin_A[query_bin] / (len(A) * BIN_SIZE)
    p_query_given_B = bin_B[query_bin] / (len(B) * BIN_SIZE)
    p_A = len(A) / TOTAL_SAMPLE
    p_B = len(B) / TOTAL_SAMPLE

    p_query_and_A = p_query_given_A * p_A
    p_query_and_B = p_query_given_B * p_B

    p_A_given_query = p_query_and_A / (p_query_and_A + p_query_and_B)
    p_B_given_query = 1 - p_A_given_query

    if p_A_given_query > p_B_given_query:
        print("Probability of {} belongs to A is {:.2f}.".format(query_val, p_A_given_query))
    elif p_A_given_query < p_B_given_query:
        print("Probability of {} belongs to B is {:.2f}.".format(query_val, p_B_given_query))
    else:
        print("Probability of {} belonging to each class is same.".format(query_val))
