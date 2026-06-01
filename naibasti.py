import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

areas = ["Lahurabeer", "Cantt", "BHU", "Chetganj"]
labels = [1, 1, 1, 0]
gg = LabelEncoder()
X = gg.fit_transform(areas)
X = [[x] for x in X]
classifier = tree.DecisionTreeClassifier()
model = classifier.fit(X, labels)
plt.scatter([x[0] for x in X], labels, color="blue", marker="o")
plt.grid()
plt.xlabel("Encoded Area")
plt.ylabel("Connectivity (0/1)")
plt.title("Area Connectivity Classification")
plt.legend(["Actual Data"])
plt.show()
