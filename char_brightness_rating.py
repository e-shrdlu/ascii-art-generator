from PIL import ImageGrab

char_range=range(32,127,20)
chars_to_fill_screen=211*72 # 211 per line, 72 lines

def get_brightness(im):
    brightness_level = []
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pixel_brightness = sum(im.getpixel((x,y)))/3
            brightness_level.append(pixel_brightness)
    brightness_level = sum(brightness_level)/len(brightness_level)
    return brightness_level

char_dict = {}

for i in char_range:
    char = chr(i)
    print(char*chars_to_fill_screen)
    char_brightness = get_brightness(ImageGrab.grab())
    char_dict[char] = char_brightness

print(char_dict,end='\n\n')


# bubble sort
char_list = []
for key in char_dict:
    char_list.append([key,char_dict[key]])

swapped = True
while swapped:
    swapped=False
    for i in range(len(char_list)-1):
        if char_list[i][1] > char_list[i+1][1]:
            char_list[i], char_list[i+1] = char_list[i+1], char_list[i]
            swapped=True
print('\n\n',char_list)


## sorted_list=[[' ', 0.33229166666666665], ['`', 5.551236014660452], ['.', 8.757084297839391], ['-', 11.728960423094009], ["'", 12.974945344646017], [',', 13.743113425918663], [':', 16.94783950617308], ['_', 17.139146894290036], [';', 21.782546296296175], ['"', 23.124488811728394], ['~', 24.175753118566597], ['*', 27.321388567427793], ['|', 28.073421424972555], ['!', 28.27049254110802], ['=', 28.853629758207507], ['+', 29.192478459404104], ['\\', 29.956127829230358], ['>', 30.033574459876533], ['<', 30.491064171797376], ['7', 32.824115869313246], ['r', 34.7669516782395], ['/', 35.35500932356709], ['i', 36.512959426435394], ['^', 37.37331211420298], ['v', 39.26505835262313], ['L', 39.338317418982676], ['Y', 40.053472222215724], ['c', 40.18070987654303], ['T', 40.721586612631505], ['J', 40.87141702031579], ['l', 40.96814236111094], ['s', 43.11892039607783], [')', 43.48233860600338], ['?', 43.653276427446386], ['(', 43.86541602368981], [']', 45.6063946759271], ['t', 45.631271219135776], ['{', 45.844833461923265], ['}', 46.822952031862606], ['5', 47.14719971709017], ['F', 47.3474569187481], ['j', 47.93222415133451], ['I', 48.0072627314811], ['1', 48.112827932078694], ['z', 48.20709153161492], ['[', 48.936381172666664], ['C', 48.9625369726777], ['x', 49.45005369085118], ['3', 49.91203060695742], ['2', 50.32380722725402], ['S', 52.329713220236904], ['n', 52.43085133749404], ['f', 52.52693447786288], ['Z', 52.91852141203654], ['V', 53.05974054781066], ['u', 53.232732124475795], ['e', 53.276077031882956], ['o', 53.84919302987539], ['4', 53.97883873480578], ['y', 54.134503922365155], ['a', 54.98579282401189], ['E', 55.614293981545124], ['U', 57.446820344453585], ['O', 57.44798418205316], ['X', 58.287995916755605], ['P', 58.34171923225244], ['A', 58.48091145840566], ['G', 60.709728652097176], ['k', 61.22812644675868], ['w', 61.22900945210827], ['K', 61.499180169752925], ['q', 61.77408693440717], ['N', 64.67374453462496], ['9', 64.7611985596852], ['h', 65.03714104302475], ['6', 65.48157937885952], ['H', 65.74255401235018], ['0', 65.75263792438354], ['m', 66.0214988427081], ['p', 66.2675090021477], ['Q', 66.42581645443546], ['$', 66.69614197538023], ['b', 68.7112911523403], ['R', 69.01750257203466], ['d', 69.03156185701133], ['#', 69.86811824845614], ['D', 70.33178642616743], ['g', 71.34052854934365], ['8', 71.37893422063964], ['%', 72.49967062111173], ['B', 74.05755208333771], ['M', 74.55160108020725], ['W', 76.77527199074862], ['@', 80.06521878218696], ['&', 84.33142891588427]]