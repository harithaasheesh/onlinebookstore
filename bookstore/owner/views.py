from django.shortcuts import render,redirect
from owner import forms

# Create your views here.
def add_book(request):
    if request.method=="GET":
        form=forms.BookForm()
        context={}
        context["form"]=form
        return render(request,"add_book.html",context)
    if request.method=="POST":
        form=forms.BookForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data["book_name"]
            author=form.cleaned_data["author"]
            price=form.cleaned_data["price"]
            copies=form.cleaned_data["copies"]
            print(book_name,author,price,copies)
            return redirect("bookadd")
        else:
            return render(request,'add_book.html',{'form':form})
