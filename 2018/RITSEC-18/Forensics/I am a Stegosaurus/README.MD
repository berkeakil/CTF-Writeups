In that challenge we provided by a png file.When we try to open that image we get an error.
<img src="stegosaurus_error.png" class="center"><br>
Image Viewer already pointed out the error.But i wanna get more details about it for that i used the pngcheck tool.
<img src="pngcheck.png"><br>
And the tool gives the hex bytes in addition to that.So what is the CRC error? <br>
<q>CRC (Cyclic Redundancy Check) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to raw data.</q>,says Wikipedia.<br>
This means there are changed bytes in my image.So i fired up hexeditor.
<img src="hexeditor.png">
Searched the given bytes and replaced them with "01 AA E4 16" at between 0x0000001D and 0x00000020.<br> 
<img src="flag.png" class="center" align="center">
