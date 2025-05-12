from django import forms
from .models import Recipe,Contact

#レシピ作成、編集用フォーム
class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'recipe_form'
        
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'items', 'steps', 'cook_time', 'created_date', 'category', 'tags')



#問い合わせ用フォーム
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')



#レシピ検索用フォーム
class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'レシピ名や材料で検索'})
    )

