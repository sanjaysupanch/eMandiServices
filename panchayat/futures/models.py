from django.db import models

# Create your models here.
class FuturesContract(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    Crop=models.CharField(max_length=50)
    CropVariety=models.CharField(max_length=50)
    Quantity=models.PositiveIntegerField(default=None)
    DeliveryDate=models.DateField(auto_now=False)
    AdvanceDate=models.DateField(null=True)
    ProductionMode=models.CharField(max_length=50)
    ContractPrice=models.FloatField(default=None)
    advance=models.FloatField(default=None)

    def __str__(self):
       return f'{self.Quantity}{self.user.username} FutureContract'

class MarketOrder(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    CropName=models.CharField(max_length=50)
    CropVariety=models.CharField(max_length=50)
    Quantity=models.PositiveIntegerField(default=None)
    OrderDate=models.DateTimeField(auto_now_add=True)
    ClosingDate=models.DateField(auto_now=False)
    ProductionMode=models.CharField(max_length=50)
    BasePrice=models.FloatField(default=None)
   

    def __str__(self):
        return f'{self.user.username}{self.CropName}MarketOrder'       