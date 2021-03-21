def banner():
    clrsc()

    print(lightred+'''      ,-.
     / \  `.  __..-,O
    :   \ --''_..-'.'               _________ ______  
    |    . .-' `. '.       |\     /|\__   __/(  __  \ 
    :     .     .`.'       ( \   / )   ) (   | (  \  )
     \     `.  /  ..        \ (_) /    | |   | |   ) |
      \      `.   ' .        \   /     | |   | |   | |
       `,       `.   \        ) (      | |   | |   ) |
      ,|,`.        `-.\       | |      | |   | (__/  )
     '.||  ``-...__..-`       \_/      )_(   (______/ 
      |  |
      |__|    \033[96m                   Youtube Downloader\033[91m
      /||\    \033[96m                   Author > RobinHood\033[91m
     //||\\   \033[96m              https://github.com/The-Robin-Hood\033[91m
    // || \\               
 __//__||__\\__
'--------------' '''+reset)

def clrsc():                                                                                    # As the name suggest it clears the screen
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def Video():                                                                                    # For Downloading Video
    vdeo = yt.streams.filter(only_video=True,adaptive=True,file_extension='mp4')
    for index,i in enumerate(vdeo):
        i = str(i)
        if "av01" in i :                                                                        # To avoid the codec format
            continue
        i = i.split()
        print(str(index)+". "+i[3]+" "+i[4])                                                    #Prints the available formats to download

    optVdeo = int(input("Enter the option: "))                                                  # Ask the user to select an format
    if optVdeo not in range(index):                                                             # If the user gives the options which is not in the list Displays an Error
        clrsc()
        print(red+"Error Invalid Option"+reset)
        Video()
    else: 
        print("Downloading") 
        out_file = vdeo[optVdeo].download()
        os.rename(out_file, 'temp.mp4')
        Audio()
        Convertor()
        

def Audio():                                                                                    # Audio Downloading   
    out_file = yt.streams.filter(only_audio=True)[0].download()
    os.rename(out_file, 'temp.mp3')



def Menu():                                                                                     # Shows the Menu
    print(f"{lightblue}\nChoose an Option :")
    print(f"{lightred}1.Download Video \n2.Download Audio{reset}")
    option = input("\n>>> ")
    if(option == '1'):
        Video()
    elif(option == '2'):
        Audio()
    else:
        banner()
        print(red+"\nError Invalid Option"+reset)
        Menu()


def Convertor():                                                                                 # Merges the Video and Audio
    print("Merging.....")
    input_video = ffmpeg.input('./temp.mp4')
    input_audio = ffmpeg.input('./temp.mp3')
    video_path = 'out.mp4'
    out = ffmpeg.output(input_video, input_audio, video_path, vcodec='copy', acodec='aac', strict='experimental')
    out.run()
    print("Deleting the unwanted files")
    os.remove('temp.mp4')
    os.remove('temp.mp3')



def start():
    try:
        Link = input("Enter Youtube Link: ")                                                     # Gets the Link from User
        global yt , title
        yt = YouTube(Link)
        title = yt.title                                                                         # Assign the title from given link
        banner()
        Menu()                                                                                    # Calls the Menu Func
        
    except KeyboardInterrupt:
        clrsc()
        print(red+"Exiting"+reset)

    except Exception as e :
        if type(e).__name__ == 'RegexMatchError':
            banner()
            print(red+"\nEnter a valid URL\n"+reset)
            start()
        else:
            banner()
            print(type(e).__name__)
            print(red+"Something Went Wrong !! Try again"+reset)
            start()

# initiating variables
reset='\033[0m'
red='\033[31m'
lightred='\033[91m'
lightcyan='\033[96m'
lightblue='\033[94m'


# Importing Required Modules
import os
import sys 
try:
    from pytube import YouTube
    import ffmpeg
except:
    print(red + "\nInstall Required Modules ")
    print("pip install -r requirements.txt\n" +reset)
    sys.exit()    
 

#Program starts 
if __name__=="__main__":
    banner()
    start()