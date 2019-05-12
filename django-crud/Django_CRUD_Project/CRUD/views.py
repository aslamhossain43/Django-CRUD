from django.shortcuts import render,redirect
from .models import BookList
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    book=BookList.objects.all()
    return render(request,'index.html',{'book':book})

def edit(request,id):
    book = BookList.objects.get(id=id)
    context = {
    'book': book
           }
    return render(request,'edit.html',context)

def delete(request,id):
    book=BookList.objects.get(id=id)
    book.delete()
    return redirect('/')

def update(request,id):
    book=BookList.objects.get(id=id)
    book.title=request.GET['title']
    book.price = request.GET['price']
    book.author=request.GET['author']
    book.save()
    return redirect('/')

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details=BookList(title=title,price=price,author=author)
    book_details.save()
    return redirect('/')

def add_book(request):
    return render(request,'add_book.html')

  #file upload

def upload(request):
    context = {}

    if request.method == 'POST':
        uploadFile = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploadFile.name, uploadFile)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)




