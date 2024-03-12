# PixelGhost
A tool which hides the messages in the image using LSB method.

<h1>Setup</h1>
1. Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
2. Install the <i>pillow</i> module on your system (Windows/Linux/MacOS) by copy and run the following command :<br><br>

```
pip3 install -r requirements.txt
```

<h1>Tested Systems</h1>
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.<br>

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and run the CMD/Powershell (Windows) or Terminal (Linux) in it and type the following commands for different operations : <br>
3. Encode the message into image : <br>
```
python PixelGhost.py -e -i image_name.png -m "Message inside this" -o output_image_name.png
```
4. Decode the message from image : <br>
```
python PixelGhost.py -d -i output_image_name.png
```

<h1>Key Features</h1>
<b>1. It hides the message like a ghost.</b><br>
<b>2. Message can be shown only by this tool.</b><br>
