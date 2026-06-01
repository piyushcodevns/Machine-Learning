import numpy as np


def kmeans(X, k, max_iterations=100):
    centroids = X[np.random.choice(X.shape[0], k, replace=False), :]
    for i in range(max_iterations):
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, labels


np.random.seed(0)
X = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
X = np.array(X)
print(X)
X = X * 10
print("Input X\n", X)

requiredcentroids = int(input("no of centroids\n"))
centroids, labels = kmeans(X, k=requiredcentroids)
print("Centroids\n", centroids, "\nLabels\n", labels)

import matplotlib.pyplot as plt

for label in np.unique(labels):
    print("X=\n", X[labels == label, 0])
    print("Y=\n", X[labels == label, 1])
    plt.scatter(X[labels == label, 0], X[labels == label, 1])
    plt.plot(X[labels == label, 0], X[labels == label, 1], label=f"Cluster {label}")

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=200,
    linewidths=3,
    color="pink",
    label="Centroids",
)
plt.legend()
plt.show()
