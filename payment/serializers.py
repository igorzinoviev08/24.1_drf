from rest_framework import serializers

from payment.models import Payment
from payment.services import get_stripe_session


class PaymentSerializer(serializers.ModelSerializer):
    """
       Сериализатор модели платежа для использования в Django REST framework.

       Attributes:
           class Meta: Метаинформация о сериализаторе.
               model (Payment): Модель, которая используется для сериализации.
               fields (str): Поля, которые будут сериализованы (все поля).
    """
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'



    def get_url(self, obj: Payment):
        session = get_stripe_session(obj.session)
        return session.url