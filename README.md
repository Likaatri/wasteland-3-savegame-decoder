# Wasteland 3 Save File Decoder

## Features

 * Extracts a Wasteland 3 save file into a human readable xml file.
 * Repacks the edited file back to a WL3 save file.

## Requirements

> pip install python-lzf

## Steps

 1. Copy the save file to this folder.
 2. In save_extract.py: Replace filename (without .xml ending) and uncomment loadfile().
 3. Run the python script. A decoded file _SAVEGAMENAME_.xml_editable
 is created.
 4. Edit _SAVEGAMENAME_.xml_editable.
 5. In save_extract.py: comment out loadfile() and uncomment savefile().
 6. Run the script again, which creates _SAVEGAMENAME_.xml_new.
 7. Replace the original save file with this new file (make a backup first).

## Credits

Based on this [Reddit post](https://www.reddit.com/r/Wasteland/comments/ik4xn9/editing_save_files_stepbystep/) of an unknown Person.




