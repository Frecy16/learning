pip install <package_name>  用来下载第三方的模块 pip uninstall <package_name>  用来删除第三方的模块 pip list 用来列出当前环境安装的模块名和版本号 pip freeze
用来列出当前环境安装的模块名和版本号

pip freeze > file_name 将安装的模块名和版本号重定向输出到指定的文件，requirements pip install -r file_name 读取文件里模块名和版本号并安装

临时修改，只修改这一个文件的下载路径 pip install  <package_name> -i <url>  从指定的地址下载安装包

永久修改：在当前用户目录下创建一个pip的文件夹，然后再在文件夹里创建pip.ini文件并输入以下内容：
[global]
index-url=https://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com

常见国内镜像： 阿里云：https://mirrors.aliyun.com/pypi/simple/
中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣：https://pypi.douban.com/simple/
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/

