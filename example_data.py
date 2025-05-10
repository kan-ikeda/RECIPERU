# 初期データ投入用のスクリプト example_data.py
from myapp.models import Category, Tag

# カテゴリの作成
categories = ['主菜','副菜','スープ','デザート','パン','麺類','和食','洋食','中華']

for category_name in categories:
    Category.objects.create(name=category_name)

# タグの作成
tags = ['簡単','時短','健康的','子供向け','パーティー','季節','伝統料理','おもてなし']

for tag_name in tags:
    Tag.objects.create(name=tag_name)

print('初期データの投入が完了しました。')