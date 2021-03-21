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

def progress_Check(stream = None, chunk = None,remaining=None):
    percent = (100*(file_size-remaining))/file_size
    percent = str(int(percent))
    downloaded_size = int(file_size/1e+6 - remaining/1e+6) 
    print("Downloading : "+percent +"% ("+ str(downloaded_size)+" MB)",end="\r")

def Video():                                                                                    # For Downloading Video
    banner()
    print(f"{lightblue}\nChoose an Option :\n"+reset)
    vdeo = yt.streams.filter(only_video=True,adaptive=True,file_extension='mp4')
    for index,i in enumerate(vdeo):
        i = str(i)
        if "av01" in i :                                                                        # To avoid the codec format
            continue
        i = i.split()
        print(str(index)+". "+i[3]+" "+i[4])                                                    #Prints the available formats to download

    optVdeo = int(input(reset+"\n>>> "))                                                  # Ask the user to select an format
    if optVdeo not in range(index):                                                             # If the user gives the options which is not in the list Displays an Error
        clrsc()
        print(red+"Error Invalid Option"+reset)
        Video()
    else:
        global file_size
        file_size = vdeo[optVdeo].filesize
        banner() 
        print("\033[92mDownloading "+title+reset+f"\n File Size = {int(file_size/1e+6)} MB \n") 
        out_file = vdeo[optVdeo].download()
        os.rename(out_file, 'temp.mp4')
        Audio(1)
        Convertor()
        banner()
        again()
        

def Audio(x):                                                                                    # Audio Downloading   
    global file_size
    file_size = yt.streams.filter(only_audio=True)[0].filesize
    out_file = yt.streams.filter(only_audio=True)[0].download()
    
    if x == 0 :
        os.rename(out_file, "./Downloaded/"+title+'.mp3')
        banner()
        again()
    elif x == 1:
        os.rename(out_file, 'temp.mp3')



def Menu():                                                                                     # Shows the Menu
    print(f"{lightblue}\nChoose an Option :")
    print(f"{reset}\n1.Download Video \n2.Download Audio")
    option = input("\n>>> ")
    if(option == '1'):
        Video()
    elif(option == '2'):
        Audio(0)
    else:
        banner()
        print(red+"\nError Invalid Option"+reset)
        Menu()


def Convertor():                                                                                 # Merges the Video and Audio
    print("Merging.....")
    input_video = ffmpeg.input('./temp.mp4')
    input_audio = ffmpeg.input('./temp.mp3')
    video_path = './Downloaded/'+title+'.mp4'
    out = ffmpeg.output(input_video, input_audio, video_path, vcodec='copy', acodec='aac', strict='experimental')
    out.run()
    print("Deleting the unwanted files")
    os.remove('temp.mp4')
    os.remove('temp.mp3')



def start():
    try:
        Link = input(lightblue+"\nEnter Youtube Link: "+reset)                                                     # Gets the Link from User
        global yt , title
        yt = YouTube(Link,on_progress_callback=progress_Check)
        title = yt.title                                                                         # Assign the title from given link
        for unwanted in ['"','|','?',':','*','\\','/']:
            if unwanted in title:
                title = title.replace(unwanted," ")
        banner()
        Menu()                                                                                    # Calls the Menu Func
        
    except KeyboardInterrupt:
        clrsc()
        for rm in ['temp.mp4','temp.mp3']:
            if os.path.exists(rm):
                os.remove(rm)
        
        print(red+"Exiting"+reset)
        sys.exit()

    except Exception as e :
        for rm in ['temp.mp4','temp.mp3']:
            if os.path.exists(rm):
                os.remove(rm)
        if type(e).__name__ == 'RegexMatchError':
            banner()
            print(red+"\nEnter a valid URL\n"+reset)
            start()
        else:
            banner()
            print(type(e).__name__)
            print(red+"Something Went Wrong !! Try again"+reset)
            start()

def again():
    Chck = input(f"{lightblue}\nDo You want to Download another video ? (Y/N) :")
    if Chck in ['Yes','yes','YES','y','Y']:
        start()
    elif Chck in ['NO','No','no','N','n']:
        clrsc()
        print(lightred+"\nBYE ...\n"+reset)
        sys.exit()
    else:
        banner()
        print(red+"\n Invalid Option \n"+reset)




# initiating variables
reset='\033[0m'
red='\033[31m'
lightred='\033[91m'
lightcyan='\033[96m'
lightblue='\033[94m'
cyan='\033[36m'
file_size = 0


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
 

# Program starts 
if __name__=="__main__":
    banner()
    start()