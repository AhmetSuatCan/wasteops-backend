from django.db import models
from .route import Route
from .container import Container


class RouteNode(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="nodes"
    )
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
        related_name="route_nodes"
    )
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('route', 'order')
        ordering = ['order']

    def __str__(self):
        return f"Node {self.order} on {self.route.name}"
