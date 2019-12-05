from rest_framework import serializers

# ElectricPen:
from backend.models import Article, Topic, Comment

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')



# class UserSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     username = serializers.CharField(max_length=100)
        

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'updated_on', 'content', 'created_on', 'topics', 'status',)
        #  'slug', 'author', 'updated_on', 'content', 'created_on', 'topics', 'status')

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ('id', 'topic',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author','created_on','message','article',)