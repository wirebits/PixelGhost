# PixelGhost
# A tool which hides the messages in the image using LSB method.
# Author - WireBits

import os
import argparse
from PIL import Image

def encode_message(originalImage, stegImage, message):
    if not os.path.exists(originalImage):
        print("Original Image does not exist!")
        return
    if not message:
        print("Enter some message to hide!")
        return
    image = Image.open(originalImage)
    message += '\x00'
    encImage = encodeMessageInPixels(image.copy(), message)
    encImage.save(stegImage)
    print("Message encoded successfully!")

def decode_message(stegImage):
    if not os.path.exists(stegImage):
        print("Steg Image does not exist!")
        return
    image = Image.open(stegImage)
    hidden_message = decode_image(image)
    print("Hidden Message : ", hidden_message)

def encodeMessageInPixels(conImage, hdata):
    imgSize = conImage.size[0]
    (x, y) = (0, 0)
    for pixel in pixelsModification(conImage.getdata(), hdata):
        conImage.putpixel((x, y), pixel)
        if x == imgSize - 1:
            x = 0
            y += 1
        else:
            x += 1
    return conImage

def pixelsModification(picElement, hiddenData):
    dataList = generateData(hiddenData)
    dataLen = len(dataList)
    imageData = iter(picElement)
    for i in range(dataLen):
        picElement = [value for value in imageData.__next__()[:3] +
                      imageData.__next__()[:3] +
                      imageData.__next__()[:3]]
        for j in range(8):
            if dataList[i][j] == '0' and picElement[j] % 2 != 0:
                picElement[j] -= 1
            elif dataList[i][j] == '1' and picElement[j] % 2 == 0:
                picElement[j] += 1
        picElement = tuple([min(max(0, val), 255) for val in picElement])
        yield picElement[0:3]
        yield picElement[3:6]
        yield picElement[6:9]

def generateData(hidData):
    newData = []
    for z in hidData:
        newData.append(format(ord(z), '08b'))
    return newData

def decode_image(cipImage):
    imgData = iter(cipImage.getdata())
    data = ''
    while True:
        try:
            pixels = [value for value in imgData.__next__()[:3] +
                      imgData.__next__()[:3] +
                      imgData.__next__()[:3]]
        except StopIteration:
            break
        
        binaryString = ''
        for w in pixels[:8]:
            if w % 2 == 0:
                binaryString += '0'
            else:
                binaryString += '1'
        char = chr(int(binaryString, 2))
        if char == '\x00':
            break
        data += char
    return data

def main():
    parser = argparse.ArgumentParser(description='PixelGhost')

    parser.add_argument('-e', '--encode', action='store_true', help='Encode message into an image')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode message from an image')
    parser.add_argument('-i', '--input', type=str, help='Input image file')
    parser.add_argument('-m', '--message', type=str, help='Message to encode')
    parser.add_argument('-o', '--output', type=str, help='Output image file with encoded message')

    args = parser.parse_args()

    if args.encode:
        if not args.input or not args.message or not args.output:
            return
        encode_message(args.input, args.output, args.message)
    elif args.decode:
        if not args.input:
            return
        decode_message(args.input)
    else:
        print("Type python PixelGhost.py -h for help!")

if __name__ == "__main__":
    main()
