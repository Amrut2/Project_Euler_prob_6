
add = 0
ad = 0
count1 = 0
count = 0

for i in range(101):
  add = add + (i**2)

  count += 1
# print(count)
z = add


for i in range(101):
  ad = (ad + i)
  count1 += 1

# print(count1)
t = ad**2


print(t-z)
