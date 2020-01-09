from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.cluster import KMeans
import numpy as np
from collections import Counter
import itertools

class HierarchicalKMeans(BaseEstimator, ClassifierMixin):

    def __init__(self, n_clusters=5, depth = 2, random_state=None):
        self.n_clusters = n_clusters
        self.depth = depth
        self.random_state = random_state

    def fit(self, X, y = None):

        clusters = [X]
        count = 0
        depth = self.depth
        n_many_clusters = self.n_clusters


        while count < depth:
            temp = []
            for cluster in clusters:
                kmeans = KMeans(n_clusters=n_many_clusters, random_state=0).fit(cluster)
                seperated = []
                for key, group in itertools.groupby(zip(cluster, kmeans.labels_), lambda x: x[1]):
                    gr_list = []
                    for thing in group:
                        gr_list.append(thing[0])
                    seperated.append(gr_list)
                temp.extend(seperated)
            clusters.clear()
            clusters.extend(temp)
            count += 1
        self.clusters_ = clusters
        return self



if __name__ == "__main__":

    X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    hkm = HierarchicalKMeans(n_clusters=2, depth= 2)
    hkm.fit(X)
    print(hkm.clusters_)