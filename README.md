# QrCode
## 必选参数
+ words: 要表示的文字,不支持中文
## 可选参数
+ picture: 背景图片路径,可选,默认为空,即生成普通二维码
+ save_dir: 生成的二维码存储位置, 默认为当前工作目录
+ save_name: 控制文件名, 格式可以是[jpg, png, bmp, gif].
> 使用背景图片默认: 背景图片文件名 + '_qrcode.png'
>> 不使用背景图片默认: qrcode.png
>>> 自定义
+ level: 纠错等级, 范围是L、M、Q、H，从左到右依次升高, 默认为"H": 超强纠错
+ colorized: 是否使用彩色, 默认使用
+ version: 二维码边长, 默认为20
## 注意
+ words 支持的文字有:
>``r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ··,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"``
+ picture 支持的图片格式有:
>`{'.jpg', '.png', '.bmp', '.gif'}`
+ picture 的**图片后缀不能是'.jpeg'**,虽然jpg是jpeg的别名,但在源码的条件判断语句里,不是jpg就会引发错误
+ picturn 图片路径最好使用绝对路径
+ save_name 与picture的图片名相同, 不能是jpeg
+ level 只能是L、M、Q、H
+ version 的值只能是1到40
+ 如果picture格式为gif那么save_name格式也需要是gif
+ gif 要比其他格式多用亿点点时间
# InPkg
+ mirrors: 可以选择pypi镜像源, 默认使用清华源
+ upgrade_pip 可以选择是否升级pip, 默认不升级
