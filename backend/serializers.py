from rest_framework import serializers

# ElectricPen:
from backend.models import Article, Topic, Comment

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'updated_on', 'content', 'created_on', 'topics', 'status',)
        #  'slug', 'author', 'updated_on', 'content', 'created_on', 'topics', 'status')

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('topic',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author','created_on','message','article',)