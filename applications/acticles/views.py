from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Tag, Comment
from .serializers import ArticleSerializer
from .serializers import ArticleSerializer, ArticleListSerializer, TagSerializer, CommentSerializer
from .permissions import IsAuthor


'''
@api_view -вьюшка на функциях

rest_framework.views.APIVIEW
rest_framework.viewsets - класс для обработки всех операций CRUD'''

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    filterset_field = ['tag', 'status']
    search_fields = ['title', ['tag__title']]
    # permission_classes = [IsAuthenticated]


    def get_serializer_context(self):
            context = super().get_serializer_context()
            context.update({'request': self.request})
            return context
    
    def get_permissions(self) -> list:
         if self.request.method == 'POST':
              self.permission_classes = [IsAuthenticated]
         elif self.action in ['PUT', 'PATCH', 'DELETE']:
              self.permission_classes = [IsAuthor]
         return super().get_permissions()
    
    def get_serializer_class(self):
         if self.action == 'list':
              return ArticleListSerializer
         elif self.action == 'comment':
              return CommentSerializer
         return super().get_serializer_class()
    
    @action(methods=['POST', 'DELETE'], detail=True)
    def comment(self, request, pk=None) -> None:
          article = self.get_object()
     #   Article.objects.get(pk=pk)
          if request.method =='POST':
               serializer = CommentSerializer(data=request.data)
               context={'request': request}
               serializer.is_valid(raise_exception=True)
               serializer.save(user=request.user, article=article)
               return Response(serializer.data, ) 
          return Response({'TODO': 'ДОБАВИТЬ УДАЛЕНИЕ КОММЕНТА'})
    
class CommentViewSet(ModelViewSet):
     queryset = Comment.objects.all()
     serializer_class = CommentSerializer

     def get_permissions(self):
          if self.action == ['create']:
               self.permission_classes = [IsAuthenticated]
          elif self.action in ['update', 'destroy']:
               self.permission_classes = [IsAuthor]
          return super().get_permissions()
     
     def get_serializer_context(self):
          context = super().get_serializer_context()
          context.update({'request': self.request})
          return context


"""
action - действия пользователя
get - получение всех оъектов
retreive - получение одного объекта
create
update
delete

"""

class TagViewSet(ModelViewSet):
    queryset= Tag.objects.all()
    serializer_class = TagSerializer

#TODO: наполнить сайт контентом