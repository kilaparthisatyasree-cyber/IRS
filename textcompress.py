def compress(text):
    compressed = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed += text[i-1] + str(count)
            count = 1
    compressed += text[-1] + str(count)
    return compressed

with open("input.txt", "w") as f:
    f.write("AAGGTTT66")

with open("input.txt", "r") as f:
    data = f.read().strip()

compressed_data = compress(data)

with open("compresses.txt", "w") as f:
    f.write(compressed_data)
print("original:", data)
print("compressed:", compressed_data)