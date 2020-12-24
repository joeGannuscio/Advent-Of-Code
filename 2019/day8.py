from collections import Counter
from itertools import chain

def main():
    input = readInput('Inputs/day8.txt')
    part1(input)
    part2(input)

def part1(input):
    layers = processImageLayers(input)
    
    minZero = 999
    result = 0
    for layer in layers:
        layerCount = Counter(layer)
        if minZero > layerCount['0']:
            minZero = layerCount['0']
            result = layerCount['1'] * layerCount['2']
        
    print(result)

def part2(input):
    image = decodeImage(processImageLayers(input))
    displayImage(image)

def displayImage(image):
    print(image[0:24])
    print(image[25:49])
    print(image[50:74])
    print(image[75:99])
    print(image[100:124])
    print(image[125:149])

def decodeImage(layers):
    image = ['2'] * (25*6)
    index = 0
    for layer in layers:
        index = 0
        for pixel in layer:
            if image[index] == '2':
                image[index] = pixel
            index += 1

    return image

def processImageLayers(input):
    layers = []
    layer = []
    index = 0

    for char in input:
        if index == 25*6:
            layers.append(layer)
            layer = []
            index = 0
        layer.extend(char)
        index += 1
    return layers

def readInput(path):
    with open(path) as file:
        return file.readline()

if __name__ == '__main__':
    main()