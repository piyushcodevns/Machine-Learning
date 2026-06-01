import matplotlib.pyplot as plt
y=[6,4,5,7,2,8]
x=[1,2,3,4,5,6]

avgy=sum(y)/len(y)
start_y=[y[0] for i in x]

if y[-1]>y[0]:
    color="green"
elif y[-1]<y[0]:
    color="red"
else:
    color="yellow"

plt.plot(x,y,color=color)
plt.plot(x,start_y,color="blue",linestyle="--")
plt.scatter(x,y)
plt.show()
