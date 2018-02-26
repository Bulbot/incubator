import math

from django.db.models.functions import Cast, Extract
from django.utils import timezone
from django.db.models import F, Sum
from django.db.models import DurationField, IntegerField
from django.db.models.functions import Now

from stock.models import Product

dt = F('producttransaction__when') - Now()
dt = Extract(dt, 'second')
individual_score = math.e ** dt
score = Sum(individual_score)

Product.objects.annotate(score=score)[0].score
