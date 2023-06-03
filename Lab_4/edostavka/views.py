from django.shortcuts import render
from .models import Product, ProductCategory, Manufacturer
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()

    # Available products (status = 'a')
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


class ProductsListView(generic.ListView):
    model = Product
    paginate_by = 5


class ProductDetailView(generic.DetailView):
    model = Product



