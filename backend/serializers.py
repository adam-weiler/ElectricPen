from rest_framework import serializers

# ElectricPen:
from backend.models import Article, Topic, Comment

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'updated_on', 'content', 'created_on', 'status')
        #  'slug', 'author', 'updated_on', 'content', 'created_on', 'topics', 'status')