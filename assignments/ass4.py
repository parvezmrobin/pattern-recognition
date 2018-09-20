true, false, null = True, False, None


def same_sign(val1, val2):
    if val1 < 0 and val2 < 0:
        return true
    if val1 >= 0 and val2 >= 0:
        return true
    return false


train_set = [
    (2, 10, 1),
    (3, 8, 1),
    (5, 2, 1),
    (50, 25, -1),
    (65, 30, -1),
    (35, 40, -1),
]
w = [0, 0, 0]
c, k = 1, 1

t = 0
while true:
    jhamela_ache = false
    for i, x in enumerate(train_set):
        t += 1
        D = w[0] + w[1] * x[0] + w[2] * x[1]
        d = x[-1]
        output = (t, i+1, x[0], x[-1], w[0], w[1], D)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*output))
        if not same_sign(d, D):
            jhamela_ache = true
            w[0] += (c * d * k)
            w[1] += (c * d * x[0])
            w[2] += (c * d * x[1])
    if not jhamela_ache:
        break

print("Total {} steps.".format(t-6))
print("Total {} passes.".format(int(t/6)-1))
