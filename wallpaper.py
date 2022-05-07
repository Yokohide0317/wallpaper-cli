#import subprocess
import os
import argparse
import shutil
import pathlib
import glob

# ~/.wallpaper
save_dir = pathlib.Path(os.environ['HOME'], ".wallpaper")

# 画像を~/.wallpaper下へ
def add_wallpaper(args):

    # 変更前と変更先のPathを確認して、取得
    def _set_path(_froml, _tol):
        if _tol != None:
            assert len(_froml) == len(_tol), "--nameの数が違います"
            
            new_froml = []
            new_tol = []
            for f, t in zip(_froml, _tol):
                assert pathlib.Path(f).exists(), f"{f}は存在しません。"
                new_froml.append(pathlib.Path(f))
                new_tol.append(save_dir / t)
        else:
            new_froml = []
            new_tol = []
            for f in _froml:
                assert pathlib.Path(f).exists(), f"{f}は存在しません。"
                new_froml.append(pathlib.Path(f))
                new_tol.append(save_dir)
        return new_froml, new_tol
    
    # ~/.wallpaperが無ければ作成
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
    
    # 呼び出し
    from_paths, to_paths = _set_path(args.img_path, args.name)
    for f, t in zip(from_paths, to_paths):
        shutil.move(f, t)
        print(f"{f} -> {t.name}")
    return

def change_wallpaper(args):
    img_path = save_dir / pathlib.Path(args.img_name)
    assert img_path.exists(), f"存在しません: {str(img_path)}"
    cmd_img_path = '\"' + str(img_path) + '\"'
    cmd = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file {cmd_img_path}'"

    print(cmd)
    os.system(cmd)
    return

def list_wallpaper(args):
    files = [str(x.name) for x in save_dir.iterdir() if x.is_file()]
    print(files)
    return

def command_help(args):
    print(parser.parse_args([args.command, '--help']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers()

    # addコマンド
    parser_add = subparsers.add_parser('add', help='see `add -h`')
    parser_add.add_argument("img_path", nargs="*")
    parser_add.add_argument("-n", "--name", nargs="*")
    parser_add.set_defaults(handler=add_wallpaper)

    # toコマンド
    parser_to = subparsers.add_parser('to', help='see `to -h`')
    parser_to.add_argument("img_name")
    parser_to.set_defaults(handler=change_wallpaper)

    # listコマンド
    parser_list = subparsers.add_parser('list', help='see `to -h`')
    parser_list.set_defaults(handler=list_wallpaper)

    # help
    parser_help = subparsers.add_parser('help', help='see `help -h`')
    parser_help.add_argument('command', help='command name which help is shown')
    parser_help.set_defaults(handler=command_help)

    # コマンドライン引数をパースして対応するハンドラ関数を実行
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        # 未知のサブコマンドの場合はヘルプを表示
        parser.print_help()
