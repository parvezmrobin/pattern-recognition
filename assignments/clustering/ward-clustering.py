from copy import deepcopy
from math import inf

from colorama import Fore

true, false, null = True, False, None


def get_means(cluster, features):
    n = len(features[0])
    sums = [0] * n
    for item in cluster:
        for i in range(n):
            sums[i] += features[item][i]

    total_item = len(cluster)
    for i in range(n):
        sums[i] /= total_item

    return sums


def get_variance(cluster, means, features):
    error = 0
    n = len(features[0])
    for item in cluster:
        for i in range(n):
            error += (features[item][i] - means[i]) ** 2
    return error


def print_error(clusters, i, j, error):
    n = len(clusters)
    for k in range(n):
        if k == j:
            continue
        if k == i:
            cluster = clusters[i] + clusters[j]
        else:
            cluster = clusters[k]
        mapped = map(lambda item: item + 1, cluster)
        print(list(mapped), end=' ')
    print("{:.2f}".format(error))


def get_near_most_clusters(clusters, features, log=false):
    if log:
        print(Fore.RED + "Errors:" + Fore.RESET)

    min_error = inf
    c1, c2 = null, null
    n = len(clusters)
    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                continue
            error = get_error(clusters, features, i, j)
            if log:
                print_error(clusters, i, j, error)
            if error < min_error:
                min_error = error
                c1, c2 = i, j

    return c1, c2


def get_error(clusters, features, i, j):
    clusters_copy = deepcopy(clusters)
    i, j = sorted([i, j])
    clusters_copy[i] += clusters_copy.pop(j)
    error = 0
    for cluster in clusters_copy:
        if len(cluster) > 1:
            means = get_means(cluster, features)
            error += get_variance(cluster, means, features)
    return error


def print_cluster(clusters):
    mapped_clusters = map(lambda cluster: [item + 1 for item in cluster], clusters)
    print(Fore.BLUE + "Clusters:" + Fore.RESET, *mapped_clusters, end='\n\n')


def main():
    features = [
        (2, 2),
        (3, 3),
        (3, 4),
        (4.5, 5),
        (6, 6),
        (6, 8),
        (7, 9),
        (8, 8),
        (9, 10)
    ]
    n = len(features)
    clusters = [[i] for i in range(n)]

    for i in range(n - 1):
        i1, i2 = get_near_most_clusters(clusters, features)
        c2 = clusters.pop(i2)
        clusters[i1] += c2
        print_cluster(clusters)


main()
