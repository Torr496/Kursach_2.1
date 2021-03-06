import json
import pprint


def get_posts():
    with open("data/data.json", "r", encoding="utf-8") as fp:
        posts = json.load(fp)
    return posts


def get_comments():
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    return comments


def get_post_with_comments_count():
    posts = get_posts()
    comments = get_comments()

    for index, post in enumerate(posts):

        comments_count = 0

        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        posts[index]["comments_count"] = comments_count

    return posts


def get_post_by_bk(post_pk):
    posts = get_posts()
    for post in posts:
        if post["pk"] == post_pk:
            return post


def get_comments_by_bk(post_pk):
    with open("data/comments.json", "r", encoding="utf-8") as fp:
        comments = json.load(fp)
    post_comments = []
    for comment in comments:
        if comment["post_id"] == post_pk:
            post_comments.append(comment)

    return post_comments


def get_post_by_word(word):
    post_found = []

    posts = get_posts()
    comments = get_comments()

    for post in posts:
        if word.lower() in post["content"].lower():
            post_found.append(post)

    for index, post in enumerate(post_found):

        comments_count = 0

        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        post_found[index]["comments"] = comments_count


    return post_found


def get_posts_by_candidate_name(username):
    post_found = []

    posts = get_posts()
    comments = get_comments()

    for post in posts:
        if username.lower() == post["poster_name"].lower():
            post_found.append(post)

    for index, post in enumerate(post_found):

        comments_count = 0

        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        post_found[index]["comments"] = comments_count

    return post_found




