import hashlib

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def convertToImage(binary_data):
    with open("image.png", 'wb') as file:
        file.write(binary_data)

def encrypt(text):
    text = text.encode()
    encrypted = hashlib.sha256(text)
    text = encrypted.hexdigest()

    return text