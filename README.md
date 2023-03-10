# Dialog Trainer
Short python code which simulates a dialog according to a script by using a text to speech library . You can give yourself a role from the script and read your part yourself.

This code uses the ```pyttsx3``` library in oreder to read aloud. You might need to install it in oreder to be able to run the script. Link: https://pypi.org/project/pyttsx3/
 
The code loads the dialog script out of a file (```dialog.txt``` by default). You might need to paste or change the path of the file. You can change the filepath (```open(file arg)```) in line (~)9.

Than it gets the name(Enter name as in script without colon) of the character you want to be and activates a ```for line in dialog:``` following this algorythm:
* if it is user's character's turn: wait for the user to finish reading and pressing (ENTER) to continue go on. (plus print the user's characters line)
* if it is not user's character's turn than read alound and print it. Note that I rely on ```engine.runAndWait()```'s natural delay. If for whatever reason, it works faster for you than ```import time``` and add a ```time.sleep()``` right after ```engine.runAndWait()```. time.sleep() takes a ```seconds``` argument but you might want to make much more to avoid delays in case it is your turn etc.
* if the line is blank: ignore it. (This gives the script a bit rellyableness regarding the dialog script)

dialog script reqirements: 
* As mentioned above the dialog is immune to blank lines. (So use them to separate pages etc.)
* Which character line it is, schould be marked as with ```NAME:```(Name + colon). eg:
```
Mr.Black: Good morning!
Tom: Hallo!
Mr.Black: How are you doing?
Lucy: I am doing great!
Tom: I am also fine.
```
* Note:
  - Names are not allowed to contain colon's but the line after the : is allowed to contain as any amount of them.
  - The whole quote(line) should be on the same line as the indicating Name. Otherwise mistakes and misinterpritation may occur. Use an editor which shows line numeration or clearly puts the whole quote into one big snake rather than adjusting it to fit into the canvas.
