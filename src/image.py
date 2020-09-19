from PIL import Image


# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
def scale_image(img, target_value, orientation="horizontal"):
    """Scales an image based on the given parameters

    :param img: Base image
    :type img: PIL image
    :param target_value: desired width or height (depending on the orientation)
    :type target_value: int
    :param orientation: Orientation of the varimage: horizontal or vertical (optional)
    :type orientation: str

    :returns: Scaled version of the input image
    :rtype: PIL image"""
    target_value = int(target_value)
    if orientation == "horizontal":
        hpercent = (target_value / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, target_value), Image.ANTIALIAS)
    else:
        wpercent = (target_value / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((target_value, hsize), Image.ANTIALIAS)
    return img
