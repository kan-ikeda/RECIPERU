from django.db import models

# Create your models here.

#カテゴリーモデル
class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=100)

    def __str__(self):
        return self.name



#タグモデル
class Tag(models.Model):
    name = models.CharField('タグ', max_length=100)

    def __str__(self):
        return self.name
    


#レシピモデル
class Recipe(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('画像', upload_to='recipes/', blank=True, null=True)
    items = models.TextField('材料', blank=True, null=True)
    steps = models.TextField('作り方', blank=True, null=True)
    cook_time = models.IntegerField('調理時間', blank=True, null=True)
    created_date = models.DateTimeField('作成日', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='所属カテゴリー')
    tags = models.ManyToManyField(Tag, related_name='所属タグ')

    def __str__(self):
        return self.title



#お問い合わせモデル
class Contact(models.Model):
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', blank=True, null=True)
    message = models.TextField('内容', blank=True, null=True)

