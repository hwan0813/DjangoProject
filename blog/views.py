from django.shortcuts import redirect,render
from blog.models import Book
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html')

def InsertBook(request, isbn, title, memo):
    Book(isbn=isbn, title=title, memo={'content': memo}).save()
    return render(request, 'blog/mypage.html',
                  { 'welcome_text': 'Insert: ' + title })

def DisplayMyPage(request):
    return render(request, 'blog/mypage.html', { 'welcome_text': 'Hello World!제이슨' })

#db에 저장된걸 가져와서 보여주는 함수 
def DisplayBook(request, isbn):
    result = Book.objects.filter(isbn=isbn)[0]
    bookInfo = "ISBN: {0}; TITLE: {1}; MEMO: {2}".format(result.isbn,
                                                        result.title,
                                                        result.memo['content'])
    return render(request, 'blog/mypage.html',
                  { 'welcome_text': bookInfo })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
           # 방법1
            #post = Post()
            #post.title = form.cleaned_data['title']
            #post.content = form.cleaned_data['content']
            #post.save()
           #방법 2
           # post = Post(title=form.cleaned_data['title'],
           #                content = form.cleaned_data['content'])
           # 
           # 방법3
           # post = Post.objects.create(title=form.cleaned_data['title'],
           #                    content = form.cleaned_data['content']) 
           # 방법4
           post = Post.objects.create(**form.cleaned_data)
           return redirect('/blog/')
    
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', { 
        'form' : form,
        })