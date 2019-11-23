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