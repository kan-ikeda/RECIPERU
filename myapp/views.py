from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from .models import Recipe, Category, Contact
from .form import RecipeForm, SearchForm, ContactForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#レシピ一覧
class RecipeList(ListView):
    model = Recipe
    template_name = 'myapp/recipe_list.html'
    context_object_name = 'recipes'

#レシピ作成
class RecipeCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixinを追加
    model = Recipe
    form_class = RecipeForm
    template_name = 'myapp/recipe_form.html'
    success_url = reverse_lazy('myapp:recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # ログインユーザーを作者として設定
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)

#レシピ詳細
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'myapp/recipe_detail.html'
    context_object_name = 'recipe'

#レシピ編集
class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'myapp/recipe_form.html'
    success_url = reverse_lazy('myapp:recipe_list')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = RecipeForm(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

#レシピ削除
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'myapp/recipe_confirm_delete.html'

#レシピ削除確認画面
class RecipeConfirmDelete(FormView):
    template_name = 'myapp/recipe_confirm_delete.html'
    form_class = RecipeForm

    def form_valid(self, form):
        context = {}
        recipe_title = form.clean_data['title']
        recipe_items = form.clean_data['items']
        recipe_steps = form.clean_data['steps']
        recipe_cook_time = form.cleaned_data['cook_time']
        recipe_created_date = form.cleaned_data['created_date']
        recipe_category = form.cleaned_data['category']
        recipe_tags = form.cleaned_data['tags']

        context['title'] = recipe_title
        context['items'] = recipe_items
        context['steps'] = recipe_steps
        context['cook_time'] = recipe_cook_time
        context['created_date'] = recipe_created_date
        context['category'] = recipe_category
        context['tags'] = recipe_tags

        context['form'] = form
        return render(self.request, 'myapp/recipe_confirm_delete.html', context)

    def form_invalid(self, form):
        return render(self.request, 'myapp/recipe_input.html')







#カテゴリー一覧
class CategoryListView(ListView):
    model = Category
    template_name = 'myapp/category_list.html'
    context_object_name = 'categories'

#カテゴリー別レシピ一覧
class CategoryRecipesView(ListView):
    model = Recipe
    template_name = 'myapp/category_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(category_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context



#お問い合わせフォーム処理
class ContactFormView(FormView):
    template_name = 'myapp/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('myapp:recipe_list')
    def form_valid(self, form):
        contact = Contact(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message']
        )
        contact.save()
        return super().form_valid(form)

#レシピ検索フォーム
class RecipeSearchFormView(FormView):
    template_name = 'myapp/search_form.html'
    form_class = SearchForm
    
    def get(self, request, *args, **kwargs):
        # GETリクエストも処理する。これがないと、最初のページ表示でエラーになる可能性がある
        form = self.form_class(request.GET)  # GETパラメータをフォームに渡す
        query = request.GET.get('query')
        recipes = []
        if query:
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(items__icontains=query) |
                Q(steps__icontains=query)
            )
        return render(request, self.template_name, {'form': form, 'recipes': recipes, 'query': query})

    def form_valid(self, form):
        query = form.cleaned_data['query']
        recipes = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(items__icontains=query) | 
            Q(steps__icontains=query)  
        )
        return render(self.request, self.template_name, {'form': form, 'recipes': recipes, 'query': query})