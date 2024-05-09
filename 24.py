import numpy as np

a1 = np.array([25, 24, -1.5, 101])
a2 = np.array([23, 51, 15, -63])

print("a. Iteration")
for i in range(2):
    b1 = a1 if (i == 0) else a2
    for j in b1:
        print(f" {j},", end="")
        b = None
    print("")

print(f"b. sorted array: \n{np.sort(a1)} \n{np.sort(a2)} \n")
print("c. concatenated array: ", np.concatenate((a1, a2)))
