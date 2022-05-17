import matplotlib.pyplot as plt


cpp_data = [[], [], []]
py_data = [[], [], []]
with open("cpp_data.dat", 'r') as cpp_input:
    for string in cpp_input:
        s = string.split()
        cpp_data[0].append(s[0])
        cpp_data[1].append(s[1])
        cpp_data[2].append(s[2])

with open("py_data.dat", 'r') as cpp_input:
    for string in cpp_input:
        s = string.split()
        py_data[0].append(s[0])
        py_data[1].append(s[1])
        py_data[2].append(s[2])


plt.subplot(2, 2, 1)
plt.grid(True)
plt.title("C++, Count/Time")
plt.xlabel("Count")
plt.ylabel("Time, ms")
plt.plot(cpp_data[0], cpp_data[1])



plt.subplot(2, 2, 2)
plt.grid(True)
plt.title("C++, Count/Size")
plt.xlabel("Count")
plt.ylabel("Size, bytes")
plt.plot(cpp_data[0], cpp_data[2])


plt.subplot(2, 2, 3)
plt.grid(True)
plt.title("Python, Count/Size")
plt.xlabel("Count")
plt.ylabel("Size, bytes")
plt.plot(py_data[0], py_data[2])


plt.subplot(2, 2, 4)
plt.grid(True)
plt.title("Python, Count/Time")
plt.xlabel("Count")
plt.ylabel("Time, ms")
plt.plot(py_data[0], py_data[1])

plt.show()
