# Python imports:
import logging
import os

# Django imports:
from django.conf import settings
from django.http import HttpResponse, JsonResponse  # Used to send a response back to user.
from django.views.generic import TemplateView, View
from django.views.decorators.cache import never_cache

# Serve Single Page Application:
index = never_cache(TemplateView.as_view(template_name='index.html'))

# ElectricPen:
from backend.models import Article, Topic, Comment


class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.STATIC_ROOT, 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )


class BlogView(View):

    def list_articles(self):
        all_articles = Article.objects.filter(status=1).order_by('-created_on')
        print(all_articles)
        return HttpResponse(all_articles)

    def show_article(self, pk):
        article = Article.objects.get(pk=pk)
        comments = Comment.objects.filter(article=article)
        print(article)
        print(comments)
        return HttpResponse(article)


    # def article_topic(self, topic):
    #     articles = Article.objects.filter(status=1).filter(topics=topic).order_by('-created_on')
    #     print(articles)
    #     return HttpResponse(articles)
