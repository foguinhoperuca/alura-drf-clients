from rest_framework.serializers import ModelSerializer, ValidationError
from clients.models import Client
from clients.validators import cpf_valid, rg_valid, name_valid, mobile_phone_valid


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not cpf_valid(data['cpf']):
            raise ValidationError({'cpf': 'The CPF must have, at least, 11 digts.'})

        if not rg_valid(data['rg']):
            raise ValidationError({'rg': 'The RG must have, at least, 9 digits.'})

        if not name_valid(data['name']):
            raise ValidationError({'name': 'The name must be alphanumeric.'})

        if not mobile_phone_valid(data['mobile_phone']):
            raise ValidationError({'mobile_phone': 'The mobile number must have, at least, 14 digits with mask: (99)9999-9999'})

        return data

