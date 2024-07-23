from http import HTTPStatus
from flask import request, Response

from app import app, USERS, POSTS


@app.post("/posts/<int:post_id>/reaction")
def set_reaction(post_id):
    if post_id < 0 or post_id >= len(POSTS):
        return Response(status=HTTPStatus.NOT_FOUND)

    data = request.get_json()
    user_id = data["user_id"]
    reaction = data["reaction"]

    if user_id < 0 or user_id >= len(USERS):
        return Response(status=HTTPStatus.NOT_FOUND)

    if reaction == "":
        reaction = "like"

    USERS[user_id].total_reactions += 1
    POSTS[post_id].reactions.append(reaction)
    return Response(status=HTTPStatus.OK)
