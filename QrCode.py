from MyQR.myqr import run
from os import getcwd


def main(
    words: str,
    level = 'H',
    version = 20,
    save_dir = getcwd(),
    save_name = None,
    picture = None,
    colorized = True
):
    '''
    # 必选参数
    + words: 要表示的文字,不支持中文
    # 可选参数
    + picture: 背景图片路径,可选,默认为空,即生成普通二维码
    + save_dir: 生成的二维码存储位置, 默认为当前工作目录
    + save_name: 控制文件名, 格式可以是[jpg, png, bmp, gif].
    > 使用背景图片默认
    >> 背景图片文件名 + '_qrcode.png'
    > 不使用背景图片默认
    >> qrcode.png
    > 自定义
    + level: 纠错等级, 范围是L、M、Q、H，从左到右依次升高, 默认为"H": 超强纠错
    + colorized: 是否使用彩色, 默认使用
    + version: 二维码边长, 默认为20
    '''
    run(
        words=words,
        version=version,
        level=level,
        picture=picture,
        colorized=colorized,
        save_name=save_name,
        save_dir=save_dir
    )


if __name__ == "__main__":
    # 最简单使用, 在工作区下生成以张名为qrcode.png的普通二维码图片
    words = input('words:')
    main(words)