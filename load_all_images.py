from PIL import Image

path=r"png/"


def load_images():
    fire_Logo = Image.open(path+"Firebase_Logo.png")
    adjust_Logo = Image.open(path+"adjust1.png")
    google_Logo = Image.open(path+"google.PNG")
    local_Logo = Image.open(path+"local3.png")
    apple_Logo = Image.open(path+"apple.png")
    
    return fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo

def load_winin_logo():
    return  Image.open(path+"winin.png")

