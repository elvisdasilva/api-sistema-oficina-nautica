from django.db import models
from apps.customer.models import Customer
from apps.brand.models import Brand
from apps.model.models import Model


class Vessel(models.Model):
    REGISTRATION_TYPE_CHOICES = [
        ("BAR_ALU", "Barco de Alumínio"),
        ("ESC", "Escuna"),
        ("JET_BOAT", "Jet Boat"),
        ("LAN", "Lancha"),
        ("MOT_AQU", "Moto Aquática"),
        ("VEL", "Veleiro"),
        ("IAT", "Iate"),
        ("CAN", "Canoa"),
        ("CAI", "Caiaque"),
        ("BAL", "Balsa"),
        ("BAR_PES", "Barco de Pesca"),
        ("CAT", "Catamarã"),
        ("SUB", "Submarino"),
        ("CARG", "Navio de Carga"),
        ("PAS", "Navio de Passageiros"),
        ("TAN", "Navio Tanque"),
        ("DRA", "Draga"),
        ("REB", "Rebocador"),
        ("FRA", "Fragata"),
        ("POR_AVI", "Porta-aviões"),
    ]

    registration = models.CharField(max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="vessels"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="vessels")
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name="vessels")
    hours_sailed = models.PositiveIntegerField()
    year_of_manufacture = models.IntegerField()
    fuel = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    photos = models.ImageField(upload_to="vessel_photos/", blank=True, null=True)
    registration_type = models.CharField(
        choices=REGISTRATION_TYPE_CHOICES, max_length=8
    )
    general_observations = models.TextField(blank=True)

    def __str__(self):
        return self.registration
