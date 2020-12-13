import random
import emoji

def my_emoji(str):
    multiple = random.randint(1,6)
    return emoji.emojize(str)*multiple

def make_reply_insta():
    reply = random.choice(reply_list_insta)
    reply_last = random.choice(reply)
    return reply_last

reply_list_insta = [
    [my_emoji(":thumbs_up:")],
    [my_emoji(":grinning_face_with_smiling_eyes:"), my_emoji(":clapping_hands:")],
    [my_emoji(":red_heart:"),my_emoji(":yellow_heart:"),my_emoji(":blue_heart:")],
    [my_emoji(":grinning_squinting_face:"), my_emoji(":winking_face:")]
]


