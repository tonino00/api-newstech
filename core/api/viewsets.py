from rest_framework.viewsets import ModelViewSet
from core.models import Noticia
from .serializers import NoticiaSerializer


class NoticiaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return Noticia.objects.filter(aprovado=True)