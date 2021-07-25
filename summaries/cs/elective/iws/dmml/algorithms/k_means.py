from typing import List

import numpy as np
from tabulate import tabulate


def k_means(data: np.ndarray, initial_centroids: np.ndarray, data_labels: List[str], class_labels: List[str], max_iterations: int = 5):
    assert len(data) == len(data_labels), "length of data does not match length of data labels"
    assert len(initial_centroids) == len(class_labels), "length of initial centroids does not match length of class labels"

    data = data.astype(float)
    initial_centroids = initial_centroids.astype(float)

    centroids = initial_centroids
    for iteration in range(max_iterations):
        print(f"\n\n{iteration}. Iteration:")

        print("\nCentroids:")
        for class_label, centroid in zip(class_labels, centroids):
            print(f"\\mu_{class_label}^{{({iteration})}} = [{', '.join([str(x) for x in centroid])}]")

        distances = []
        clusters = {n: [] for n in range(len(initial_centroids))}
        for data_label, data_point in zip(data_labels, data):
            dist = np.sqrt(((centroids - data_point[np.newaxis, :]) ** 2).sum(axis=1))
            distances.append(dist)
            clusters[np.argmin(dist)].append((data_label, data_point))

        print("\nDistances:")
        print(tabulate(np.asarray(distances).T, headers=data_labels, showindex=class_labels, tablefmt="github"))

        print("\nClustered Data:")
        for cluster_idx, cluster_data in clusters.items():
            print(class_labels[cluster_idx] + ": " + ", ".join(data_label for data_label, _ in cluster_data))
            centroids[cluster_idx, :] = np.mean([data_point for _, data_point in cluster_data], axis=0)


def main():
    data = np.array([[2, 8],
                     [2, 5],
                     [1, 2],
                     [5, 8],
                     [7, 3],
                     [6, 4],
                     [8, 4],
                     [4, 7]])
    initial_centroids = np.array([[1, 2],
                                  [6, 4],
                                  [8, 4]])
    data_labels = ["1", "2", "3", "4", "5", "6", "7", "8"]
    class_labels = ["A", "B", "C"]
    k_means(data, initial_centroids=initial_centroids, data_labels=data_labels, class_labels=class_labels)


if __name__ == '__main__':
    main()
