with open("input") as f:
    encrypted_image = [int(x) for x in f.readline()]

size = (25,6)

number_layers = len(encrypted_image)//(size[0] * size[1])

layers = []
counter = 0
for x in range(number_layers):
    layer = []
    for i in range(size[1]):
        row = []
        for j in range(size[0]):
            row.append(encrypted_image[counter])
            counter+=1
        layer.append(row)
    layers.append(layer)

layers.reverse()

image = layers[0]

for layer in layers[1:]:
    for i, row in enumerate(layer):
        for j, pixel in enumerate(row):
            if pixel != 2:
                image[i][j] = pixel

for row in image:
    print (" ".join([str(x) for x in row]))
