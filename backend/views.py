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



from django.core import serializers
import json
from django.forms.models import model_to_dict


from rest_framework import viewsets
from backend.serializers import ArticleSerializer


# class FrontendAppView(View):
#     """
#     Serves the compiled frontend entry point (only works if you have run `yarn
#     run build`).
#     """

#     def get(self, request):
#         try:
#             with open(os.path.join(settings.STATIC_ROOT, 'index.html')) as f:
#                 return HttpResponse(f.read())
#         except FileNotFoundError:
#             logging.exception('Production build of app not found')
#             return HttpResponse(
#                 """
#                 This URL is only used when you have built the production
#                 version of the app. Visit http://localhost:3000/ instead, or
#                 run `yarn run build` to test the production version.
#                 """,
#                 status=501,
#             )


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    serializer_class = ArticleSerializer


class BlogView(View):

    def list_articles(self):
        all_articles = Article.objects.filter(status=1).order_by('-created_on')
        print(all_articles)
        # return HttpResponse(all_articles)
        serializer_class = ArticleSerializer

    def show_article(self, pk):
        article = Article.objects.get(pk=pk)
        comments = Comment.objects.filter(article=article)
        print(article)
        print(comments)
        # return HttpResponse(article)

        # serialized_obj = serializers.serialize('json', [ article, ])
        dict_obj = model_to_dict( article )
        serialized = json.dumps(dict_obj)

        return JsonResponse({
            # 'article': serialized_obj,
            'article': serialized,
            # 'comments': list(comments),
            'hey': 'hey'
        })


    # def article_topic(self, topic):
    #     articles = Article.objects.filter(status=1).filter(topics=topic).order_by('-created_on')
    #     print(articles)
    #     return HttpResponse(articles)
