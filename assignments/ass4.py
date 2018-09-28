"""
Adaptive Decision Boundary
"""
true, false, null = True, False, None


def same_sign(val1, val2):
    if val1 < 0 and val2 < 0:
        return true
    if val1 >= 0 and val2 >= 0:
        return true
    return false


train_set = [
    (0, 0, 0, 1),
    (2, 1, 1, 1),
    (2, -1, 1, 1),
    (1, 2, -1, -1),
    (3, 2, 2, -1),
    (2, 3, -3, -1),
    (3, -3, 2, -1),
]
w = [0, 0, 0, 0]
c, k = 1, 1

t = 0
while true:
    has_error = false
    for i, x in enumerate(train_set):
        t += 1
        D = w[0] + w[1] * x[0] + w[2] * x[1] + w[3] * x[2]
        d = x[-1]
        output = (t, i+1, x[0], x[-1], w[0], w[1], w[2], w[3], D)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*output))
        if not same_sign(d, D):
            has_error = true
            w[0] += (c * d * k)
            w[1] += (c * d * x[0])
            w[2] += (c * d * x[1])
            w[3] += (c * d * x[2])
    if not has_error:
        break

print("Total {} steps.".format(t-len(train_set)))
print("Total {} passes.".format(int(t/len(train_set))-1))

print("Weights:", w)
