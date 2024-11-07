from django.shortcuts import render, redirect
from .models import Photo, Category


# Create your views here.
def photo_gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)


    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def photo_detail(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photos/detail.html', {'photo': photos})

def photo_upload(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        print('data:', data)
        print('image:', image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image,
        )

        return redirect('photo_gallery')
        
    context = {'categories': categories}
    return render(request, 'photos/upload.html', context)