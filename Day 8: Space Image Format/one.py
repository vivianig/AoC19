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
    
min_layer = min(layers, key=(lambda layer: [x for row in layer for x in row].count(0)))
print(sum([row.count(1) for row in min_layer]) * sum([row.count(2) for row in min_layer]))
