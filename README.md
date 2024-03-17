# PixelGhost
A tool which hides the messages in the image using LSB method.

# Key Features
- It hides the message using LSB method.<br>
- Message can be decoded only by this tool.<br>

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
- Currently it supports `.png`.

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
