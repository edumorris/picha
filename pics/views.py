from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Images

# Create your views here.
def index(request):

    # Getting images
    imgs = Images.objects.all().order_by('-id')

    title = 'Home'
    

    return render (request, 'index.html', {"title": title, "imgs": imgs})

def search_category(request):
    if 'images' in request.GET and request.GET["images"]:
        category_term = request.GET.get('images')
        searched_images = Images.search_image(category_term)

        message = f"{category_term}"
        
        return render(request, "search.html", {"message": message, "images": searched_images})
    
    else:
        message = "Nothing to search"
        return render(request, 'search.html', {"message": message})

def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location_term = request.GET.get('location')
        searched_images = Images.filter_by_location(location_term)

        message = f"{location_term}"
        
        return render(request, "location_search.html", {"message": message, "images": searched_images})
    
    else:
        message = "Nothing to search"
        return render(request, 'location_search.html', {"message": message})

def image_view(request, img_id):
    view_image = Images.get_image_by_id(img_id)
    # view_image = Images.objects.get(id = img_id)
    if view_image:
        return render(request, "photo.html", {"view_image": view_image})
    else:
        return redirect(index)