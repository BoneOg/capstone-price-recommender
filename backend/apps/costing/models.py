from django.db import models
from apps.menu.models import MenuItem

class MenuCostSnapshot(models.Model):
    """
    Saves a historical snapshot of how much it cost to make a MenuItem on a specific date,
    and what the actual profit margin was based on ingredient market prices that day.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='cost_snapshots')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Calculated cost of all ingredients based on today's market price")
    actual_profit_margin_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Calculated actual profit margin % based on selling price vs total cost")
    date_calculated = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_calculated']

    def __str__(self):
        return f"{self.menu_item.name} Cost: ₱{self.total_cost} margin: {self.actual_profit_margin_percentage}% on {self.date_calculated}"
