# -*- coding: utf-8 -*-
def InPkg(mirrors="https://pypi.tuna.tsinghua.edu.cn/simple", upgrade_pip=False):
    from os import system
    '''
    安装myqr及其依赖包.
    + mirrors: pip镜像源
    + upgrade_pip: 是否升级pip
    '''
    if upgrade_pip == True: system(f'pip install -i {mirrors} pip -U')
    system(f'pip install myqr -i {mirrors}')
    return


if __name__ == "__main__":
    # 直接使用
    InPkg()