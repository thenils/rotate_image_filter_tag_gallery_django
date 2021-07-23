from django.shortcuts import render, redirect
from .models import Image, Tag
from .forms import FormTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PIL import Image as IG
from django.conf import settings


# anticlock wise
def rotateLeft(request, ImageID):
    image = Image.objects.get(id=ImageID)

    igm = IG.open(f'{settings.BASE_DIR}' + image.image.url)
    rotate_image = igm.rotate(90)

    rotate_image.save(image.image.file.name, overwrite=True)

    return redirect(f'/image/{ImageID}')

# clockwise


def rotateRight(request, ImageID):
    image = Image.objects.get(id=ImageID)

    igm = IG.open(f'{settings.BASE_DIR}' + image.image.url)
    rotate_image = igm.rotate(-90)

    rotate_image.save(image.image.file.name, overwrite=True)

    return redirect(f'/image/{ImageID}')


def ImageListView(request):

    if request.method == 'POST':
        form = FormTag(request.POST)
        if form.is_valid():
            tags = form.cleaned_data.get('tag')
            if len(tags) >= 1:
                images = Image.objects.filter(itag__tag__in=tags)
            else:
                images = Image.objects.all()
        else:
            images = Image.objects.all()

    else:
        form = FormTag()
        images = Image.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(images, 8)

    try:
        imgs = paginator.page(page)
    except PageNotAnInteger:
        imgs = paginator.page(1)
    except EmptyPage:
        imgs = paginator.page(paginator.num_pages)

    ctx = {
        'images': imgs,
        'form': form,
    }
    return render(request, 'home.html', ctx)


def ImageView(request, ImageID):
    image = Image.objects.get(id=ImageID)
    ctx = {
        'image': image
    }
    return render(request, 'image.html', ctx)


def AddImage(request):

    if request.method == 'POST':
        form = FormTag(request.POST)
        print(form)
        images = request.FILES.getlist('images')
        if form.is_valid():
            tags = form.cleaned_data.get('tag')

            itag = Tag.objects.filter(tag__in=tags)
            for image in images:
                created = Image.objects.create(image=image)
                for tag in itag:
                    created.itag.add(tag)

                if created:
                    print('+1')

            return redirect('imagelistview')

    else:
        form = FormTag()

    ctx = {
        'form': form,
    }
    return render(request, 'add_image.html', ctx)
