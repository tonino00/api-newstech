from rest_framework.viewsets import ModelViewSet
from core.models import Noticia
from .serializers import NoticiaSerializer


class NoticiaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
