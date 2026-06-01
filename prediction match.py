import numpy as np
import matplotlib.pyplot as plt

runs_input = input("Enter runs separated by comma : ")
# Run
runs = np.array(list(map(int, runs_input.split(","))))
total = np.cumsum(runs)
# ball
balls = np.arange(1, len(runs) + 1)
overs = balls / 10
print("\nOver\tScore\tBall\tTotal")

for i in range(len(runs)):
    print(f"1\t{runs[i]}\t{overs[i]:.1f}\t{total[i]}")

# Graph
plt.figure(figsize=(8,5))

plt.plot(overs, total, marker='o', linewidth=3)

plt.title("Cricket Score Graph")
plt.xlabel("Ball")
plt.ylabel("Total Score")

plt.xticks(overs)
plt.grid(True)

# Score labels
for i in range(len(overs)):
    plt.text(overs[i], total[i], str(total[i]))

plt.show()