from django.db import models
from apps.inventory.models import Ingredient

class MenuItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Current price on the restaurant menu (pesos)")
    target_profit_margin = models.DecimalField(max_digits=5, decimal_places=2, help_text="Target profit margin in % (e.g., 10.00)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity_required = models.DecimalField(max_digits=10, decimal_places=4, help_text="Quantity needed per 1 serving (based on ingredient's unit of measurement)")

    def __str__(self):
        return f"{self.quantity_required} {self.ingredient.unit_of_measurement} of {self.ingredient.name} for {self.menu_item.name}"
