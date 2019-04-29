fname = "googleMemo.txt"

f = open("googleMemo.txt", "r", encoding="utf8")
f = f.read()
count = 0
for i in f:
    count += 1
    print(i)

print(count)