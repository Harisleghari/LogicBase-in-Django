from multiprocessing import context
import re
from django.shortcuts import render, redirect

from .models import Listing
from .forms import ListingForm

# Create your views here.

#CRUD create , retrieve, update, delete, and also a list

# 1-list
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }

    return render(request, "index.html", context)

# 2-retrieve
def listing_retrive(request, pk):
    listing = Listing.objects.get(id= pk)
    context = {
        "listing": listing
    }
    return render(request, "retrieve.html", context)

# 3-create
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "create.html", context)

# 3-update
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "create.html", context)

# 4-delete
def listing_delete(request, pk):
    listing = Listing.objects.get(id = pk)
    listing.delete()
    return redirect("/")