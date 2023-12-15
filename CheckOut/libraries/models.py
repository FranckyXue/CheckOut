from django.db import models

# Create your models here.

from django.db import models

class Library(models.Model):
    ID = models.AutoField(primary_key=True)
    BRANCH = models.CharField(max_length=255)
    ADDRESS = models.CharField(max_length=500)  # 调整了长度
    CITY = models.CharField(max_length=255)
    POSTCODE = models.CharField(max_length=10)
    PHONE = models.CharField(max_length=20)     # 调整了长度
    MONDAY = models.CharField(max_length=100, null=True, blank=True)       # 调整了长度
    TUESDAY = models.CharField(max_length=100, null=True, blank=True)      # 调整了长度
    WEDNESDAY = models.CharField(max_length=100, null=True, blank=True)    # 调整了长度
    THURSDAY = models.CharField(max_length=100, null=True, blank=True)     # 调整了长度
    FRIDAY = models.CharField(max_length=100, null=True, blank=True)       # 调整了长度
    SATURDAY = models.CharField(max_length=100, null=True, blank=True)     # 调整了长度
    SUNDAY = models.CharField(max_length=100, null=True, blank=True)       # 调整了长度
    LATITUDE = models.DecimalField(max_digits=10, decimal_places=6)        # 使用了DecimalField
    LONGITUDE = models.DecimalField(max_digits=10, decimal_places=6)       # 使用了DecimalField
    LINK = models.URLField(max_length=1000, null=True, blank=True)         # 调整了长度
    NYU = models.CharField(max_length=255)


    def __str__(self):
        return self.BRANCH
