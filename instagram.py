from instabot import Bot
from PIL import Image
from resizeimage import resizeimage
import praw,requests,random,os,time


if os.path.exists("meme.jpg.REMOVE_ME"):
    os.remove("meme.jpg.REMOVE_ME")
if os.path.exists("shitpost.jpg.REMOVE_ME"):
    os.remove("shitpost.jpg.REMOVE_ME")
elif os.path.exists("meme.jpg"):
    os.remove("meme.jpg")
elif os.path.exists("shitpost.jpg"):
    os.remove("shitpost.jpg")
else:
    print("The file does not exist")
def redditmeme():

    def simpleshitposts():
        print('shitposts')
        reddit = praw.Reddit(
            client_id = os.environ['CLIENT_ID'],
            client_secret = os.environ['CLIENT_SECRET'],
            user_agent="Oasis discordbot by /u/oasis-bot-discord"
        )
        print("Praw took creds")
        
        subreddit = reddit.subreddit('memes').new(limit=20)
        resp = []
        print("Chooser chose shit")
        for submission in subreddit:
            if submission.url.startswith('https://i'):
                resp.append({"url":submission.url,"title":submission.title})
        print("for loop ended")
        meme = random.choice(resp)
        memeurl = meme.get('url')
        memetitle = meme.get('title')
        image = requests.get(memeurl)
        file = open('shitpost.jpg','wb')
        file.write(image.content)
        file.close()
        
        
        programmersubreddit = reddit.subreddit('programmerhumor').new(limit=20)
        programmerresp = []
        print("Chooser chose shit")
        for programmersubmission in programmersubreddit:
            if programmersubmission.url.startswith('https://i'):
                programmerresp.append({"url":programmersubmission.url,"title":programmersubmission.title})
        print("for loop ended")
        programmermeme = random.choice(programmerresp)
        programmermemeurl = programmermeme.get('url')
        programmermemetitle = programmermeme.get('title')
        image = requests.get(programmermemeurl)
        file = open('meme.jpg','wb')
        file.write(image.content)
        file.close()

        programmerimg = Image.open('meme.jpg', 'r')
        img_w, img_h = programmerimg.size
        programmerimg = resizeimage.resize('thumbnail', programmerimg, [600,600])
        bgcolor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        background = Image.new('RGB', (750, 750), bgcolor)
        offset = ((50),(50))
        background.paste(programmerimg, offset)
        if os.path.exists("meme.jpg.REMOVE_ME"):
            os.remove("meme.jpg.REMOVE_ME")
        elif os.path.exists("meme.jpg"):
            os.remove("meme.jpg")
        else:
            print("The file does not exist")
        background.save('meme.jpg')
        print("file got saved")
        print(meme)
        memew = open('meme.txt',"a")
        memew.write(f'{meme}\n')
        memew.close()
        
        #pil
        
        img = Image.open('shitpost.jpg', 'r')
        img_w, img_h = img.size
        if img_h >= 700:
            img = resizeimage.resize('thumbnail', img, [600,600])
            print('big')
        else:
            img = resizeimage.resize('thumbnail', img, [600,600])
        bgcolor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        background = Image.new('RGB', (750, 750), bgcolor)
        offset = ((50),(50))
        background.paste(img, offset)
        if os.path.exists("shitpost.jpg.REMOVE_ME"):
            os.remove("shitpost.jpg.REMOVE_ME")
        elif os.path.exists("shitpost.jpg"):
            os.remove("shitpost.jpg")
        else:
            print("The file does not exist")
        background.save('shitpost.jpg')
        print("file got saved")
        print(meme)
        memew = open('shitpost.txt',"a")
        memew.write(f'{meme}\n')
        memew.close()
    # instagram
        programmerbot = Bot()
        shitpostCaption = f'{memetitle}\n#shitposting #offset #shitposts #india #memes #meme'
        programmerCaption = f'{programmermemetitle}\n#codedatt #programmerslife #python #python3 #backenddeveloper #androiddeveloper #webdevelopment #hacking #cprogramming #programmingmemes #java #deeplearning #softwaredeveloper #programming #coding #programmer #programminglife #coder #javascript #fullstackdeveloper #codingmemes #programmers #cplusplus #programmingisfun #developer #coders #neuralnetworks #html #webdeveloper #programmer #programmingmemes #memes'
        programmerbot.login(
        username=os.environ['SHIT_USERNAME'],
        password=os.environ['SHIT_PASSWORD']
        )
        programmerbot.upload_photo('shitpost.jpg', caption = shitpostCaption)
        time.sleep(32)
        programmerbot.upload_photo('meme.jpg', caption = programmerCaption)
    simpleshitposts()
    time.sleep(10800)
    redditmeme()
redditmeme()
