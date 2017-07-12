from django.shortcuts import render
from blog.models import Book

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