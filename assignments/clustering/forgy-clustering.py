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


def get_new_centroids(centroids, nearest_centroids, features):
    m = len(centroids[0])
    k = len(centroids)
    summations = [[0] * m for i in range(k)]
    count = [0] * k
    for item, centroid in enumerate(nearest_centroids):
        for col in range(m):
            summations[centroid][col] += features[item][col]
        count[centroid] += 1

    for i in range(k):
        for j in range(m):
            summations[i][j] /= count[i]

    return summations


def main():
    features = [
        (4, 4),
        (8, 4),
        (15, 8),
        (24, 4),
        (24, 12),
    ]
    n = len(features)
    k = 2
    centroids = features[:k]
    nearest_centroids = [-1] * n
    while true:
        centroid_changed = false
        for i in range(n):
            nearest_centroid = get_nearest_centroid(features[i], centroids)
            if nearest_centroid != nearest_centroids[i]:
                centroid_changed = true
                nearest_centroids[i] = nearest_centroid
        print_cluster(centroids, features, n, nearest_centroids)
        if centroid_changed:
            centroids = get_new_centroids(centroids, nearest_centroids, features)
        else:
            break


def print_cluster(centroids, features, n, nearest_centroids):
    print(Fore.BLUE + "Centroids: " + Fore.RESET)
    for i in range(n):
        print(features[i], centroids[nearest_centroids[i]])
    print("")


main()
