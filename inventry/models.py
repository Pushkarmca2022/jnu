from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY =  (
    ('Analgesics', 'Analgesics'),
    ('Antacids', 'Antacids'),
    ('Antianxiety','Antianxiety'),
    ('Antiarrythmics','Antiarrythmics'),
    ('Antibacterials','Antibacterials'),
    ('Antibiotics','Antibiotics'),
    ('Antcoagulants and Thrombolytics','Antcoagulants and Thrombolytics'),
    ('Anticonvulsants','Anticonvulsants'),
    ('Antidepressants','Antidepressants'),
    ('Antidiarrheals','Antidiarrheals'),
    ('Antiemetics','Antiemetics'),
    ('Antifungals','Antifungals'),
    ('Antihistamins','Antihistamins'),
    ('Antihypertensives','Antihypertensives'),
    ('Anti-inflammatories','Anti-inflammatories'),
    ('Antineoplastics','Antineoplastics'),
    ('Antipsychotics','Antipsychotics'),
    ('Antipyretics','Antipyretics'),
    ('Antivirals','Antivirals'),
    ('Barbiturates','Barbiturates'),
    ('Beta-Blockers','Beta-Blockers'),
    ('Broncodilators','Broncodilators'),
    ('Cold Cures','Cold Cures'),
    ('Corticosteroids','Corticosteroids'),
    ('Cough Suppressants','Cough Suppressants'),
    ('Cytotoxics','Cytotoxics'),
    ('Decongestants','Decongestants'),
    ('Diuretics','Diuretics'),
    ('Expectorant','Expectorant'),
    ('Hormones','Hormones'),
    ('Hypoglycemics(Oral)','Hypoglycemics(Oral)'),
    ('Immunosuppresives','Immunosuppresives'),
    ('Laxatives','Laxatives'),
    ('Muscle Relaxants','Muscle Relaxants'),
    ('Sedatives','Sedatives'),
    ('Sex Hormones(Female)','Sex Hormones(Female)'),
    ('Sex Hormones(Male)','Sex Hormones(Male)'),
    ('Sleeping Drugs','Sleeping Drugs'),
    ('Tranquilizers','Tranquilizers'),
    ('Vitamins','Vitamins'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'
    
    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)        
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'    
