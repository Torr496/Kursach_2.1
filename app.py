from flask import Flask, render_template, request

from utiis import get_post_with_comments_count, get_post_by_bk, get_comments_by_bk, get_post_by_word, get_posts_by_candidate_name

app = Flask(__name__)


@app.route('/' )
def page_index():
    posts = get_post_with_comments_count()
    return render_template("index.html", posts=posts, )


@app.route('/posts/<int:post_pk>' )
def page_post(post_pk):
    post = get_post_by_bk(post_pk)
    comments = get_comments_by_bk(post_pk)
    return render_template("post.html", comments=comments, post=post)


@app.route('/search')
def get_post_word():
    word = request.args['word']
    posts = get_post_by_word(word)
    posts_count = len(posts)

    return render_template("search.html", posts=posts, posts_count=posts_count)

@app.route('/users/<username>' )
def page_post_by_name(username):
    posts = get_posts_by_candidate_name(username)

    return render_template("user-feed.html", posts=posts)

if __name__ == "__main__":
    app.run()
