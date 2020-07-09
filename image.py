from PIL import Image


# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
def scale_image(img, target_value, orientation="horizontal"):
    if orientation == "horizontal":
        hpercent = (target_value / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, target_value), Image.ANTIALIAS)
    else:
        wpercent = (target_value / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((target_value, hsize), Image.ANTIALIAS)
    return img
