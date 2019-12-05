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
from rest_framework.response import Response
from backend.serializers import ArticleSerializer, TopicSerializer, CommentSerializer



from rest_framework import status
from rest_framework.decorators import api_view




from rest_framework.views import APIView



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


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    serializer_class = ArticleSerializer

    # def list(self, request):
    #     queryset = Article.objects.filter(status=1).order_by('-created_on')
    #     serializer = ArticleSerializer(queryset, many = True)
    #     return Response(serializer.data)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects
    serializer_class = ArticleSerializer

# class TopicViewSet(viewsets.ModelViewSet):
#     queryset = Topic.objects
#     serializer_class = TopicSerializer



class TopicList(APIView):
    """
    List all topics, or create a new topic.
    """
    def get(self, request, format=None):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicDetail(APIView):
    """
    Retrieve, update or delete a code topic.
    """
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise HTTP404

    def get(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        topic = self.get_object(pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects
    serializer_class = CommentSerializer

# class UserViewSet(ListCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class BlogView(View):

    def list_articles(self):
        all_articles = Article.objects.filter(status=1).order_by('-created_on')
        print(all_articles)
        # return HttpResponse(all_articles)
        serializer_class = ArticleSerializer

    def show_article(self, pk):
        article = Article.objects.get(pk=pk)
        # comments = Comment.objects.filter(article=article)
        # print(article)
        # print(comments)
        # # return HttpResponse(article)

        # # serialized_obj = serializers.serialize('json', [ article, ])
        # dict_obj = model_to_dict( article )
        # serialized = json.dumps(dict_obj)

        return JsonResponse({
            # 'article': serialized_obj,
            'article': 'serialized',
            # 'comments': list(comments),
            'hey': 'hey'
        })


    # def article_topic(self, topic):
    #     articles = Article.objects.filter(status=1).filter(topics=topic).order_by('-created_on')
    #     print(articles)
    #     return HttpResponse(articles)
