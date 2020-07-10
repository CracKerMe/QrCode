from MyQR.myqr import run


def main(
    words: str,
    picture: str,
    save_dir: str,
    level='H',
    version=20,
    colorized=True
):
    '''
    + words: 要表示的文字,不支持中文
    + picture: 背景图片
    + save_dir: 生成的二维码存储位置
    + level: 纠错等级, 默认为"H": 超强纠错
    + colorized: 是否使用彩色, 默认使用
    + version: 二维码边长
    '''

    run(
        words=words,
        version=version,
        level=level,
        picture=picture,
        colorized=colorized,
        save_dir=save_dir
    )


if __name__ == "__main__":
    pass