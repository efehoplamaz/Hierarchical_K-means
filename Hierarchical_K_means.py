from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.cluster import KMeans
from collections import Counter

class HierarchicalKMeans(BaseEstimator, ClassifierMixin):

    def __init__(self, n_clusters=5, random_state=None):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def fit(self, X, y = None):

        clusters = {X}
        len_list = [1 if len(c) == 1 else 0 for c in clusters]

        while not all(len_list):

            print("In the depth of ...")

            for c in clusters:
                if len(c) > 1:
                    km = KMeans(n_clusters=self.n_clusters, random_state= self.random_state)
                    km.fit(c)
                    data_and_centers = zip(c,km.labels_)
                    for x, y in data_and_centers:
                        if y in data_and_centers:
                            Output[y].append((x, y))
                        else:
                            Output[y] = [(x, y)]




        return self