A = [
    0.80, 0.91, 0.93, 0.95, 1.32, 1.53, 1.57, 1.63, 1.67, 1.74,
    2.01, 2.18, 2.27, 2.31, 2.40, 2.61, 2.64, 2.64, 2.67, 2.85,
    2.96, 2.97, 3.17, 3.17, 3.38, 3.67, 3.73, 3.83, 3.99, 4.06,
    4.10, 4.12, 4.18, 4.20, 4.23, 4.27, 4.27, 4.39, 4.40, 4.46,
    4.47, 4.61, 4.64, 4.89, 4.96, 5.12, 5.15, 5.33, 5.33, 5.47,
    5.64, 5.85, 5.99, 6.29, 6.42, 6.53, 6.70, 6.78, 7.18, 7.22
]

B = [
    3.54, 3.88, 4.24, 4.30, 4.30, 4.70, 4.75, 4.97, 5.21, 5.42,
    5.60, 5.77, 5.87, 5.94, 5.95, 6.04, 6.05, 6.15, 6.19, 6.21,
    6.33, 6.41, 6.43, 6.49, 6.52, 6.58, 6.60, 6.63, 6.65, 6.75,
    6.90, 6.92, 7.03, 7.08, 7.18, 7.29, 7.33, 7.41, 7.41, 7.46,
    7.61, 7.67, 7.68, 7.68, 7.78, 7.96, 8.03, 8.12, 8.20, 8.22,
    8.33, 8.36, 8.44, 8.45, 8.49, 8.75, 8.76, 9.14, 9.20, 9.86
]

query_val = 7.5

BIN_SIZE = 1
TOTAL_SAMPLE = len(A) + len(B)
minimum, maximum = 0, 10

bin_A = [0] * 10
bin_B = [0] * 10

bin_i = 0
bin_max = 1
for a in A:
    if a >= bin_max:
        bin_max += BIN_SIZE
        bin_i += 1
    bin_A[bin_i] += 1

bin_i = 0
bin_max = 1
for b in B:
    if b >= bin_max:
        bin_max += BIN_SIZE
        bin_i += 1
    bin_B[bin_i] += 1

query_bin = int((query_val - minimum) / BIN_SIZE)
p_query_given_A = bin_A[query_bin] / (len(A) * BIN_SIZE)
p_query_given_B = bin_B[query_bin] / (len(B) * BIN_SIZE)
p_A = len(A) / TOTAL_SAMPLE
p_B = len(B) / TOTAL_SAMPLE

p_query_and_A = p_query_given_A * p_A
p_query_and_B = p_query_given_B * p_B

p_A_given_query = p_query_and_A / (p_query_and_A + p_query_and_B)
p_B_given_query = 1 - p_A_given_query

print("Probality of {} belongs to A is {}.".format(query_val, p_A_given_query))
