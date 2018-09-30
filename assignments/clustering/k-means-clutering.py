from functools import reduce
from math import inf

from colorama import Fore

true, false, null = True, False, None


def euclidean_distance(feature1, feature2):
    n = len(feature1)
    assert n == len(feature2)

    dist = sum([(feature1[i] - feature2[i]) ** 2 for i in range(n)]) ** .5
    return dist


def get_nearest_centroid(item, centroids):
    min_i = -1
    k = len(centroids)
    min_dist = inf
    for i in range(k):
        dist = euclidean_distance(item, centroids[i])
        if dist < min_dist:
            min_dist = dist
            min_i = i
    return min_i


def update_centroid(cluster):
    m = len(cluster[0])
    n = len(cluster)
    summation = reduce(lambda x, y: [x[i] + y[i] for i in range(m)], cluster)

    return list(map(lambda x: x / n, summation))


def main():
    features = [
        (8, 4),
        (24, 4),
        (15, 8),
        (4, 4),
        (24, 12),
    ]
    k = 2
    centroids = features[:k]
    clusters = [[features[i]] for i in range(k)]

    for feature in features[k:]:
        cluster = get_nearest_centroid(feature, centroids)
        clusters[cluster].append(feature)
        centroids[cluster] = update_centroid(clusters[cluster])

    clusters = [[] for i in range(k)]
    for feature in features:
        cluster = get_nearest_centroid(feature, centroids)
        clusters[cluster].append(feature)

    print(Fore.BLUE + "Centroids:" + Fore.RESET, *centroids)
    print(Fore.BLUE + "Clusters:", Fore.RESET)
    print(*clusters, sep='\n')


main()
