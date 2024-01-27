api_list = [
    "pars",
    "rslogo",
    "myrc",
    "unsound_unsafe",
    "rust2c",
    "send_sync",
    "webserver",
    "channels",
    "train_game",
    "hooked",
    "currying",
    "repetition",
    "average_macro",
    "fun_types",
    "languages",
    "dungeons_and_dragons",
    "pointy",
    "modularity",
    "vector_operations",
    "doctor_who",
    "christmas_tree",
    "type_lifetimes",
    "annotate_lifetimes",
    "pusheen",
    "my_first_borrow",
    "data_analysis",
    "collections",
    "to_upper",
    "tribonacci",
    "io",
    "picasso",
    "dall_e_rs",
    "carnival",
    "multiverse",
    "mini_grep",
]

import os
import requests


def download_file(url, dest_directory, dest_filename):
    response = requests.get(url, stream=True)
    os.makedirs(dest_directory, exist_ok=True)  # 创建目录，如果目录不存在
    dest_path = os.path.join(dest_directory, dest_filename)
    with open(dest_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)


# 替换下面的 URL 和文件名
for activity_name in api_list:
    url = f"https://cgi.cse.unsw.edu.au/~cs6991/current/api/activity/{activity_name}/autotest.tar"
    destination_directory = f"activity/{activity_name}"  # 将活动名称添加到目录路径
    destination_filename = "autotest.tar"
    download_file(url, destination_directory, destination_filename)
