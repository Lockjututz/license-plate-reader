# License plate number extractor

Extract an Åland/Swedish/Finnish licence plate from a picture.

## Prerequisites
You must install tesseract separately before running this script. On MacOS:

```
brew install tesseract
brew install tesseract-lang
```

On Linux use apt-get. Windows? Google it.

Then you must install all the required packages specified in the requirements.txt file. Like this:

```
pip install -r requirements.txt
```

## Running
Run the script:
```
python plate_reader.py
```