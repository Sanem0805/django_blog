from rest_framework.routers import DefaultRouter
from .views import ArticleViewSEt, TagViewSet

router = DefaultRouter()
router.register('article', ArticleViewSEt, 'articles')
router.register('tags', TagViewSet, 'tags')

urlpatterns = router.urls

