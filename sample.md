# Django演習課題2：レシピ共有アプリケーション

## 課題概要

ユーザーがレシピを投稿・閲覧できるシンプルなレシピ共有アプリケーションを開発します。モデルのリレーション、テンプレートタグ、FormViewの活用を通じて、Djangoの基本的な機能を学びます。

## 必要な機能

1. レシピの作成・編集・削除・一覧表示・詳細表示
2. カテゴリによるレシピの分類
3. レシピ検索機能
4. お問い合わせフォーム

## 要件詳細

### モデル設計

以下のモデルとリレーションを実装します：

1. `Category`（カテゴリ）モデル
   - 名前（CharField）

2. `Recipe`（レシピ）モデル
   - タイトル（CharField）
   - 材料（TextField）
   - 作り方（TextField）
   - 調理時間（IntegerField）
   - 作成日（DateTimeField）
   - カテゴリ（ForeignKey → Category）
   - タグ（ManyToManyField → Tag）

3. `Tag`（タグ）モデル
   - 名前（CharField）

4. `Contact`（お問い合わせ）モデル
   - 名前（CharField）
   - メールアドレス（EmailField）
   - 内容（TextField）

### URL設計

- `/` - レシピ一覧（ホーム）
- `/recipes/add/` - レシピ作成
- `/recipes/<int:pk>/` - レシピ詳細
- `/recipes/<int:pk>/edit/` - レシピ編集
- `/recipes/<int:pk>/delete/` - レシピ削除
- `/categories/` - カテゴリ一覧
- `/categories/<int:pk>/` - カテゴリ別レシピ一覧
- `/contact/` - お問い合わせフォーム
- `/search/` - レシピ検索

### ビュー実装

1. 汎用ビュークラスの活用
   - ListView（レシピ一覧、カテゴリ一覧）
   - DetailView（レシピ詳細）
   - CreateView（レシピ作成）
   - UpdateView（レシピ編集）
   - DeleteView（レシピ削除）

2. FormView
   - お問い合わせフォーム処理
   - レシピ検索フォーム

### テンプレート

以下のテンプレートを作成し、テンプレートタグを活用します：
- `base.html` - サイト共通のベーステンプレート
- `recipe_list.html` - レシピ一覧
- `recipe_detail.html` - レシピ詳細
- `recipe_form.html` - レシピ作成・編集フォーム
- `recipe_confirm_delete.html` - レシピ削除確認
- `category_list.html` - カテゴリ一覧
- `category_recipes.html` - カテゴリ別レシピ一覧
- `contact_form.html` - お問い合わせフォーム
- `search_form.html` - 検索フォーム
- `search_results.html` - 検索結果

### フォーム

1. `RecipeForm` - レシピ作成・編集用
2. `ContactForm` - お問い合わせ用
3. `SearchForm` - レシピ検索用

### 提出物

- プロジェクトコード一式
  - GitHubリポジトリを作成して、コードをプッシュしてください。
- `README.md` ファイル
  - プロジェクトのルートディレクトリに作成してください。
  - 課題で行った内容や学んだことなどを記載してください。
  - 余裕があれば、以下の内容も記載してください。
    - モデル間のリレーションの説明とER図
    - URLルーティングの説明
    - 各ビューの機能と実装方法の説明
    - プロジェクトのセットアップ手順

## 発展課題（オプション）

1. レシピの評価機能（星評価）の追加
2. レシピ画像のアップロード機能
3. レシピのお気に入り登録機能
4. カテゴリのCRUD機能の実装
5. ページネーション機能の実装
