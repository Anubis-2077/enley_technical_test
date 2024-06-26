from django.db import models

class User(models.Model):
    date_joined = models.DateTimeField(db_index=True)  # Se crea un indice en la base de datos en date_joined
    username = models.CharField(max_length=40)
    name = models.CharField(max_length=50, db_index=True)  # Lo mismo con name
    first_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"usuario : {self.id}"

class Contracts(models.Model):
    start_date = models.DateTimeField(db_index=True)  
    product_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Aca se definen los indices compuestos de la base de datos lo que va a derivar en que la base de datos 
        optimice consultas que involucren la combinacion de columnas especificas"""
        indexes = [
            models.Index(fields=['start_date', 'user']),
        ]

class RecurrentContracts(models.Model): 
    contract = models.OneToOneField(Contracts, on_delete=models.CASCADE)
