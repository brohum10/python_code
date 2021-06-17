num = 4

print("%-10s %-10s %-10s" % ("a", "a^2", "a^3"))
for x in range(num):
    print("%-10d %-10d %-10d" % (x, x*x, x**3))
