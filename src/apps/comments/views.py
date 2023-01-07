from django.shortcuts import redirect
from django.urls import reverse

from apps.catalog.models import Product
from .forms import CommentForm


def comment_processing(request):
    """Обрабатуем запрос на созданение коментария"""

    if request.method == 'POST':

        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            this_product = Product.objects.get(pk=request.POST['product'])
            new_comment.product = this_product
            new_comment.save()
            return redirect(reverse('catalog:product_detail', kwargs={'slug': this_product.slug}))
