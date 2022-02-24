from django.db import models
from datetime import datetime

class Contas(models.Model):
    titulo = models.CharField(max_length=80)
    data_vencimento = models.DateTimeField(null=True, blank=True, default=datetime.now())
    valor = models.FloatField()
    data_pagamento = models.DateTimeField(null=True, blank=True, default=None)
    recorrente = models.BooleanField(null=True, blank=True, default=False)
    paga = models.BooleanField(null=True, blank=True, default=False)

    @property
    def atrasada(self):
        return (datetime.now().date() > self.data_vencimento.date()) and self.data_pagamento is None
