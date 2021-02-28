from PIL import Image, ImageGrab
import time
import cv2
import sys
import os
import socket


def print_large_block(text):
    global save_ascii_art_in
    print('',end='',flush=True)
    sys.stdout.flush()
    print('\n',end=text, flush=True)
    if save_ascii_art_in:
        with open(save_ascii_art_in, 'a') as f:
            f.write(text+'\n')


def get_ascii_from_image(im):
    global char_list, mirrored
    lines=[]
    x_range = range(im.size[0])[::-1] if mirrored else range(im.size[0])
    for y in range(im.size[1]):
        line=[]
        for x in x_range:
            pix = sum(im.getpixel((x,y)))/3
            char_list_pos = int((len(char_list)-1)*pix/255)
            line.append(char_list[char_list_pos])
        lines.append(''.join(line))
    return '\n'.join(lines)


def get_video_frms(path, format="cv2"):
    cap = cv2.VideoCapture(path)#,cv2.CAP_DSHOW)
    # print(cap,cap.isOpened())
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            if format=='PIL':
                yield cv2_to_PIL(frame)
            else:
                yield frame
        else: # end of file
            cap.release()
            cv2.destroyAllWindows()
            break


def cv2_to_PIL(frame):
    color_mode_converted = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # cv2.imshow('image',frame)
    pil_im = Image.fromarray(color_mode_converted)
    return pil_im


def video_chat(webcam_id):
    webcam_id = int(webcam_id)
    s = socket.socket()
    role = input('a) host\nb) join\n>>')
    if role == 'a':
        host = '0.0.0.0' # socket.gethostname()
        port = int(input('port: '))
        s.bind((host,port))
        print("port:",port,"\nIP:",socket.gethostbyname(host),"\nwaiting for connection...")
        s.listen(1)
        conn, addr = s.accept()
        print(addr, "has connected")
    elif role == 'b':
        host = input('IP: ')
        port = int(input('port: '))
        conn=s
        conn.connect((host,port))
    else:
        return -1
    for frame in get_video_frms(webcam_id, 'PIL'):
        conn.send((get_ascii_from_image(frame)+'\n\n').encode())
        recv_frms = str(conn.recv(16384).decode()).split('\n\n')
        if len(recv_frms) > 50: # if this computer is really behind, just reset
            conn.recv(2**32) # clear buffer
            continue
        for frm in recv_frms:
            print_large_block(frm)



def show_screenshot():
    # imported inside function so as to not require install for everything else
    failed_import = False
    try:
        import pyautogui
    except ModuleNotFoundError:
        print('you must install pyautogui for this feature. try running "python -m pip install pyautogui"')
        failed_import=True
    try:
        import keyboard
    except ModuleNotFoundError:
        print('you must install keybord module for this feature. try running "python -m pip install keyboard"')
        failed_import=True
    if failed_import:
        return -1

    print('press shift @ top left corner')
    while not keyboard.is_pressed('shift'):
        pass
    first_pos = pyautogui.position()
    print('got first corner, press shift @ bottom right corner')
    time.sleep(1)
    while not keyboard.is_pressed('shift'):
        pass
    second_pos = pyautogui.position()
    screenshot = ImageGrab.grab(bbox=(first_pos[0],first_pos[1],second_pos[0],second_pos[1]))
    print('done')
    print_ascii_from_im(screenshot)


def print_ascii_from_im(im):
    global horizontal_size, vertical_size, save_ascii_art_in
    horizontal_size = int(vertical_size*horizontal_scale*im.size[0]/im.size[1])
    im=im.resize((horizontal_size,vertical_size))
    ascii_art = get_ascii_from_image(im)+'\n'
    print_large_block(ascii_art)


def play_ascii_video(path):
    global frames_to_play
    i=0
    for im in get_video_frms(path, 'PIL'):
        print_ascii_from_im(im)
        i+=1
        if i > frames_to_play and frames_to_play != 0:
            break


def download_yt_video(url, path):
    try:
        from pytube import YouTube # imported inside function so as to not require install for everything else
    except ModuleNotFoundError:
        print('you must install pytube for this feature. try running "python -m pip install git+https://github.com/pytube/pytube"')
        return -1

    yt = YouTube(url)
    yt.streams.first().download(path)
    path = os.path.join(path,yt.title+'.mp4')
    return path


