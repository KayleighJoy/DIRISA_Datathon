import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import MiniBatchKMeans

data = pd.read_csv("C:\\Users\\ruans\\Desktop\\Dataset_Without_Redundant.csv", sep=';')
x_Train, x_Test = train_test_split(data, test_size=0.20, random_state=42)

kmeans = MiniBatchKMeans(n_clusters=2, random_state = 0, batch_size = 30)
