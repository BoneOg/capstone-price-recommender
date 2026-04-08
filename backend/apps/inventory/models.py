from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    unit_of_measurement = models.CharField(max_length=50, help_text="e.g., kg, grams, pieces, liters")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IngredientPriceHistory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit of measurement (in pesos)")
    date_bought = models.DateField(auto_now_add=True, help_text="Date the ingredient price was manually logged from the market")
    source = models.CharField(max_length=100, default='Manual Input', help_text="e.g. Manual Input or OCR Receipt")
    
    class Meta:
        ordering = ['-date_bought']

    def __str__(self):
        return f"{self.ingredient.name} - ₱{self.price} on {self.date_bought}"
