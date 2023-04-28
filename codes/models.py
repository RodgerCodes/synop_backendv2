from django.db import models


# Create your models here.

class Data(models.Model):
    station_id = models.ForeignKey('user_account.Station', on_delete=models.CASCADE, related_name="station_info")
    wind_speed = models.FloatField(null=True)
    wind_direction = models.PositiveIntegerField()
    max_temperature = models.FloatField(null=True)
    min_temperature = models.FloatField(null=True)
    dry_bulb = models.FloatField(null=True)
    wet_bulb = models.FloatField(null=True)
    dew_point = models.CharField(null=True, max_length=100)
    pressure_value = models.FloatField(null=True)
    isobaric_value = models.PositiveIntegerField(null=True)
    ground_max_temp = models.FloatField(null=True)
    low_clouds = models.CharField(max_length=350, )
    middle_clouds = models.CharField(max_length=350)
    high_clouds = models.CharField(max_length=350)
    sunshine = models.FloatField(null=True)
    evaporation = models.FloatField(null=True)
    relative_humidity = models.PositiveIntegerField(null=True)
    rainfall_amount = models.CharField(null=True, max_length=100)
    total_Cloud_amount = models.CharField(max_length=30, null=True)
    present_weather = models.CharField(null=True, max_length=10)
    past_weather = models.CharField(null=True, max_length=10)
    pastTwentyWeather = models.CharField(null=True, max_length=10)
    lowcloud_amount = models.CharField(null=True, max_length=10)
    middlecloud_amount = models.CharField(null=True, max_length=10)
    highcloud_amount = models.CharField(null=True, max_length=10)
    lowcloud_height = models.CharField(null=True, max_length=10)
    middlecloud_height = models.CharField(null=True, max_length=10)
    highcloud_height = models.CharField(null=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.station_id.station_name

    class Meta:
        ordering = ['-created_at']


class synop(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True, related_name="synop_data")
    code = models.CharField(max_length=1000, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-created']
