# wallpaper-cli
PythonによるmacOS用の壁紙管理ツール

# Installation

```
python setup.py develop
```

# How To

## 壁紙の追加

```
w-cli add path/to/wallpaper.png

## + 名前の変更
w-cli add path/to/wallpaper.png --name new_name

## + 複数追加
w-cli add path/to/wallpaper1.png path/to/wallpaper2.png --name new_name1 new_name2
```

## 壁紙の一覧

```
w-cli list
```

## 壁紙の変更

```
w-cli to wallpaper_name
or
w-cli to [ID]
```

# Uninstall

```
python -m pip uninstall w-cli
rm -r ~/.wallpaper
```


# execution error: Not authorized to send Apple events to Finder. (-1743)

System Preferences > Security & Privacy > Privacy Tab > Automation <br>

Check `iTerm`, `Kitty` ... etc.