def play_webcam(num):
    play_ascii_video(int(num))


def show_saved_picture(path):
    im = Image.open(path)
    print_ascii_from_im(im)


def play_youtube_video(url):
    global yt_video_path
    if not yt_video_path:
        print('you need to set yt_video_path in settings')
        return -1
    if not os.path.exists(yt_video_path):
        os.mkdir(yt_video_path)
    video_path = download_yt_video(url, path=yt_video_path)
    play_ascii_video(video_path)
    os.remove(video_path)


def read_ascii_art_file(path):
    with open(path,'r') as f:
        txt = []
        for line in f:
            if len(line) <= 1:
                print_large_block(''.join(txt))
                txt=[]
                time.sleep(0.025)
            else:
                txt.append(line)


def change_settings():
    global char_list,horizontal_scale,vertical_size,yt_video_path,frames_to_play,mirrored,save_ascii_art_in
    while 1:
        print('syntax: [var]=[value], or type "back" to go back to main menu')
        print(f"""
        float horizontal_scale={horizontal_scale}
        int vertical_size={vertical_size}
        str yt_video_path={yt_video_path}
        int frames_to_play={frames_to_play}
        int mirrored={mirrored}
        str save_ascii_art_in={save_ascii_art_in}""")
        user_input = {}
        user_input['raw'] = input('>> ')
        if user_input['raw'] == 'back':
            break

        # parses input. stores variable to change in user_input['var'], and value to change it to in user_input['val']
        user_input['var'] = ''
        user_input['val'] = ''
        i = 'var'
        for char in user_input['raw']:
            if char == '=' and i == 'var':
                i = 'val'
            else:
                user_input[i]+=char
        print(user_input)
        # change value. theres gotta be a better way to do this
        if user_input['var'] in 'horizontal_scale':
            horizontal_size = float(user_input['val'])
        elif user_input['var'] in 'vertical_size':
            vertical_size = int(user_input['val'])
        elif user_input['var'] in 'yt_video_path':
            yt_video_path = user_input['val']
        elif user_input['var'] in 'frames_to_play':
            frames_to_play = int(user_input['val'])
        elif user_input['var'] in 'mirrored':
            mirrored = int(user_input['val'])
        elif user_input['var'] in 'save_ascii_art_in':
            save_ascii_art_in = user_input['val']


def stop_execution():
    global go
    go = False


def ui():
    global go
    go = True
    # options, letter is how you select the option, first item is name, second is options required, third is func
    choices = {'a':['saved video','path',play_ascii_video],'b':['saved picture','path',show_saved_picture],'c':['screenshot','',show_screenshot],'d':['webcam','webcam id (probably 0)',play_webcam],'e':['youtube video', 'url', play_youtube_video], 'f':['read saved ascii art', 'path',read_ascii_art_file], 'g':['video chat (expirimental)','webcam id (probably 0)',video_chat], 'h':['settings', '',change_settings], 'i':['quit','', stop_execution]}
    while go:
        print('\n'.join([opt+') '+choices[opt][0] for opt in choices.keys()])) # prints menu
        try:
            # gets user choice for func to exec
            choice=''
            while choice not in choices.keys():
                choice=input('> ')

            # gets values to pass to chosen func
            if choices[choice][1]:
                print('values needed:',choices[choice][1])
                value = input('>> ')
                choices[choice][2](value) # calls chosen function with value given
            else:
                choices[choice][2]() # calls chosen function if doesnt need value

        except Exception as e:
            print(e,'\nsomething broke bro idk') # probably not best practice but idk what else to do


def main(): # do I even need a main function? why do i have this?
    ui()


char_list=list(' `.-\',:_;"~*!+<7r/i^vl?t}jCx2SVyEOXGqN0$b#D8%MW@&')
horizontal_scale = 2
vertical_size = 75
yt_video_path = None
frames_to_play = 0
mirrored = 0
save_ascii_art_in = None # if not blank, will store each frame in this text file

go = True


if __name__=='__main__':
    main()
