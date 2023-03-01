from PIL import Image, ImageDraw

from modules.textfield import Textfield
from modules.varimage import Varimage


def add_text(img, layout_object, request):
    """Adds textfields to an image as specified by the given layout

    :param img: Base image
    :type img: PIL image
    :param layout_object: Target layout
    :type layout_object: Layout object
    :param request: Request with all URL parameters
    :type request: str

    :returns: New image with added text
    :rtype: PIL image
    """
    draw = ImageDraw.Draw(img)
    for info in layout_object.get_textfields():
        tf = Textfield(info)
        text = request.args.get(info['name'], default="MISSING_TEXT_PARAMETER")
        tf.add_textfield(draw, text)
    return img


def add_extras(img, layout_object, request):
    """Adds extras (images, varimages,...) to an image as specified by the given layout

    :param img: Base image
    :type img: PIL image
    :param layout_object: Target layout
    :type layout_object: Layout object
    :param request: Request with all URL parameters
    :type request: str

    :returns: New image with added extras
    :rtype: PIL image
    """
    for extra in layout_object.get_extras():
        if extra['type'] == "image":
            im = Image(extra)
            img = im.add_image(img)
        if extra['type'] == "varimage":
            varimg = Varimage(extra)
            progress_parameter_value = request.args.get(extra['value_parameter_name'], default=0)

            if 'orientation' in extra:
                orientation = extra['orientation']
            else:
                # default to horizontal to retain backwards compatibility
                orientation = "horizontal"
            img = varimg.add_varimage(img, progress_parameter_value, orientation)
    return img
