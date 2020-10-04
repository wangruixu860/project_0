import requests
url = "https://wenku.baidu.com/view/136311f80a4c2e3f5727a5e9856a561253d3211a.htmlw"
result = requests.get(url)
print(result.text)
"""
提交：git add.
git commit -m "备注"
git push origin 分支名
拉取代码：
第一次用：git clone 代码所在仓库地址
之后用：git pull
"""