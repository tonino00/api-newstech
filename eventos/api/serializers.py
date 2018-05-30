from rest_framework.serializers import ModelSerializer
from eventos.models import Evento


class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nome', 'descricao', 'horario_inicial', 'horario_final', 'valor', 'foto')
