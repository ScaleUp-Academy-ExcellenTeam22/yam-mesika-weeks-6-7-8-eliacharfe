from PIL import Image


def decoding_message_in_image(image_path):
    """
    The function decodes a hidden message hidden in in each column of the image that the line number
    is corresponds to the numeric value of the character pixels if we take from left to right order.
    :param image_path: The path to an image.
    :return: The hidden message.
    """
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size[:2]
    return "".join([chr(row) for col in range(width) for row in range(height) if pixels[col, row] == 1])


if __name__ == '__main__':
    print(decoding_message_in_image("resources/code.png"))
    # Returns: "Place gunpowder beneath the House of Lords. 11/05/1605"


