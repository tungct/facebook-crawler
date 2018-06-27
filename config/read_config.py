
def getAccessToken(configFile):
    with open(configFile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    access_token = content[0]
    return access_token