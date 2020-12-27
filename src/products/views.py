from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd

# Create your views here.

def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    # print(product_df)
    # print(purchase_df)
    product_df['product_id'] = product_df['id']
    df = pd.merge(purchase_df, product_df, on='product_id')
    context = {
        'products' : product_df.to_html(),
        'purchase' : purchase_df.to_html(),
        'df' : df.to_html(),
    }
    return render(request, 'products/main.html', context)