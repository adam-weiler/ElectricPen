from django.urls import include, path
from rest_framework import routers

# from rest_framework.urlpatterns import format_suffix_patterns


from backend import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'articles', views.ArticlesViewSet)
# router.register(r'article', views.ArticleViewSet)
# router.register(r'topics', views.TopicViewSet)
# router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),


    path('topics/', views.TopicList.as_view()),
    path('topics/<int:pk>/', views.TopicDetail.as_view()),

    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = format_suffix_patterns(urlpatterns)