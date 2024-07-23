import json
from http import HTTPStatus
from flask import request, Response

from app import app, USERS, POSTS, models


@app.post("/posts/create")
def post_create():
    data = request.get_json()

    post_id = len(POSTS)
    author_id = data["author_id"]
    text = data["text"]

    if author_id < 0 or author_id >= len(USERS):
        return Response(status=HTTPStatus.NOT_FOUND)

    post = models.Post(post_id, author_id, text)
    USERS[author_id].posts.append(post.id)
    POSTS.append(post)
    response = Response(
        json.dumps(post.to_dict()),
        HTTPStatus.CREATED,
        mimetype="application/json",
    )
    return response


@app.get("/posts/<int:post_id>")
def get_post(post_id):
    if post_id < 0 or post_id >= len(POSTS):
        return Response(status=HTTPStatus.NOT_FOUND)

    post = POSTS[post_id]
    response = Response(
        json.dumps(post.to_dict()),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response
