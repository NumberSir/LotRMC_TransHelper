import json
import re
from pathlib import Path
from typing import Optional
from zipfile import ZipFile

FLAG = {
    "legacy": "assets/lotr/lang/en_US.lang",
    "renewed": "assets/lotr/lang/en_us.json"
}

LANGUAGE = [
    "be_by", "cs_cz", "de_de", "enws", "en_gb",
    "en_nz", "en_pt", "en_ud", "en_us", "es_es",
    "fr_ca", "fr_fr", "hu_hu", "it_it", "ja_jp",
    "ko_kr", "pl_pl", "pt_br", "ro_ro", "ru_ru",
    "sk_sk", "sv_se", "tr_tr", "uk_ua", "vec_it",
    "zh_cn",
]


def get_jar_file(jar_files: list) -> Optional[list]:
    """获取 jar 文件的名称、版本新旧、语言 json 文件内容"""
    jar_list = []
    for file in jar_files:
        if file.endswith(".jar"):
            data = get_lang_data(file)
            if data:
                version = re.findall(r"\d+\.?\d*", file)[-1]
                if jar_list:
                    if dist_higher_version(version, jar_list[0]["version"]):
                        version, jar_list[0]['version'] = 'new', 'old'
                    else:
                        version, jar_list[0]['version'] = 'old', 'new'
                jar_list.append({"name": file, "version": version, "data": data})
    return jar_list


def get_lang_data(file: str) -> Optional[str]:
    """获取语言 json 文件内容"""
    with ZipFile(file, 'r') as zf:
        zf_data = zf.NameToInfo
        renewed_flag = is_renewed(zf_data)

        if not isinstance(renewed_flag, bool):
            return None

        if renewed_flag:
            renewed_lang = zf_data[FLAG["renewed"]]
            with zf.open(renewed_lang, 'r') as f:
                json_data = json.load(f)
                return json_data

        else:
            return None


def is_renewed(zf_data: dict) -> Optional[bool]:
    """
    判断 jar 文件是复兴版/传承版

    :param zf_data: jar 文件内容
    :return: 复兴版 True, 传承版 False, 错误 None
    """
    if FLAG["legacy"] in zf_data.keys():
        return False
    elif FLAG["renewed"] in zf_data.keys():
        return True
    return None


def dist_higher_version(ver1: str, ver2: str) -> bool:
    """判断两个版本号的大小"""
    ver1_list = ver1.split(".")
    ver2_list = ver2.split(".")
    for idx, val in enumerate(ver1_list):
        if int(val) > int(ver2_list[idx]):
            return True
        elif int(val) < int(ver2_list[idx]):
            return False
    return False


def dump_json(data: dict, file: Path) -> None:
    """
    将对比结果写入文件

    :param data: 对比结果
    :param file: 文件路径
    :return: None
    """
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
