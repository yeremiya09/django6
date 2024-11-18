from os.path import exists

from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:

    # likes = list(Like.objects.filter(user_id=user_id, article_id=article_id))
    # if likes:
    #     raise Exception
    return Like.objects.create(user_id=user_id, article_id=article_id)


def undo_like(user_id: int, article_id: int) -> None:
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    like.delete()
