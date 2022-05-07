#import subprocess
import os
import argparse



def main(_fs_args):

    if _fs_args.command == "add":
        parser = argparse.ArgumentParser()
        parser.add_argument("img_path", nargs="*")
        parser.add_argument("-n", "--name", nargs="*")


    elif _fs_args.command == "to":
        parser = argparse.ArgumentParser()
        parser.add_argument("img_name")
        args = parser.parse_args()
        change_wallpaper(args.img_name)
    return

def change_wallpaper(_img_path):
    cmd_img_path = '\"' + str(_img_path) + '\"'
    cmd = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file {cmd_img_path}'"

    print(cmd)
    os.system(cmd)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers()

    # addコマンド
    parser_add = subparsers.add_parser('add', help='see `add -h`')
    parser.add_argument("img_path", nargs="*")
    parser.add_argument("-n", "--name", nargs="*")
    parser_add.set_defaults(handler=add_wallpaper)

    # toコマンド
    parser_to = subparsers.add_parser('to', help='see `to -h`')
    parser.add_argument("img_name")
    parser_add.set_defaults(handler=change_wallpaper)

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
