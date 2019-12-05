from django.urls import include, path
from rest_framework import routers

# from rest_framework.urlpatterns import format_suffix_patterns


from backend import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'articles', views.ArticlesViewSet)
router.register(r'article', views.ArticleViewSet)
# router.register(r'topics', views.TopicViewSet)
router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),


    path('topics/', views.topic_list),
    path('topics/<int:pk>/', views.topic_detail),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = format_suffix_patterns(urlpatterns)