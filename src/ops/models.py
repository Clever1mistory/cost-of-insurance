from tortoise import fields
from tortoise.models import Model


class Tariff(Model):
    date = fields.DateField(auto_now_add=True)  # Автоматически устанавливает текущую дату при создании объекта
    cargo_type = fields.CharField(max_length=255)
    rate = fields.DecimalField(max_digits=6, decimal_places=2)


class Calculation(Model):
    declared_value = fields.DecimalField(max_digits=10, decimal_places=2)
    cargo_type = fields.CharField(max_length=255)
    date = fields.DateField(auto_now_add=True)  # Автоматически устанавливает текущую дату при создании объекта
    insurance_cost = fields.DecimalField(max_digits=10, decimal_places=2)
