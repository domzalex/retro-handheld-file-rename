# retro-handheld-file-rename
A quick/rudimentary way to remove the 'numbering' from the front of game files to help order alphabetically

VIDEO GUIDE: https://youtu.be/VP2iPfSrzIw

EASY TEXT GUIDE:

If your ROM folder structure looks something like:

GBC
SNES
PSX
..
..

Put the Python script outside of ALL of them like this:

GAMES>
  rename.py
  GBC
  SNES
  PSX
  ..
  ..
  
And then when prompted, input the file directory like so:

GBC/


If your files look like:

001 Pokemon Ruby
002 Legend of Zelda
003 Megaman Zero
..

Then you would want to remove 4 digits (script will remove however many digits you set at the BEGINNING of the file name), so if you input 4, the files will come out like this:

Pokemon Ruby
Legend of Zelda
Megaman Zero
..

Feel free to add onto this script/modify it to be even better.
