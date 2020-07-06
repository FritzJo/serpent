# 🐍 Serpent (Serverless Picture Enrichment Toolkit)
## Configuration
### Structure Overview
```json
{
  "textfields": [
    {
      "name": "<PARAMETER_NAME>",
      "position": ["<X_COORDINATE>", "<Y_COORDINATE>"],
      "color": ["<RGB_VALUES>"],
      "font": ["<FONT_NAME>","<FONT_SIZE>"]
    }
  ],
  "extras": [
  ]
}
```
### Components
Components are the types of elements you can add to an image. Currently supported are:
* Textfields
* Other Images
* Variable Images

#### Textfields
Textfields are the most basic components of Serpent. They display a given text on a specific position in your image. Each textfield configuration has to contain four values:

| Configuration | Description | Example |
| --- | --- | --- |
| name | Name of the URL parameter that contains the text value | value1 |
| position | Array containing coordinates of the top left corner of the textfield | [100, 130] |
| color | Array containing RGB values, defining the text color | [168, 235, 52] |
| font | Name and size of the font that will be used to render the text (has to be placed in the fonts folder) | ["Roboto-Light",30] |

#### Other Images
Serpent can also merge images together and overlay different images. Those configurations are placed in the **extras** section of a layout file. Each **extras** component has a value, defining its own type. "Other Images" have the type: *image*

| Configuration | Description | Example |
| --- | --- | --- |
| type | Type of the extra | image *(has to be that value)* |
| offset | Array containing coordinates of the top left corner of the image | [100, 130] |
| filename | Name of the image that will be added to the base image (has to be an existing file in the images folder) | example.png |

#### Variable Images
Variable Images are currently the most complex structures supported by Serpent. They add the ability to add a scaled image to a base image, with the option to move it inside a pre-defined box dynamically with URL parameters. They can be used to create custom progress bars.

Those configurations are also placed in the **extras** section of a layout file. Each **extras** component has a value, defining its own type. "Variable Images" have the type: *varimage*

| Configuration | Description | Example |
| --- | --- | --- |
| type | Type of the extra | varimage *(has to be that value)* |
| filename_bar | File name of the image that will be added | example.png |
| position_bar | Point where the top left corner of the image will be inserted | [355, 350] |
| height | Height of the image (will be scaled to match that height, while retaining the aspect ratio | 120 |
| width | Width of the dynamic box | 860 |
| max | Maximum value for the dynamic positioning. Use 100 if you want to use percentages as values | 100 |
| value_parameter_name | Name of the URL parameter that will contain the dynamic positioning value of the image | value1 |

