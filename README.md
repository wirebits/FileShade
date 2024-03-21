# FileShade
A tool which transfer files in password protected text.

# Key Features
- It can encode and decode files into text.
- It lock/unlock the text with a password.

# OS Support
- Windows 10

# Setup
Make sure the latest python is installed on your system (Windows/Linux/MacOS).<br>

# Parameters
There are 4 parameters after command ```python``` (windows) or ```python3``` (Linux) :
1. **-e** - Encode the input.
2. **-d** - Decode the input.
3. **-p** - The password set on the file.
4. **-i** - The file name want to encode / decode.

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder.<br>
3. Open CMD/Powershell (Windows) or Terminal (Linux) in that folder.
## Encode

```
python FileShade.py -e -p password -i file_name
```
## Decode

```
python FileShade.py -d -p password -i file_name
```
