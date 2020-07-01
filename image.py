from PIL import Image

from storage import get_image

# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
def scale_image(img, target_height):
    hpercent = (target_height / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, target_height), Image.ANTIALIAS)
    return img
