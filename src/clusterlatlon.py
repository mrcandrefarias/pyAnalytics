import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


registros = pd.read_csv('/home/marcos/Downloads/ultimos_registros.csv')

eps = 50/111034.61
X  =  np.array(registros[['Longitude','Latitude']])
db = DBSCAN(eps=eps, min_samples=10).fit( X )
core_samples = db.core_sample_indices_
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print n_clusters_

clusters = [X[labels == i] for i in xrange(n_clusters_)]
print clusters[0][1]
print clusters[1][1]

outliers = X[labels == -1]
#print outliers
