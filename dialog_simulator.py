#imports
import pyttsx3 as tts

#get the names of the characters
name=input('name:')

#load dialog
dialog=0
with open('dialog.txt','r') as file:
    dialog=file.readlines()
dialog=[line.strip('\n') for line in dialog]
#script
enginne=tts.init()
for line in dialog:
    if line=='':
        pass
    elif len(line)<len(name) or line[:len(name)]!=name:
        enginne.say(line[line.find(':')+1:])
        print(line)
        enginne.runAndWait()

    else:
        input('Press to continue.')
        print('You: '+line[len(name):])
        
print("END Thank You")
