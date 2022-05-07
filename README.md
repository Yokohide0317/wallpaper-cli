# wallpaper-cli
PythonによるmacOS用の壁紙管理ツール

# How To

## 壁紙の追加

```
python wallpaper.py add path/to/wallpaper.png

## + 名前の変更
python wallpaper.py add path/to/wallpaper.png --name new_name

## + 複数追加
python wallpaper.py add path/to/wallpaper1.png path/to/wallpaper2.png --name new_name1 new_name2
```

## 壁紙の一覧

```
python wallpaper.py list
```

## 壁紙の変更

```
python wallpaper.py to wallpaper_name
or
python wallpaper.py to [ID]
```

## Develop

```
python setup.py develop
```
