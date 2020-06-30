# 🐍 Serpent (Serverless Picture Enrichment Toolkit)
## Configuration
### Structure Overview
```json
{
  "textfields": [
    {
      "name": <PARAMETER_NAME>,
      "position": [<X_COORDINATE>, <Y_COORDINATE>],
      "color": [<RGB_VALUES>],
      "font": [<FONT_NAME>,<FONT_SIZE>]
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
* Progress bars (WIP)