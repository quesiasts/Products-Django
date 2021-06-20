from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.indexes import GinIndex

class ProductHistory(models.Model):
    product = models.ForeignKey(
        "Product", related_name="history", on_delete=models.deletion.CASCADE
    )
    created_at = models.CharField( max_length=14)
    data = JSONField(help_text="Product data history")

    class Meta:
        ordering = ["-created_at"]
        indexes = [GinIndex(fields=["data"]), models.Index(fields=["created_at"])]
        verbose_name = ("product history")

    def __str__(self):
        return f"{self.product.barcode} - {self.created_at}"

class Product(models.Model):
    historic_model = ProductHistory
    barcode = models.CharField(
        db_index=True, max_length=14, blank=True, default="", help_text="Global Trade Item Number (Barcode)"
    )
    brand = models.ForeignKey(
        "brands.Brand", on_delete=models.deletion.PROTECT, related_name="products", help_text="Product brand"
    )
    title = models.CharField(max_length=128, help_text="Product title")
    description = models.TextField(help_text="Product Description", default="")
    status = models.CharField(
        db_index=True,
        max_length=64,
        default="draft",
        help_text="Product status",
    )
    height = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, help_text="Height in centimeters"
    )
    width = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, help_text="Width in centimeters"
    )
    length = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, help_text="Length in centimeters"
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, help_text="Weight in grams"
    )
    region = models.CharField(max_length=2)
    active = models.BooleanField(db_index=True, default=True, help_text="Activation/deactivation flag")
    errors = JSONField(
        default=list, help_text="any errors", blank=True
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["region", "barcode"], name="region_barcode_unique"
            ),
            models.UniqueConstraint(
                fields=["region", "barcode", "brand"],
                name="region_barcode_brand_unique",
            ),
        ]
    def __str__(self):
        return self.barcode
