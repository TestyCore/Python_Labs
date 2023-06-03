from django.shortcuts import render
from .models import Product, ProductCategory, Manufacturer


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    context = {
        'num_products': num_products,
        'num_manufacturers': num_manufacturers,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

