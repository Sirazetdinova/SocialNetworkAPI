import re

from app import USERS


class User:
    def __init__(self, user_id, first_name, last_name, nickname, email):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email
        self.total_reactions = 0
        self.posts = []

    def __lt__(self, other):
        return self.total_reactions < other.total_reactions

    def to_dict(self):
        return dict(
            {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "nickname": self.nickname,
                "email": self.email,
                "total_reactions": self.total_reactions,
                "posts": self.posts,
            }
        )

    @staticmethod
    def is_valid_nickname(nickname):
        return re.match("^[A-Za-z0-9_]*$", nickname) and 2 < len(nickname) < 14

    @staticmethod
    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def get_leaderboard(reverse="asc"):
        if reverse == "desc":
            leaderboard = sorted(USERS, reverse=True)
        elif reverse == "asc":
            leaderboard = sorted(USERS)
        return [user.to_dict() for user in leaderboard]


class Post:
    def __init__(self, post_id, author_id, text):
        self.id = post_id
        self.author_id = author_id
        self.text = text
        self.reactions = []

    def to_dict(self):
        return dict(
            {
                "id": self.id,
                "author_id": self.author_id,
                "text": self.text,
                "reactions": self.reactions,
            }
        )
