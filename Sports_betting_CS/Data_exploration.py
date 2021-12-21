# The intent of this file is
# to generate some plots for the presentation

import matplotlib.pyplot as plt
import numpy as np
import re
from sklearn.cluster import MeanShift# as ms
from matplotlib import style
style.use("ggplot")

team_away = dict()
team_home = dict()
match_ups = set()
results = []
winners = dict()
losers = dict()

with open("season20082009.txt") as f:
    lines = f.readlines()
    team_name = re.compile("^[a-zA-Z\s]*$")
    stat = re.compile("([0-9]*[.])?[0-9]+")
    w_or_l = re.compile("^\d+$")


    for line in lines:
        stripped = re.sub('[\[\]]','',line)
        stripped = re.sub('([\"\'])', '', stripped)
        splits = stripped.split(",")
        print(splits)
        team_away[splits[0].strip()] = [float(val.strip(" ")) for val in splits[1:5] if val[-2] == 1]
        team_home[splits[5].strip()] = [float(val.strip(" ")) for val in splits[6:-2]if val[-2] == 0]
        winners[splits[0].strip()] = [float(val.strip(" ")) for val in splits[1:5] if int(splits[-2].strip(" ")) == 1]
        winners[splits[5].strip()] = [float(val.strip(" ")) for val in splits[6:-2] if int(splits[-2].strip(" ")) == 0]
        losers[splits[0].strip()] = [float(val.strip(" ")) for val in splits[1:5] if int(splits[-2].strip(" ")) == 0]
        losers[splits[5].strip()] = [float(val.strip(" ")) for val in splits[6:-2] if int(splits[-2].strip(" ")) == 1]
        match_up = (splits[0].strip(),splits[5].strip(),int(splits[10]))
        match_ups.add(match_up)


deletes = []
for key in winners:
    if winners[key] == []:
        deletes.append(key)
for key in deletes:
    del winners[key]
deletes = []
for key in losers:
    if losers[key] == []:
        deletes.append(key)
for key in deletes:
    del losers[key]

print(winners)
print(losers)

X = []
for key in winners:
    X.append(winners[key][0:2,2])
for key in losers:
    X.append(losers[key][0:2,2])

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
n_clusters_ = len(np.unique(labels))
cluster_centers = ms.cluster_centers_
fig = plt.figure()
ax = fig.add_subplot(111)
print("Number of estimated clusters:", n_clusters_)
colors = 10*['m','c','b','r','k','y','g']
plt.title('Mean Shift Clustering of Statistics')
plt.xlabel('ORB')
plt.ylabel('FT%')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], c=colors[labels[i]], marker='o')


ax.scatter(cluster_centers[:,0],cluster_centers[:,1],
            marker="x",color='k', s=150, linewidths = 5, zorder=10)

plt.show()








