#!/usr/local/bin/python3
import os
import argparse
import shutil
import pathlib

# ~/.wallpaper
save_dir = pathlib.Path(os.environ['HOME'], ".wallpaper")

def init():
    # ~/.wallpaperが無ければ作成
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

def list_wallpaper():
    files = list(pathlib.Path(save_dir).glob("*"))
    # 更新順でsort
    files.sort()
    wallpapers = [str(x.name) for x in files if x.is_file()]
    wallpapers = dict(zip(range(0, len(wallpapers)), wallpapers))

    # ex: {0: 'kuusou-ressha.jpg', 1: 'ch4nge.JPG', 2: 'kitty_nya.png'}
    return wallpapers

# 画像を~/.wallpaper下へ
def add_wallpaper(args):
    # 変更前と変更先のPathを確認して、取得
    def _set_path(_froml, _tol):
        # --nameが指定されている場合
        if _tol != None:
            assert len(_froml) == len(_tol), "--nameの数が違います"

            new_froml = []
            new_tol = []
            for f, t in zip(_froml, _tol):
                f_path = pathlib.Path(f)

                assert f_path.exists(), f"{f}は存在しません。"
                new_froml.append(f_path)
                # 拡張子が指定されていない場合や違う場合、変更前の拡張子をくっつける
                if f_path.suffix == pathlib.Path(t).suffix:
                    t_path = save_dir / pathlib.Path(t)
                else:
                    t_path = save_dir / pathlib.Path(t+f_path.suffix)
                new_tol.append(t_path)

        # --nameが指定されていない場合、名前も拡張子もそのまま
        else:
            new_froml = []
            new_tol = []
            for f in _froml:
                f_path = pathlib.Path(f)
                assert f_path.exists(), f"{f}は存在しません。"
                new_froml.append(f_path)
                new_tol.append(save_dir)
        return new_froml, new_tol

    # 呼び出し
    from_paths, to_paths = _set_path(args.img_path, args.name)
    for f, t in zip(from_paths, to_paths):
        shutil.move(f, t)
        print(f"{f} -> {t.name}")
    return

def change_wallpaper(args):
    change_to = args.change_to
    if change_to.isdigit():
        wallpapers = list_wallpaper()
        img_name = wallpapers[int(change_to)]
    else:
        img_name = str(change_to)
    img_path = save_dir / pathlib.Path(img_name)
    assert img_path.exists(), f"存在しません: {str(img_path)}"
    cmd_img_path = '\"' + str(img_path) + '\"'
    cmd = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file {cmd_img_path}'"

    os.system(cmd)
    return

def show_list(args):
    wallpapers = list_wallpaper()
    print ("{:<4} {:<15}".format('ID','Name'))
    print ("-------------------")
    for key, value in wallpapers.items():
        print("{:<4} {:<15}".format(key, value))
    return

def open_img(args):
    open_path = save_dir
    if args.name != None:
        open_path = open_path / pathlib.Path(args.name)

    cmd = f"open {str(open_path)}"
    os.system(cmd)
    return

def command_help(args):
    print([args.command, '--help'])

def main():
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers()

    # addコマンド
    parser_add = subparsers.add_parser('add', help='see `add -h`')
    parser_add.add_argument("img_path", nargs="*")
    parser_add.add_argument("-n", "--name", nargs="*")
    parser_add.set_defaults(handler=add_wallpaper)

    # toコマンド
    parser_to = subparsers.add_parser('to', help='see `to -h`')
    parser_to.add_argument("change_to")
    parser_to.set_defaults(handler=change_wallpaper)

    # listコマンド
    parser_list = subparsers.add_parser('list', help='see `list -h`')
    parser_list.set_defaults(handler=show_list)

    # showコマンド
    parser_show = subparsers.add_parser('show', help='see `show -h`')
    parser_show.add_argument("-n", "--name", default=None)
    parser_show.set_defaults(handler=open_img)

    # help
    parser_help = subparsers.add_parser('help', help='see `help -h`')
    parser_help.add_argument('command', help='command name which help is shown')
    parser_help.set_defaults(handler=command_help)


    init()
    # コマンドライン引数をパースして対応するハンドラ関数を実行
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        # 未知のサブコマンドの場合はヘルプを表示
        parser.print_help()

if __name__ == "__main__":
    main()
