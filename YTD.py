from pytube import YouTube
import ffmpeg 
import os 

reset='\033[0m'
red='\033[31m'
lightred='\033[91m'

def clrsc():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def Video():
    vdeo = yt.streams.filter(only_video=True,adaptive=True,file_extension='mp4')
    for index,i in enumerate(vdeo):
        i = str(i)
        i = i.split()
        print(str(index)+"."+i[3]+" "+i[4])
    optVdeo = int(input("Enter the option: "))
    if optVdeo not in range(index):
        clrsc()
        print(red+"Error Invalid Option"+reset)
        Video()
    else:
        print("Downloading")
        out_file = vdeo[optVdeo].download()
        os.rename(out_file, 'video.mp4')
        Audio()
        #Convertor()

        print("Downloaded")
        

def Audio():
    out_file = yt.streams.filter(only_audio=True)[0].download()
    os.rename(out_file, 'audio.mp3')
    print("asdas")



def Menu():

    print(f"{lightred}1.Download Video \n2.Download Audio{reset}")
    option = int(input("\nEnter the option: "))
    if(option == 1):
        Video()
    elif(option == 2):
        Audio()
    else:
        clrsc()
        print(red+"Error Invalid Option"+reset)
        Menu()


def Convertor():
    input_video = ffmpeg.input('/video.mp4')

    input_audio = ffmpeg.input('/audio.mp4')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(title+'.mp4').run()
    os.remove('video.mp4')
    os.remove('audio.mp3')

try:
    Link = input("Enter Youtube Link: ") 
    yt = YouTube(Link)
    title = yt.title
    clrsc()
    Menu()
except KeyboardInterrupt:
    clrsc()
    print(red+"Exiting"+reset)