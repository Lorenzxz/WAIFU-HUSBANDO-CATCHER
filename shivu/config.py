class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6735787636"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002029618511
    TOKEN = "6545872361:AAGx_ZIAHg3J_DBZn1J0H9YfkgKPOn7ioCw"
    mongo_url = "mongodb+srv://Lorenzxz:iamatomic@cluster0.xnnkihu.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "lorenznimesupport"
    UPDATE_CHAT = "lorenznimesupport"
    BOT_USERNAME = "lorenznime_bot"
    CHARA_CHANNEL_ID = "-1002029618511"
    api_id = 22411806
    api_hash = "5fe949ec29369a8cb1e7d38ccc485e92"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
