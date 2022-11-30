from praw import Reddit
from praw.models import Submission
import json
import datetime
import os

client_id = "AVAYjUeLZ4WGx5Yn-ZYdqQ"
client_secret = "t8QTAMhZ16rjZrj4_gWkF1KHspgtkA"

reddit = Reddit(user_agent="asdf")

def get_submission_for_url(url:str)->Submission:
    return reddit.submission(url=url)

def get_comments_for_post(submission:Submission):
    submission.comments.replace_more(limit=None, threshold=0)
    return[{"content": c.body, "score": c.score} for c in submission.comments.list()]

def get_top_n_posts_for_subreddit(subreddit:str, time_filter="all"):
    return list(reddit.subreddit(subreddit).top(time_filter=time_filter))
    
if __name__ == "__main__":
    if not 'comments' in os.listdir("."):
        os.mkdir("./comments")

    # for sub in ["buddhism", "hinduism", "atheism", "christianity"]:
    for sub in [ "christianity"]:
        print(f"starting lookup for posts in {sub}")
        posts = get_top_n_posts_for_subreddit(sub, time_filter="month")
        print("retrieved top posts")
        print("loading comments")
        comments = []
        for i, post in enumerate(posts):
            comments.append(
                {
                    'post_id': post.id,
                    'post_name': post.name,
                    'post_permalink': post.permalink,
                    'post_score': post.score,
                    'comments': get_comments_for_post(post)
                }
            )
            print(f"{i+1}/{len(posts)}")
        with open(f"comments/{str(datetime.datetime.now())} {sub}.json", "w") as f:
            f.write(json.dumps(comments))
    

    # for e in posts:
    #     print(get_comments_for_post(e))
    # res = get_comments_for_post(url="https://www.reddit.com/r/MacOS/comments/z7v7sn/appeared_after_turning_on_macbook_normally_i_dont/")
    # print(res)