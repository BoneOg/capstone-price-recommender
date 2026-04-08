from django.db import models
from apps.menu.models import MenuItem

class PriceRecommendation(models.Model):
    STATUS_CHOICES = [
        ('Recommendation', 'Recommendation'),
        ('Warning', 'Warning'),
        ('Action Taken', 'Action Taken'),
    ]
    
    ACTION_CHOICES = [
        ('Increase Price', 'Increase Price'),
        ('Maintain Price (Monitor)', 'Maintain Price (Monitor)'),
        ('Decrease Price', 'Decrease Price'),
    ]

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recommendations')
    alert_type = models.CharField(max_length=50, choices=STATUS_CHOICES)
    suggested_action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    reasoning = models.TextField(help_text="Explanation: e.g., 'Ribeye Beef rose by 10% this week, dropping your profit margin to 8%.'")
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alert_type}: {self.menu_item.name} - {self.suggested_action}"
