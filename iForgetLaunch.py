import praw
import os
import re
import pdb

reddit = praw.Reddit(user_agent='iForgetBot v1.0',
                     client_id='xxxxxxxxx',
                     client_secret='**********************', #Add your client secret replacing ******, you will get it on regestring account.
                     username='iForgetBot',
                     password='**********')

print("Which Sub you want to hunt?")
sub = input()

# we haven't run this code before so,
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# If we have ready run this code, you know what I mean
else:
    # Read the file into the list and remove empty value
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit(sub)
for submission in subreddit.new(limit=10):

    # if havent reply to this code before
    if re.search("What do you", submission.title, re.IGNORECASE):
        submission.reply(""" Well to be perfectly honest, in my humble opinion, of course without offending anyone who thinks differently from my point of view, but also by looking into this matter in a different perspective and without being condemning of one's view's and by trying to make it objectified, and by considering each and every one's valid opinion, I honestly believe that I completely forgot what I was going to say. """)
        print("Bot replying to : ", submission.title)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

# Update the list on the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
