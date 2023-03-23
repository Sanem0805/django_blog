from rest_framework.viewsets import ModelViewSet
from .models import Article, Tag
from .serializers import ArticleSerializer
from .serializers import ArticleSerializer, ArticleListSerializer, TagSerializer

'''
@api_view -вьюшка на функциях

rest_framework.views.APIVIEW
rest_framework.viewsets - класс для обработки всех операций CRUD'''

class ArticleViewSEt(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TagViewSet(ModelViewSet):
    queryset= Tag.objects.all()
    serializer_class = TagSerializer
