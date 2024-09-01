# PixelGhost
A tool which hides the messages in the image using LSB method.

# Key Features
- It hides the message using LSB method.
- Message can be decoded only by this tool.

# JPG To PNG CLI Converter
- It is a small command-line tool so that it converts `.jpg` files into `.png` files.
- It can download from [here]().
- It works only on Windows.
- To use this tool, create a folder and put this tool and `.jpg` file in it.
- Open Terminal.
- Type the following command and press enter :
  
  ```
  JPGToPNGConverter.exe INPUT.jpg OUTPUT
  ```
- Replace `INPUT` with actual file name of the `.jpg` file and `OUTPUT` with actual file name of `.png` file.

# Setup
1. Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
2. Install the <i>pillow</i> module on your system (Windows/Linux/MacOS) by copy and run the following command : <br>

```
pip3 install -r requirements.txt
```

# Parameters
1. **-e** : Encode
2. **-d** : Decode
3. **-i** : Input Image
4. **-m** : Message want to hide
5. **-o** : Output Image

# Supported Image Format
- Currently it supports `.png`.<br>
- Use `.png` format images for hide messages more securely.<br>
- Try to use those `.png` image with background not transparent background.<br>

# Tested Systems
The tool is currently tested on : <br>
1. Windows (10)<br>

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and run the CMD/Powershell (Windows) or Terminal (Linux) in it : <br>
## Encode the message
- Windows
```
python PixelGhost.py -e -i input_image_name.png -m "Message inside this" -o output_image_name.png
```
- Linux
```
python3 PixelGhost.py -e -i input_image_name.png -m "Message inside this" -o output_image_name.png
```
## Decode the message
- Windows
```
python PixelGhost.py -d -i output_image_name.png
```
- Linux
```
python3 PixelGhost.py -d -i output_image_name.png
```
