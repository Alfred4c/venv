import os

import requests
import unearth



# 创建虚拟环境
os.system('python3 -m venv venv')
print(1)
# 解析requirements.txt
with open('requirements.txt') as f:
    for line in f:
        os.chdir('D:\\venv')
        # 获取包名
        package_name = line.strip().split('==')[0]
        # 创建包名对应的文件夹
        os.makedirs(package_name, exist_ok=True)
        # 下载包
        version=line.split('==')[1]
        os.chdir(f'D:\\venv\\{package_name}')
        print(os.getcwd(), package_name)
        os.system('pip download {p}=={v}'.format(p=package_name,v=version))

        # 解析架构包链接
        for filename in os.listdir(os.getcwd()):

                wheel_info = filename.split('-')
                wheel_arch = wheel_info[-1]
                print(wheel_info,"------",wheel_arch)
                if 'amd64' in wheel_arch:
                    finder = unearth.PackageFinder(index_urls=['https://pypi.org/simple/'])
                    result=finder.find_matches('{}=={}'.format(wheel_info[0],wheel_info[1]))
                    for i in result:
                        url=i.link.url
                        judge=url.split("-")[-1]
                        if "amd64" not in judge and "linux" not in judge and "win32" not in judge:
                            file_name=url.split("/")[-1]
                            content = requests.get(url).content
                            with open(file_name, 'wb') as f:
                                f.write(content)

