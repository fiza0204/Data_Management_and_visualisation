
import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    x_val = int(input("Enter X value: "))
    y_val = int(input("Enter Y value: "))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Dynamic Line Chart")
plt.show()

