from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    return Article.objects.get(id=article_id)
