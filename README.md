# 学習管理アプリ

学習管理デスクトップアプリ

## 特徴
- 課題登録
- 進捗管理
- 進捗確認グラフ表示、完了時期予測
- 単語帳機能
- 辞書機能

## 使用技術
- python3.5    

## ライブラリ
- numpy
- pandas
- matplotlib
- tkinter
- tksheet

## セットアップ

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. データベースの初期化
```bash
python db/init_db.py
```

### 3. アプリケーションの起動
```bash
python ui/app.py
```

## データベースについて
- `progress.db`は個人のデータが含まれるため、Git管理対象外です
- 初回セットアップ時は`db/init_db.py`を実行してデータベースを作成してください
- サンプルデータは`db/`ディレクトリのCSVファイルから読み込まれます
