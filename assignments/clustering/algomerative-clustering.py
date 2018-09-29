from math import inf, nan
from colorama import Fore

true, false, null = True, False, None


def euclidean_distance(x0, x1):
    n = len(x0)
    assert n == len(x1)

    distance = 0
    for i in range(n):
        distance += (x0[i] - x1[i]) ** 2

    return distance ** .5


def init_distance_triangle(features):
    n = len(features)
    assert n > 0

    distances = {0: []}
    for i in range(1, n):
        distances[i] = [euclidean_distance(features[i], features[j]) for j in range(i)]
    return distances


def get_near_most_clusters(distances):
    c1, c2 = null, null
    min_dist = inf
    for i, row in enumerate(distances):
        for j, dist in enumerate(distances[row]):
            if dist < min_dist:
                min_dist = dist
                c1, c2 = i, j

    return c1, c2


def distance_update(distances, i, j, algorithm='SingleLinkage'):
    if algorithm not in ['SingleLinkage']:
        raise RuntimeError("Invalid algorithm!")
    n = len(distances)
    i, j = sorted([i, j])
    new_distances = {0: []}
    adv = 0  # determines if jth row is crossed
    for k in range(1, n):
        if k == j:  # row for second cluster no longer exists
            adv = 1
            continue
        if k == i:  # row for first cluster will be combined with row for second cluster
            if algorithm is 'SingleLinkage':
                new_distances[k] = [min(distances[i][l], distances[j][l]) for l in range(k)]
            continue
        new_distances[k - adv] = []
        for l in range(k):
            if l == i:
                distance = nan
                if algorithm is 'SingleLinkage':
                    distance = min(distances[k][i], distances[k][j])
                new_distances[k - adv].append(distance)
                continue
            if l == j:
                continue
            new_distances[k - adv].append(distances[k][l])

    return new_distances


def print_cluster(clusters):
    mapped_clusters = map(lambda cluster: [item + 1 for item in cluster], clusters)
    print(Fore.BLUE + "Clusters:" + Fore.RESET, *mapped_clusters)


def print_distances(distances):
    mapped_distances = map(lambda key: ["{:5.2f}".format(dist) for dist in distances[key]], distances)
    print(Fore.GREEN + "Distances:" + Fore.RESET, end='')
    for row in mapped_distances:
        print(*row)
    print("")


def main():
    features = [
        (4, 4),
        (8, 4),
        (15, 8),
        (24, 4),
        (24, 12),
    ]

    n = len(features)
    clusters = [[i] for i in range(n)]
    distances = init_distance_triangle(features)

    for i in range(len(clusters) - 1):
        print_cluster(clusters)
        print_distances(distances)
        i1, i2 = get_near_most_clusters(distances)
        c1 = clusters.pop(i1)
        clusters[i2] += c1
        distances = distance_update(distances, i1, i2)


main()
