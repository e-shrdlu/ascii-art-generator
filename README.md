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
vertical_size = 25
```
///////r!+vlvvvi*!}VVVVVVVVVVSji<<7/////////////////////////////<~/vv^^^i/77r^?j2SSSS2V#
///////+*ilv^^^^i+7jSVVVVVVVVVVVClr+<r/iii//////////////////////7!!/i/r/^ltCSVVVVVSSSSV#
//////<~!/r77<77ii77l2VVVVVSSVVVVyS}^7<7r/////////rrrrrr7777777<<!*7^l}xSSSVVSSSSSSSSSyb
/////r~~<<++!!!!+//!+ijSVVVVVVVVVVVVV2?/<<7<7777r////////////iivltjxSVVVSSSSSSSSSSSSVSV$
/////!;+<++!!!!!!+<<+!+v2VVVVSSSVSSVVVVSxCCCCxxx2SSVVVVVVVVVVVVVVVVSSSSSSSSSSSVVVSVS2j?t
i///7;~++++++++!+!+<<+~~7}VVVVSSSSSSSVVVVVVVVVVVVSSSSSSSSSVVSSSSSSSSSSSSSSSSSSVVVSx?irr/
iiir*"!+++!!!++++++++++*~!iCVSx2SSSSSSSVVSSVSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVV2j^7+!++<
ii/<;*<<<+!!!!!!++!!!++++!~!r^?CSVVSSSVVVVVVVVVVSSSSSSVVSSSSVVSSSSSSVSSS2x2VVx?/<+++++++
/ir~"!+!!!!!!!!!!!!!****!++~~^2SSSSSSSVVVSSVSSVVSSSSSSVSSSSSSSSSSSSSSSVS2j?lir+++<<<<+!!
//!;~*****!!!!!!!!*~";;;~!!~rxVSSSSSSVyVVSSVVVVVSSSSSSSSSSSVSSVVVVSSSSSSS2t7!+<<<<<+++!!
i7;"*!!!!!**!!!!!!~;___;*!"*tVSSSSxCjt}xSVSSVVSSSSSSSSSSSSSxj}lv}xSSSSSSSSSt7+<<<<++++++
/*;!+!!!!!!!!!!!!!*~""~*+*"/2SSSS2?ljr~<tSSSSSSSSSSSSSSSSS2??Sl"~/CSSSSSSSSSl+!<77777777
+;"!+!*~~~~~"~*!+!!!++<7r**tSS22Sx^+7~,;^2SSSSSSSSSSSSSSSS2l+<*:_7}SSSSSSSSV2/*<r///////
;_*!*~";___::__;*+++++<7<"7xS22SSS2v<!!<?2SSSSSSSSSSSSSSSSSx?r+!<l2SSSSSSSSSVt+<///rrrrr
:"!!~"___:::::::"!!+<<<<*!}VVVVVVVVVS222SSSSxt^ivt2SSSSSSSSSVS2x2SVVVVVVVSSSS2r+/////rrr
"++!~";_:::::,,_~!+<777+"*iv?jxSVVVVVVVVSSSSSC?i/lxSSSSSSSSSSSVVVVSxCCCCxSSSSSl</i///rrr
+<++!*****!!!!*+<777r77*;*7rr7rl2VVVVVVVSVVVVVVVVSSSSSSSSSSSSSSVV2ti/iiiilCSSSC7<ii///rr
+<++++<<77r777/i//rr77+;~illv^/iCVVVVVVVVVVVVVS2222SVSVSSSSSSSSVSj^/^^^^irl2SSSl+7///rr/
!+!!!++++++!!!<r//rr77~:~r^^^^/l2VVSVVVVVVVx?/<7/^vvltCSSSSSSSSVS}ii^vvvirl2VSSxr*<77777
<++!!!!!!!!*!!!!!!+++!"~i^rr/ilCVVVSSVVVVVS}<~/}CxxC}vlCSSSSSSSVV2?iiiii^vCVSSSVt!+77777
r+!!!!!!*************~"*}y2Cxx2SVVVVVVVVVVVx/7}SSSSSx?vCSSSSSSSSSVSC}}}}C2SVSSSVSi+ii//r
7+!!!!****************~"rxyVVVSVSVVVVVSSVSVV}iitjCxCt^lxSSSSSSSSSSSSSSSSSSSSSSSSVt+/^///
7<<7r7<<+<<77rrrr777777+*/xVVSSSSVVVVSSSSSSVV2}?vvvvv?CSSSSSSSSSSSSSSSSSSSSSSSSSVxr+r77<
!**+7//iiii^^iiiiiiiiiii<!/xVSSSVSSSSSSSSSSSVVVSS2S2SSSSSSSSSSSSSSSSSS2SSSSSSSSSSSl!<<<<
**~*!+++<7//////////r7+!!++v2SSSVVSSSSSSSSSSSSSSSSSSS2SSSSSSSSSSSSSSSSSSSSSSSSSSSSj<!<<<
```
vertical_size=75
```
rr//////////////iii////r7+*~~+rivllllvvvvvvv^i/7*;;"!/?CSVSVVVVVVVVVVVVVVVVVVVVVVVVVyVS2xjtl/+!!!!+<<7rr/////////////////////////////////////////////////////////////////////////////////////////r<!~"*<ivlvvvvvv^^^^^^^vvvvvvv^^i//r7<+++!+<7ri^v?}jCx2SSSSSSS2222222VDDD
rr/////////////////////r<!~~*<ivllllvvvvvvvvvv^/<*""~<itxSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVyVV2jlir<++++<7r/////////////////////////////////////////////////////////////////////////////////////////r<+~"~+r^vvvvvvv^^^^^^^^^^^ii//77+++!++7r/iv?tjCx2SSSSVVSVVSSSS222222VDDD
///////////////////////7+***+r^lllllvvvvvvvvvvv^/7!~~!7v}xSVVVVVVVVVVVVVVVVSVVVVVVVVVVVVyyyyV2C}v/r7<<<77rr//////////////////////////////////////////////////////////////////////////////////////rr<*~~!</vvvvvvv^^^^^^^iii/r7<<++<<r/ivt}jCx2SVVVVVVVVVVSSSSSSSSSS222yDDD
/////////////////////r7+!**+7^lllllvvvvvvvv^^^^^^i7+**!rv}2SVVVVVVVVVVVVVVVSVVVVVVVVVVVVVVVyyVV2C}l^/7<+++<7rr////////i///ii/////////////////////////////////////////////////////////////////////rr7+!~~*<ivvvv^^^^^i///rrrr777r/^l?}jx2SVVVVVyVVVVVVVSSSSSSSSSSSSSS22yDDD
////////////////////r7+*~~!7ivllvv^^^^^^^^^^^i^^^^i7+**+/ljx2SVVVVVVVVVVVVVVVVSVVVVVVVVSSSVVVyVVV2xCtv/7+!*!!<7rr/////////i////i/////////////////////////////////////////////////////////////////rr7<+**~*</vvv^^ii/rr7777r/^v?tjCxSSSVVVVVVVVVVVSSSSSVSSSSSSSSSSSSS22yDDD
////////////////////r<!~~*+r^vvv^^^iiiiiiiiiii^^^^^ir+*!<i?}CxSVVVVVVVVVVVVVVVVVVSVVVSSSSSVVVVVVyVVVSxj?ir<!!!++<7rr////////i//ii//////////////////////////////////////////////////////////////rrrr7<+!***!7/iii/r7777r/^l?t}Cxx222SSVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSSSyDDD
///////////////////r<+*~~!</i^^i////rrrrrr//////i^^^ir<++7/v?}C2SVVVVVVVVVVVVVVVVSSSSSSSSSSVVVVVVVVVVyVSx}lir<+!!!<7rr////iiiiiiii/////////////////////////////////////////////////////////////rrrr77+!****!<77777rrivltjxx22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSyDD#
//////////////////r<!*~"~!<r//r77777<<<<<<<<7<77r/^^^^/r<<<7ivtCxVVVVVVVVVVVVVVVVSSSVVVVVSVVVVVVVVVVVyyyyV2Ctv/7<+++<7rr/////////////////////////iiiiii////////////////////rr////////////////rrr7777<+*~~**!+<r/ivlt}CxxSSSSVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSyD#b
///iii//i////////r7+*~"~*+<777<<<<<<++++++++++++<r/i^^^ir<++<r^?j2VVVVVVVVVVVSSVVVVVVVVVVVVVVVVVVVVVVVVVyyVV2C}?vi7<++++<<<r//////rrrrrr/////////ii/////rrrrrrr777rrrr777777777777<<<<<<<<<<<++!!!!!!!!!!<7r^lt}jC22SSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSyD#b
/////////////////r<!~""~!<77<<<++<<++++!!!!!!!!!+<7/i^^ir<!!!+7il}x2SVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVS2xCj?^/7+!!!++<7777777777777777777777<<<<<+++++++++++++++!!!!!!!!!!!!***********!!!++<<7r/ivl}C22SSSVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSy#b$
///////////ii////7+*"""*+777<<<++++!!+!!!!!!!!!!!+<7r/iir<++!!+<r^tjxSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVS2Ctv/7<+!!!++++++++++++++++++++++<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<7777rrrr/i^vll?t}jCxx2SSSSVSSVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVSSSSSSVSVVVSV#$0
///////////ii///7+*";"*+<<<<<<<++++!!!!!!!!!!!!!!!++77rr7<++!!!!+7ivtjx2SVVVVVVVVVVSVVVSSSVVVVVVVVVVVVSSVVVVVVVVVyVS2C}?vi/r777777777777rrrrr/////ivlllll???????ttttttt?ttttttttttttt}jjCCxxxxx22S2SSSSVVVVVSSSSSSSSVVSSSSSSSSSSSSSSSSSSSSSVVVVSVVVSSSSSVVSSSSSSVSSS2C2$$0
///////////////r+*";"~!<<<<<<++++++!!!!!!!!!!!!!!!!++<<<<<<+++!!!+<r/vtj2SSVVVVVSVVVVVVVVVVVVVVVVVVVSSSSSSSVVVVVVVVVSSxxCjj}}ttt??tttttt}}}}}}j}}}jx222222SSVVVVVVVVVVVVVVVVVVVVVVVVVVVyyyyyyyyVVVVVVSSVVVVSSSSSSSSSVVSSSSSSSSSSSSSSSSSSSSVVVVVVVVSSSSSSVVVVVVVVS22xC}lSN0
///////////////7!";;"*+<<++<+<+++!!!!!!!!!!!!!!!!!!!++++<<<<<<++!!!!+7i?jxSVVVVVVVVVSSVVSSVSSVSVVVVSVSSSVSSVVVVVVVVVVSSVVSSSSS2222222S22SSSSSSSSSSSSSSVVyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyVVVVVVVVVVVSSVVSSSSSSSSSSSSVVVVSSSSSSSSSSSSSSSSSSSSSVVVVVVSVVVSSSSVVVVVSS2xCj}tli/^t
//////////////r+~;_;~!+<<+++++++++++!!!!!!!!!!!!!!!!!!++<<<<<<++!!!***</l}x2SVVVVVSVSSSVSSSSSSSSSVSSVVVVVVVVVVVVVVVSSSVVVVVVSSSSSSSSSSSSSSVSVVVVVVVSSSSSSSSSSSSSVVVVVVVVVVVVVVVVVVVVVVSSSSVSVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVVVVVSSSSVVSSxCCjtllvvi/r7
/////////////r7!;__"*+<<<+++++++++++++!!!!+++!!!++++++++<<<<<<+++!**""*+7i?}C2VVVVVSSSSSSSSSSSSSVVSSVVVVSVVVVVVVVVVSVVVVSVSSVSSSSSVVSVSSSSVVSVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSSSSSSSSSSSSVVVVVVSSVVVVVVVVVVS2xjt?v^iii^^^ii
i////////ii/r7+~;_;~!+<<+++++!++++++++++++++++!++++++++++<<<<<<++!!*"""~*+r^tj2yyyVVVVSVSSVSSSSSSSSSSVVSSVSSSVVVVVVVSSSVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSVSSSSSVSVVSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVSVVVVVVVVS2C}?vi/r777r//i^^
iii/////ii//r7!";;"*!+++++++!!!++++++!++!+++!++++!!!+++++<<<<<<<++!**~"""~!<il}2SVVVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVSSVVVVVVVS2xjtvi/7<+++++<<7r/i
iiiiiiiii//r7+~;;"*!!++++++++!!!+++++++++++!!!!!!!!!+++++++<<<<<<++!!*~~~"~*+7i?j2SVVVVVVVSSSSSSSSSSSVSSSSSSSSSSSSSSVVVVVVVSSSSSSSSVVVVVSSSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVSSSSSVVVVVVVVVSC}l^/7<<++++++++<<<77
iiiiiiii///r<*";;~!++++++++++!+!!+!!!!++++++++++++!!+++++++++++++++++!!!*~~~*!+r^tCSVyyyVVS22222SSSSSVSSSSSSSSSSSSSSVVVVVVVVVVVVVVVVVVVVSSSSSSVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSSSSSSSSVVVVVVS2xjtvir7<++++!+++++!+++++
iiiii/ii//r<!";;"*+++++++++++++!!!!!!!!!!!!++++++++++++++++++++++++++++++!*****!<rvtCx222xCCjjCC22SSSVSSVVSSSSSSSSSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSVVSSSSSSSSSSSSSSVVVVVVVVVVVVVVVSSSVVVVVVVVSSSSSSSSSSSSSSSSSSSSSVVVVVVSSS2Ct?v/r<++<+++!!++++++++!!!
iiiiiii//r7+~;;;~!+<<<+++++++++!!!!!!!!!!!!!!++++++++++++!++++++++++++++++!!***~*!<r^lt}}t??tt}jx2SSVVSVVVVSSSSSSSSSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSVVVVSSSSSSSVSSVVVVVVVVVVSSSSSSSSSSSSSVVVVVSSSSSSSSSSSSSSSSSSSSSVVVVVS22xCtvir7<<++++++++++++++++++++
iiiiii///r<!";;"*+<7<<<<<<<++++!!!!!!!!!!!!!!!!!+!!!!!!!!!!+++++++++++++++++!**~~~~*!7ri^^^vltjC2SVVVSSSVSSSSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSVVVVVVVVSSSSSSSSSVVVVVVVVSSSSSSSSSSSSSSSVVVSSSSSSSSSSSSS222222SVVVVVV2xj}?^/7<<++++++<<+<<++++++++++++
iiiii////7!~";"~!<77<<<<<<<<++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!+++++++++++!!*~"""~*+7/^?}Cx2SSVVSSSSSSSSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSVVVVVVSSSSSSSSSSSSVVVVVVVSSSSSSSSSSSSSSSVVVSSVSSSSSSSS2xCCCCCCx2SSS2xCtvir<<++++<<<<<<<<<<<++++++++!!!
////i///r<!~;""*!<<<<++++++++++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!+++++++++!*"""~+7/l}x2SSSSSSSSSSSVVSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVSSVSVVVSSSS2xCj}}}}jCCj}t?vir<<+++++++<<<<<<<<<<<<<++++!!!+
///ii//r7+*"""~*!!!!+!!!!!!!!!!!****!!!!!!!!!!!!!!!!!!!!!!!************!!!++++<<<+*~;"~+rv}x2SSSSVSSSSSSSSSSSSSSSSSVVSVVVVVVVVSSSSSVVVSSSVVVVVVVVVVSSSSSSSSSSSSSSSSSVVSSSSSSSSSSSSSSSSSSSSSSSSSVVSSSSSSSSSSSSSVVVVVVVSSSSS2xCj}t??lll^i/r7<<+++++++<<<<<<<<<<+++++++!!!!!!
///i///7+*";"~*!!!**!!!!!!!!*******!!!!!!!!!!!!!!!!!!!!!********~~~~~~~~**!!+++<<!*";"*7^}xVVSSSVVSSSSSSSSSSSSSSSSSVVSVVVVVVSSSVVVVVVVSSSSVVVVVVVVVSSSSSSSSSSSSSSSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSSSSS2xCjtlvi/r7<<<+<<<<<<<<<<<<<<<<<<<<+++++!!!!!!!
///////<!";_;~*!****************!!!!!!!!!!!!!!!!!!!!!!!****~~~~~""""""""~~~*!!+++!~""*<i?xVyVSSSSVSSSSSSSSSSSSSSSSSVVVVVVVVVSSSSSSSSSVVSVVVVVVVVVVVSSSSSSSSSSSSSSSSSSVVSSSSSSSSSSSSSSSSSSSSSSSVSSSSSSSSSSSSSSSSSSSSVVVSSSSSS22C}?vi7+!!!!++<<<<<<<<<<<<<<<<<<<<+++++!!!!!!
ii////7+~;__;~*!*********!!**!!!!!!!!**!!!!!!!!!!!!!!!!**~~~~""";;;;;;;;;"~~*!++!*~"~+/lCSyyVSSVSSSSSSSSSSSSSSSSSSVVVVVVVVVVVVSSSSSSVVVVVVVVVVVVVVVSSSSSSSSSSSSSVVSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVSVSSSSSSSSSSSSSSVSSSSSSSS2xj?vr+!!!!++<<<<<<<<<<<<<<<<<<<++++++++!!!!
i////7+*";;;"~**********!!!!!!!!!!***!!!!!!!!!!!!!!!!!!**~~""";;;;_____;;"~**!!!*~~~!rv}2SVVSSSSSSSSSSSSSSSSSSVSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSSSSSSVVVVVVVVVVVVVVVSSSSSSSSSSSSSVSSSSSSSSS2Ct^r+!+++<<<<<<<<<<<<<<<<<++++++++++++!!!
i///r<*";;;"~****!***!!!!!!!!!*!!***!!!!!!!!!!!!!!!!!!!*~~"";;_________;"~**!!*~~;"*</?CSVVVSSSSSSSSSSSSSSSSSSVSSSVVVVVVVVVVSVVVVSVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVSSS222222xxxxx2SSSVVVVVSSSSSSSSSSSSSSSSSSSSSVVS2j?^7++++++<<<<<<<<<<<<<<++++++++++++++++
////7!~;;;"~!!!*!!*!!!!!!!!!!!!****!!!!!!!!!!!!!!!!!!!**~~";__________;"~**!!!*~";"*7v}xSSSSSSSSSSSSSSV2xxCCxCCCjj}}jxx2SVVVSSSSSSSSSVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxCCj}}tt?vvvv?}jCCx2SSSSSSSSSSSSSSSSSSSSSSSSVVS2Ct^7<++++<<<+<<<<<+++++++++++++++++++++
ii/r7*"_;"~*!!!!!!!!!!!!!!!*******!!!!!!!!!!!!!!!!!!!!*~~";;___::_____;"~*!++!~"""~+i?CSVVSSSSSSSSSSSS2xjt???lvv^/rriv?}C2SSSSSSSSSSSVVVVVVVSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22jtt?lllvir<+!+7/^ltCxSSSSSSSSSSSSSSSSSSSSSSSSVVS2C?ir+++++<<++<<<<<<<<+++++++++++++++++
ii/r+~;_;~*!+!!!!!!!!!!!!!!****!**!!!!!!!!!!!!!!!!!!!!*~~"";___::____;"~*!!++!""""*rvj2SVSSSSSSSSSSS22xjtlvvllli7+*!!<7il}C2SSSSSSSSSSVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2x}?l?tCxC}^7!""~*+r^?jxSSSSSSSSSSSSSSSSSSSSSSSVVVV2jl/<+!!!+++++<<<<<<<<<<<<<<<<<<<<<<<<
//r<!;__"*!++++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!*~~~"""""""""~~~*!!+++!*~"~*<itx2SSSSSSSSSSSSS2xC}llltCxx}vr+~"~*+/l}C2SSSSSSSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxC}l?tCyXXECv<~"""*+7il}xSSSSSSSSSSSSSSSSSSSSSSSSVVS2}vr+!!!++++<<<77777r7777777rrrrrr777
/r7+~__;"*+++++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!********!!!!+++++<7<+!*""~!/lj2SSSSSSSSSSSSSS2xj?^i^lCSV2}^!"_;"~+/l}xSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2xCtv^v}2EEyCl7~";;"*+rvtC2SSSSSSSSSSSSSSSSSSSSSSSSSVSx}^<!!!!!+<777rrrr///rr//////////rrr
/7+~;__;~*!++++!!!!!!**!!******************!!!!!+!!!!!!!!!!!!++++<<<77777rr<!*""*<^}xSVSSSS22222SSSS2xjl/<+<il?l/+;___;"!rvtC2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2xC?i7<rivlvr+~;___;~+/vtC2SSSSSSSSSSSSSSSSSSSSSSSSSVSSC?/+**!!+<7rr///////////////////rrr
r<*"___"~!!!++!!!!!***~**~~~~~~~~~"""""""~~**!!!!++!!!!!!+!!!+++<<<<77777rr<!*~"*rlC2SSSS2S22222222S2Cjl/!~~*!+*"_::::_;*7^tC2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22xj?i<*~~**~;____:_;~+/vtCx2SSSSSSSSSSSSSSSSS222SSSVVVV2jv7*~**+7rr///////////////////r//r
<!~;___"*!!!!!!!**~~~""""""""";;;;;;;;;;;;""~~*!!+++!!!!!+++++++++<<<7777rr<!~"~!itxSSSS22222222222S2xC}vr+*~~";__::::_;*7^tC2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2xCtv/+*~";;__::::_"*7/l}C2SSSSSSSSSSSSSSSSSSS2SSSSSVVVVxti+*~*+7r////r/////////////////rr
+*"_:_"~*!!!!***~~~"";;;;;;;______________;;;""~*!!++++++++++++++++<<<777r7+~";~<^}2SSSS2222222222SSSS2xC?i<!*~";;____;"!r^tC2SS22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22Ctli7!*"";;;__;"~+/vtjx2SSSSSSSSSSSSSSSSSSSSSSSSSSVVV2jvr!**+7r/////////rrrrrrrrrrr//rr
*"_::;"**!!!**~~~~"";;;_________::::::_:______;"~*!+++++++++++++++<<<<7777<!";"!/?CSSSS222222222SSSSSSSVSCt^r<+!*~***~*+7iljx2SS22SSSSSSSSSSSSSSS22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2xjtl^/7++!*~~*!<r^tj22SSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSxti<!*+7r/////////rrrrrrrrrrrrrrr
"_,,:"~*!!!!*~~~"";;;;________:::::::::::___::::;"~!!!+++++++++<++<<<<<77<+~;;*<vj2SSSSS222SSSSSVVVVVVVVVSxj}?lv^iiiiii^ltjx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2xCjt?l^i//i^v?}C2SSSSSSSSSSSSSSVSVVVVSSSSSSSSSSSSS2jlr+*!<r//////////r////rrrrrrrrr
_,,:;~*!*!****~"";;___________::::::::::::::::::_"~*!!++!++++<<<<<<<<<<<<+*~"~+itC2SSSSSSSSSSSSSVVVVVVVVVVVSSS2xCjjjjjjjCx2SSSSSSSSSSS22xxxxCCCxx22x22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSSS2xxCj}}jjCx2SSSSSSSSSSSSSSSSVSVVVVSSSSSSSSSSSSSSxti<!!<r///////////////rrrrrrrrr
:::;"*!!!!!**~~";;;________::::::::::::::::::,,:_"~*!!!!!+++<<<<<<7<<<<<+!~~~*r?C2SVVVVSSSSSSSVVVyyVVVVVVVVVVVVVSSSSS22SSSSSSSSSSSSSS2xC}?lvv^i^vvl?t}Cx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22SSSSVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSx}^7!!+r/////////////rrr//////rr
:_;~*!!!!!!**~~";;;________:::::::::::::::::::::_"~*!!!!!++<<<77777<<<<<+*~~*<^}2SSSSVVVVVVVVVVVVVyVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSS2xxjt^/7+!***!+</^ltCx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSV2jl/<+<r/i/////////////r//////rr
_;~!!+++!!***~~"";;_____:__:::::::::::::,,,,:::_;"~*!!!!++<<<<777777<<7<+*~~!7^tCCxxxx2SSSVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSSS22x}?v/7+*~""~!<r^?jx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVVVVVVVVVVSVVVVVVVSSSSSSSSSSSSSSSSSSSVSxt^r<<7///////////////////////r
_;*+++++!!!**~~""";;____:_:::::::::::::,,,,,,::_;"~*!++++<<<<<<77777<<7+!~""~!7i^vvl?t}jCx22SSVVVVVVVVVVVVVVVSSVVVVVVVSSSSSSSSSSSSSSSSSS2xCjtl^i/rr/iv?}x22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVVVVSS222222222xxxxxx2SSSSSSSSSSSSSSVS2jl/<+7/iiiii//////////rrrrrrrr
"~!<<+++!!!**~~~~""";;______::::::::::::,,,,,:_;"~*!!+++<<<77777777<<<<!~;::_;~!+!+<77r/^v?t}jC2SVVVVVVVVVVVVVVVVVSSSSVSSSSSSSSSSSSSSSSSSSSSS22xC}}jjCC2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVVSxj}}t????????????t}Cx2SSSSVSSSSSSS2C?i7++7/iii//i//////rrrrrrrrrr
*!+<<+++++!!**~~~~~~""";;;;;;;;;;;;;;________;"~**!++<<<<<777rrrr77<<<+*"_::_;~*!*!!!!++<<r/iv?}C2SVVVVVVVVVVVVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVSS2C}lv^ii//iiiiiiiii^vltjC2SVVVSSSSSSS2}vr+!+riiiiii//////rrrrrrrrrr
!+<<<++++++!!*******************!!!!!!!!****!!+++<<<77777777rrrrr777<<+*"__;~!<7rrrrrr77<<<<7/^?}CSVVVVVVVVSSVVVVVVVVVVVVVVSSVVVVVVVVVSSSSSSSVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVSVVS2C}l^i//rr///////////iivltjxSVVVVSSSSS2Cti<!!<r/iii//////////////rrr
+<<<<<<++++++!!!!+++++++++++<<77rrrrrrrr77777rrrrrrrrrrrrrrrrrrr7777<<!";;~!7/i^vvvvv^^^i/rr7rivtj2SVVVVVSVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSS2xj?vi//////iiiiii//////i^vtjxSSSVVSSSSS2jlr+!+<rii//iiiii///////////
+<<<<<<++++++++++<<<<<<<<7777r////////////ii///i////////rrrrrrr77777<+~;_;*</^vvlllvvvv^^^i/rr/^?}xSSVVSSVVVVVVVVVVVVVVVVVVSSVVVVVVVVSSSSVVVVVVVVVVSSSSSSSSVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVS2xj?vi///iii^^^^^^^^^iii///^vtjxSVVVSSSSSSxti<!!<r///iiiiii///////////
!+<<<+<++++++++++++<<<<<77777777777777777rr////ii/////rrrrrrr777777<!~;__;*</^vvvlvvvvv^^^^i/ri^?jxSSSVSVVVVVVVVVVVVVVVVVVVSSSVVVVVVVSSSVVVVVVVVVVVVSSSVVVVVVVVVVVSVSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSxC}l^iiiii^^^^^^^vvv^^^i/rr/^?jxSVSSSSSSSS2jlr+!+<7r/ii///i///rrrr////
~!+<++++!++++++++++++<<<<<<<<<<<<<<<++++++<7r////////rrr777777<7777+~;___;*</^vvvvvvv^^^^^^i/r/^?jxSSSVSSVVVVVVVVVVVVVVVVVVVVVVVVVVVVSSSSSSS22xxxCCCCCCCxxx2SSVVVSSVVVSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSxjtviiiiii^^^^^^vvvv^^^i/rr/il}xSVSSSSS2SS2x}^7!*!+<7rrrrrrrrrrrrrrrrr
~!+++!!!!!++++++++++++++<<<<<<<+++++!!!!!!+<7////////rrrr7777<<<77<*"____"*+rivvvvvvv^^^^^^i/r/^?j2SSVVSSVVVVVVVVVVVVVVSVVVVVVVVVVVVS2xCj}??lv^ii///iiii^vlt}}}jCCx2SSSVVSSSSSSSSSSSSSSSSSSSSSVVVVVSxjtvi//iii^^vvvvvvvvv^^i/rrriltC2SSSSSS22SS2C?i<**!+<77777777777777777
~!++!!!!!!+!!!++++!+++++++<<+++++++!!!!!!!++<7rr/////////rrr7777<<+*;____;~+r/i^^^vvv^^^^^^i//^?}x2SSSVVVVVVSSVVVVVVVVSSVVVVVVVVVSSxC}?v/7+!!!***!+<77rrrrr/ii^^l?t}CxSSVSSSSSSSSSSSSSSSSSSSSSVVVVVSxjtl^ii/ii^^^vvvv^vv^^^i/rr/^l}C2SSSSSS2SSSS2}v7!*!+<77777777777777777
~!++!!!!!!+!!!!!!!++++++++++++++!!!!!!!*!!!!+<<7rr///rrrrrrrrrrr7<+*;___;"*+<7r/i^^^^^^^^^^iiil}x2SVSSVVVSSSSSSVVVVVVSSVVVVVVVVVSS2jtvi7*~"""~!+7/ivllllllv^^iiii^vl?jxSSSSSSSSSSSSSSSSSSSSSSSSVVVVVSx}?^ii/ii^^^^vvvvv^v^^^ii/ivtjxSVVVSS22SSSS2Cl/+**!<<<<<<<<77<<<<<<<7
!+++++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!***!!!!!!+++<<<<<<<<<<<<<777<!~;__"~!<<7<7rrr/////iiiii^vtjxSVVVVSVVSSSVSSSSVVVVVVVSSSVVVVVSSx}li7!~"~*+7ilt}jCxxxxxCCj}t?lv^^vltjx2SSSSSSSSSSSSSSSSSSSSSSVVVVVS2C}l^iiiii^^^^^^^^^^^^^iiiv?jxSVVVSSS22SSSSSx}^7!*!+<<<<<<<<<<<<<<<<<
<<+++++!+!!!!!!!!!!!!!!!!!!!*!!!!!!!!!!*!!!**!!!!!!!!!!!!!!!!!+++!*~";"*</^^i/7<<<<<77rrrri^v?jx2VVVVVVVVVVVSSSSSVVVVVVVSVSVVVVSSSx}lr+*~~!<il}jCx2222222222xxC}?lv^v?}CxSSSSSSSSSSSSSSSSSSSSSSVVVSSVS2C}l^iiiiiiiiii^iiiiiiiiv?jxSVVVSSSSSSSSSSVSx?/+*!+<<<77777777777777
rr7<<+++!!!!!!!!!!!!!!!!!!**********!!!!!**!!!****************!!**~"";~+/l}j}tv/rrr7rr/ii^v?tjx2SVVVSVVVVVVSSSSVVVVVVVVVVVVVVVSSSS2}vr+***<i?jxxx2222222222222xjt?v^vltjxSSSSSSSSSSSSSSSSSSSSSSVVVVVVVS2Ctl^ii/iiiiiiiiiiii^vl?}xSVVVVSSSSSSSSSSVVSjv7!!!+7rrrrr7rrrrrr777
i/r7<+++!!!!!!!!!!!!!!!!!****************!!*****************!*****~"""~+it2VVSxjt??????t}jCxxx2SVVVVSVVVSVSSSVVVVVVVVVVVVVVVVVSSVVSC?^7++</v}Cx222222222222222xC}?vvvltjxSSSSSSSSSSSSSSSSSSSSSSSVVVVVVVV2xj}tlvvvllvvvvvll?t}jCx2SVVVSSSSSSSSSSSVyVxt^<!!<r/////r///rrrr77
i/7<<+++!!!!!!!!!!!!!!!!!!!!**********!*!*******************!*****~""""!r?xyEEyS222222222SSSSSSSVVVVVVVVSVVVVVVVVVVVVVVVVVVSVVVVVyV2}v/7<7/ljx2222222222222222xC}?vvvl}CxSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVS22xCjjjjjjjjjjjjCx22SSSSVVVSSSSSSSSSSSVyySxt/<++7/i^ii//////rrrr
r7<++!!!!!!!!!!!!!!!!*****!!*****!!!*****************************~~~";;~+i}SyEEyVyyyVVVVVVVVSSVSSVVVVVVVVVVVSSSSVVVVVVVVVVVSVSVVVVV2C?i777/vtx2SS2222S2SSSSS222C}?v^vl}C2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSSSSS2222222222222SSSSSSSVVSSSSSSSSSSSSSVVVV2jv7!!<r^vv^iii//////r
7<+!!!*!!!!!!!!!!!***************!****************************~*~~~~""""!r?CSyyyVVyVVVVVVVSSSVSSVVVVVVSSSVVVVVVVVVVVVSVVVVVSVSSVVVVSx}vi/rr/v}C2SS222SS222SS22xC}lv^vl}C2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSClr+!+rivv^iiiiiiii//
7<+!!!!!!!!!!!!!!************************************~************~~~"""~</?CSVyVVVVSSSSSSSSSSSSVVVVVVVVVVVVVVVVVVVVVSVVVVVSSSSSSVVV2x}l^/rr/^l}jxxx22SSS222xC}?l^i^v?}C2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVSxti<!+7/^v^ii///////r
/r7<<<++++++!!!!!!*******************!!!!!!!!**************!**!*****~~~~"*<i?CSVVVVVVSSSSSSSSSSVVVSSSVVVVVVVVVVVVVSSSSVVVSSSSSSVVVVVVSxjtlirrrri^l?t}}jjjj}}tl^i///^l}Cx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVS2jvr++<riv^i/////rrr7
//rr7777777<<<<<+++!!!!******!!!!!!!+++++++++++++++++++++++++++++!+!!!!~"~*<itCSSVVVVVSSSSSSSSSVVVSSSVSSVVVVVVVVVSSSSSVVVSSSSSSSVVVVVVV2xCt?vi//////iiiiii/////rr/^l}Cx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVV2C?i<+!<7/i/r7rr777<<
/r777777777rrrrrr77<<<++!!!+++<<<<<777rrrrrrrrrrrrrrrrrrr7777777777777<+*~~!7^txSVVVVVVSSSSSSVVSVVSSSVVVVVVVVVVVSSSSSSSSSSSSSSSSSSSVVVVVSS2xCjt?vv^iiii////ii^^vlltjCx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVSSx}vr!*!+7rr77777<<<<
<<+++++++<7r////////rrrrrrrrrrrrr//i/iiiiiiiiiiiiiiiiiiii//////////////r<!**!7i?j2SVVVVVVVVSSSSSVVVVVVSSVVSSSSSSSSSSSSSSSSSSSSSSSSSSVVVVVVSS222xCjj}}tttt}}}}}jCCxxx2SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxjl/+!!+<777<<<<<<<<
!!!!!!!!!!<7rrr//iiiiiiiiiiiiiiiiiiii^^^iii^iiiiiiiiiiiiiiiiiiiiiiiiii^i/7+!*!</lj2SVVVSSSSVSSSSSVVSVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSVVSVVSSSSSSS222222222SS222222222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2C?^7+!!+<<<<<<<<<<<
!!!******!!<77rrr///iiiiiiiiiiiii^^^i^^^iiiiiiiiiiiiiiiiiiii/iiiiiiiiiv^ir<+!!!7itC2VVVSSSSSSSSSSSVSSVSSVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS22SSSSSSSSSSSSSSSSSS2SSSSSSSS2SSSSx}vr+!!+<<<<<<<<<<<
**********!++<7rrrrr////iiiiiiiiii^^iiiiiiiiiiiiiiiiiiiiii///////r//////r7<<+!!+rltC2SSSSSSSSSSSSVVSSSSSSSVVSSSSSSSSSSSSSSSSSSSSSSSSSSVVSSSVSSSSSSSSSSSSSSSS222SS22SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2SSSSSSSSSSSSSSSSSSSSSSSSSSSS22SSSS2Cti+!!+<<<<<<<<<<<
************!+<<7777777rrr//iiiiiiiiiiiiiiiiiiiiiiiii/////////rrr77<<<<++++++!!+</l}C2SSSSSSSSSSSVVVVVVVSSSVVSSSVSSSSSSSSSSSSSSSSSSSSSSSSSSVVSSSSSSSSSSSSS2222222222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2SSSSSSSSSSSSSSSSSSSSSSSSSSSSS2SSSSS2}^<!!++<<<<<<<<<<
*****~~~~~~**!!!++!!+!!!+++<7rr//////////////////////////////rr77<++!**!***!+++++7i?}x2SSSSSSVSSSVVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2222S22SSSSSSS22222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2SS2jv7!!!!+<<<<<<<<<
****~~~~~~~~***************!++<<<777rrrr/rrrrrrrrrrrrr//////rrrr7<++!*****!!+<<+++r^?jxSSSSSSVVSSSSSVVVVVVSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS2S2222222222222SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSCti<!*!++<<<<<<<<
```
