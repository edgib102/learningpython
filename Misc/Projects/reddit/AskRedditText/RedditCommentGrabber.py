import praw

username = 'edgib102'
password = 'Edgib101'
path = "/Users/bridgibson/Documents/GitHub/learningpython/Misc/Projects/reddit/AskRedditText/files/test.txt"
afile = open(path, 'w')
afile.truncate

reddit = praw.Reddit(client_id = 'syWXRTZJoN3LHw' , client_secret = 'fk1c1MVSD1XKW1wr3w7wYqpjBgg', username = username, password = password, user_agent = "prawtest")

subreddit = reddit.subreddit('askreddit')
subreddit_hot = subreddit.hot(limit=1)

for submission in subreddit_hot:

    #print(dir(submission))
    submission.save()
    comments = submission.comments

    for comment in comments:
        try:
            afile.write(comment.body)
            afile.write('\n\n')
        except:
            break

print("ended")

#assume that the output to the .txt is the final with formatting
