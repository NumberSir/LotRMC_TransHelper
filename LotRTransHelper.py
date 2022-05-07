"""
----------------------------------

实现功能：

1.筛选出新旧两版复兴版魔戒模组

2.对比两版语言文件差异

2.1.对比两版对话文件差异(实现中)

3.将 新加词条 / 删除词条 / 修改词条 写入文件

Goals:

1.Find newer and older version of LotR mod Renewed jar files

2.Compare the language files (en_us.json) between the two versions

2.1.Compare the speech files (en_us.json) between the two versions

3.Write the additions / deletions / editions of the files into a new file

----------------------------------
"""
from os import listdir, mkdir, system
from pathlib import Path
from typing import Union

from utils import dump_json, get_jar_file

PATH = Path().resolve()


def get_difference():
    jar_files = [_ for _ in listdir(PATH) if _.endswith('.jar')]
    if not jar_files:
        jar_files = ['None']
    if len(jar_files) != 2:
        return (
            f"--------------------------------------------------------\n"
            f"必须仅传入 2 个版本的复兴版魔戒模组 jar 文件哦！\n"
            f"目前的文件：{', '.join([_ for _ in jar_files])}\n"
            f"请检查目录：{PATH}\n\n"
            f"You must input 2 and only 2 versions of the jar file of LotR-renewed mod!\n"
            f"Currently file(s): {', '.join([_ for _ in jar_files])}\n"
            f"Please check the directory: {PATH}\n"
        )
    jar_list = get_jar_file(jar_files)

    if not jar_list:
        return (
            f"--------------------------------------------------------\n"
            f"没有找到复兴版魔戒模组的 jar 文件！\n"
            f"请检查目录：{PATH}\n\n"
            f"Did not find the jar file of LotR-renewed mod! \n"
            f"Please check the directory: {PATH}\n"
            f"--------------------------------------------------------\n"
        )
    jar_old: dict[str, Union[str, dict]] = [_ for _ in jar_list if _['version'] == 'old'][0]
    jar_new: dict[str, Union[str, dict]] = [_ for _ in jar_list if _['version'] == 'new'][0]

    additions = {}
    deletions = {}
    editions = {}
    for new_key, new_val in jar_new['data'].items():
        if new_key not in jar_old['data'].keys():
            additions[new_key] = new_val
        elif jar_old['data'][new_key] != new_val:
            editions[new_key] = new_val
    for old_key, old_val in jar_old['data'].items():
        if old_key not in jar_new['data'].keys():
            deletions[old_key] = old_val

    if "diff" not in listdir(PATH):
        mkdir(PATH / "diff")

    if additions:
        dump_json(additions, PATH / "diff" / "additions.json")
        print(
            f"--------------------------------------------------------\n"
            f"已将新增词条写入文件：{Path('diff/additions.json')}\n"
            f"The additions have been written into file: {Path('diff/additions.json')}\n"
        )
    else:
        print(
            f"-----------------\n"
            f"没有新增键值对！\n"
            f"No additions!\n"
        )

    if deletions:
        dump_json(deletions, PATH / "diff" / "deletions.json")
        print(
            f"--------------------------------------------------------\n"
            f"已将删除词条写入文件：{Path('diff/deletions.json')}\n"
            f"The deletions have been written into file: {Path('diff/deletions.json')}\n"
        )
    else:
        print(
            f"-----------------\n"
            f"没有删除键值对！\n"
            f"No deletions!\n"
        )

    if editions:
        dump_json(editions, PATH / "diff" / "editions.json")
        print(
            f"--------------------------------------------------------\n"
            f"已将修改词条写入文件：{Path('diff/editions.json')}\n"
            f"The editions have been written into file: {Path('diff/editions.json')}\n"
        )
    else:
        print(
            f"-----------------\n"
            f"没有修改键值对！\n"
            f"No editions!\n"
        )


def main():
    print(
        f"-----------------\n"
        f"正在运行中...\n"
        f"Running...\n"
    )
    return get_difference()


if __name__ == "__main__":
    result = main()
    print(result) if result else None

    system("pause")
