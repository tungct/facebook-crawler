import facebook
import sys
from config.read_config import getAccessToken
import setting

# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
app_id = ""
app_secret = ""
# access_token = app_id + "|" + app_secret
access_token = getAccessToken(setting.ACCESS_TOKEN_FILE)

# get name of post from argv
def getPage():
    return sys.argv[1]

def CrawlerPage():

    page = getPage()

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(page)

    # get 100 post in page
    posts = graph.get_connections(profile['id'], 'posts', limit="100")

    # crawl posts and save to file in data folder
    for idPost in range(0, 100):
        print("number of post : ", idPost)

        # get content post
        content_data = posts['data'][idPost]['message']
        file_path = setting.DIR_PATH_DATA + "/" + str(page) + ".txt"
        with open(file_path, "a") as commentFile:
            commentFile.write(content_data + "\n---end content---\n\n")
            commentFile.close()
        try:
            # get 100 comment in each post
            comments = graph.get_connections(posts['data'][idPost]['id'], 'comments', limit="100")
        except IndexError:
            try:
                comments = graph.get_connections(posts['data'][idPost]['id'], 'comments')
            except IndexError:
                pass
        countComment = 0

        # save comments to file
        for i in range(0, len(comments['data'])):
            countComment += 1
            try:
                print(comments['data'][i]['message'])
                with open(file_path, "a") as commentFile:
                    commentFile.write(comments['data'][i]['message'] + "\n\n")
                    commentFile.close()
                print("number of comment : ", countComment)
                print("---end post---\n\n")
            except IndexError:
                pass
            continue
        with open(file_path, "a") as commentFile:
            commentFile.write("---end post---\n\n")
            commentFile.close()
