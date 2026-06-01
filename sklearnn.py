from sklearn import tree

x = [[2, 2], [8, 8]]
y = [20, 80]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(x, y)
result = clf.predict([[5, 5]])
print(result)
