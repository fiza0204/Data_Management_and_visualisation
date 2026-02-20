import matplotlib.pyplot as plt

n = int(input("Enter number of data values: "))

data = []

for i in range(n):
    value = int(input("Enter value: "))
    data.append(value)

bins = int(input("Enter number of bins: "))

plt.hist(data, bins=bins)
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()