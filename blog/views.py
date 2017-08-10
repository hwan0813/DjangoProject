from django.shortcuts import redirect,render,get_object_or_404
from .models import Book
from .forms import PostForm
from .models import Post

# Create your views here.

# myapp/views_cbv.py
class DetailView(object):
    '이전 FBV를 CBV버전으로 컨셉만 간단히 구현. 같은 동작을 수행'
    def __init__(self, model):
        self.model = model
    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs['id'])
    def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
    def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
    self.model._meta.model_name: self.get_object(*args, **kwargs),
    })
    @classmethod
    def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view

post_detail = DetailView.as_view(Post) # post_detail은 함수이다. gen~ 함수가 리턴해준 view_fn을 가지고 있는

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

def post_edit(request, id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
           post = form.save(commit=False)
           post.ip = request.META['REMOTE_ADDR']
           post.save()
           return redirect('/blog/')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', { 
        'form' : form,
        })

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
           #post = Post.objects.create(**form.cleaned_data)
           #return redirect('/blog/')
           # 이장석이 전호하는건 create를 forms.py안으로 옮기는것.
           post = form.save(commit=False) # 밑에 post.save()에서 저장일어나니까 커밋 false로해서 저장안되게??
           post.ip = request.META['REMOTE_ADDR']
           post.save()
           return redirect('/blog/')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', { 
        'form' : form,
        })

    

