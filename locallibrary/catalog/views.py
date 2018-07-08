from django.shortcuts import render
from django.views.generic import ( ListView ,DeleteView ,TemplateView ,CreateView ,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime

from .models import *
from .forms import *

# Create your views here.
def home (request):
    num_book =BookModel.objects.all().count()
    num_author=AuthorModel.objects.all().count()
    num_instance =BookInstanceModel.objects.all().count()
    num_avilable_instance =BookInstanceModel.objects.filter(status__exact='a').count()
    num_language=LanguageModel.objects.all().count()
    num_gener =GenerModel.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request,'catalog/home.html',{"num_book":num_book,"num_author":num_author,
                                                "num_instance":num_instance,"num_avilable_instance":num_avilable_instance,
                                                "num_language":num_language,"num_gener":num_gener ,'num_visits':num_visits})

class BookListView(ListView):
    model=BookModel
    template_name='catalog/book.html'
    context_object_name ='book_list'
    paginate_by = 10

    def get_queryset(self):
        return BookModel.objects.filter()


class BookDetailsView(DeleteView):
    model=BookModel
    template_name='catalog/book_details.html'
    context_object_name='book_details'

class AuthorListView(ListView):
    model =AuthorModel
    context_object_name ='author_list'
    template_name ='catalog/author.html'
    paginate_by =10

    def get_queryset(self):
        return AuthorModel.objects.filter()
class AuthorDetailsView(DeleteView):
    model=AuthorModel
    template_name='catalog/author_details.html'
    context_object_name='author_details'

class AboutTemplateView(TemplateView):
    template_name ='catalog/about.html'

class LoanedBooksByUserListView(LoginRequiredMixin,ListView):
    model = BookInstanceModel
    context_object_name='loanbook'
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstanceModel.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')



@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstanceModel, pk = pk)
    if request.method == 'POST':
        form = RenewBookModelForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['due_back']
            book_inst.save()
            return HttpResponseRedirect(reverse('my-borrowed') )
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

class AuthorCreate(CreateView):
    model =AuthorModel
    fields='__all__'

class AuthorUpdate(UpdateView):
    model=AuthorModel
    fields='__all__'


class AuthorDelete(DeleteView):
    model =AuthorModel
    success_url = reverse_lazy('author')

class BookCreate(CreateView):
    model =BookModel
    fields='__all__'

class BookUpdate(UpdateView):
    model=BookModel
    fields='__all__'


class BookDelete(DeleteView):
    model =BookModel
    success_url = reverse_lazy('book')
