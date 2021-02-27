# ascii-art-generator
generates ascii art from pictures, videos, webcam feed, or youtube videos



# how it works
### short version
image is shrunk, then each pixel is converted to a character based on its brightness (ex ' '=brightness 0, 'X'=brightness 100, '@'=brightness 255, etc)
### longer version
Videos will be split into frames with openCV, and each frame is converted to a PIL image.
PIL image is then resized to y=vertical_size, keeping the orignal aspect ration, then x is scaled by horizontal_scale to roughly match the original aspect ratio when converted to ascii.
Each pixel in the resized image is itererated through, and brightness is determined by (r+g+b)/3, which is then scaled down to an integer from 0-48, and that location in char_list defines the character which will be used to represent that pixel.

char_list was generated using char_brightness_rating.py, which prints out each character enough to fill terminal window, screenshots, calculates average brightness, and sorts characters based on calculated brightness

youtube videos are downloaded with pytube https://github.com/pytube/pytube



# usage
run ascci_art_generator.py. you should see the following

```
a) saved video
b) saved picture
c) screenshot
d) webcam
e) youtube video
f) read saved ascii art
g) settings
h) quit
```

enter a letter to choose what you want to do. The may then prompt you for input if your choice requires it. For a, b, and f, the option required is 'path'. this is where on your disc the file you want to display is.
for e, the option required is 'url'. this is the url of the youtube video
for d, the option required is 'webcam id'. this is the id of the webcam you want to use, which will usually be 0


### description of each option

`a) saved video`
uses openCV to convert each frame of an mp4 video to ascii, and displays that on the terminal
input: path=location of video on disc

`b) saved picture`
uses PIL to open an image, and prints out it's ascii art
input: path=location of picture on disc

`c) screenshot`
uses PIL.ImageGrab, pyautogui, and keyboard to capture a screenshot. to use this option, move your mouse to the top left corner of what you want to caputre, press shift, move mouse to bottom right corner, pres shift again, and the program will display this in ascii art

`d) webcam`
uses openCV to get live webcam feed
input: webcam id=which webcam to use, starting from 0

`e) youtube video`
uses pytube to download video to yt_video_path (changeable in settings menu), calls play_ascii_video, then deletes the saved file
input: url=url of youtube video to play

`f) read saved ascii art`
reads and displays a text file containing ascii art generated from this program. to save ascii art, see settings menu
input: path=location of text file

`g) settings`
allows user to change settings. you can change the following variables:
```
float horizontal_scale -- default 2, how many characters wide each pixel should be
int vertical_size -- default 75, how many lines the generated ascii art should be
str yt_video_path -- default None, where to temporarily save youtube videos (must be set to use option e)
int frames_to_play -- default 0, how many frames of a video to display before returning to menu. if 0, displays all
int mirrored -- default 0, (0 or 1) if image should be flipped when converted. most useful with webcam feed
str save_ascii_art_in -- default None, text file to save each ascii image in.
```

`h) quit`
pretty self explainitory



# dependencies

### required
    PIL
    cv2

### needed for certain features
    pytube (for youtube feature)
    keyboard (for screenshot feature)
    pyautogui (for screenshot feature)

# examples

### surprised pikachu
##### vertical_size = 25

![surprised_pikachu_small](https://raw.githubusercontent.com/rainbowkitty227/ascii-art-generator/main/examples/surprised_pikachu_small.png)

##### vertical_size=75

![surprised pikachu large](https://raw.githubusercontent.com/rainbowkitty227/ascii-art-generator/main/examples/surprised_pikachu_large.png)

### my desk

##### vertical_size=75
objects from left to right: an open drawer, a dry erase marker, my phone, coffee mug, and a keypad

![my desk](https://raw.githubusercontent.com/rainbowkitty227/ascii-art-generator/main/examples/my_desk.png)


# inspiration
https://github.com/samuel1212703/Video-To-Ascii-CMD and https://github.com/jsimb/image-to-ascii
