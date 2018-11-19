In that challenge we provided by a png file.When we try to open that image we get an error.
<img src="stegosaurus_error.png">
Image Viewer already pointed out the error.But i wanna get more details about it for this i used the pngcheck tool.
<img src="pngcheck.png">
And the tool gives the hex bytes in addition to that.So what is the CRC error? Looking up the google:
CRC (Cyclic Redundancy Check) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to raw data.
This means there are corrupted bytes in my image.So i fired up hexeditor.
<img src="hexeditor.png">
I searched the given bytes.And replace the bytes at between 0x0000001D and 0x00000020 with 01 AA E4 16
<img src="flag.png">
