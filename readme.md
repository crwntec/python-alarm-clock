**Simple Alarm clock**
This is a simple alarm clock coded in python

**Instructions:**
To Work we need to install playsound package via **pip install playsound**

**How it works:**
The script compares the actual Time with the entered Time every Second.
For that to work we need to convert the entered Sting into the same format which the function datetime.now() returns.
The method datetime.now() returns the full date but we only want to compare hours and Minutes so we need to access those by accessing the object with contains the datetime.now() Method. With a.hour and a.minute we get the current hour and Minute as int! So now we only need to convert our Input to Int and seperate it. With the map() function we convert tge input and split it with the split() function. Now we can compare the current Hour with the Input Hour and the Input Minute with the Actual Minute. If those match: Boom! It prints ALARM! In the console and plays a sound.
