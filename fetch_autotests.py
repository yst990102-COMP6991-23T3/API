api_list = [
    "assign02_pars",
    "assign01_rslogo",
    "lab09_myrc",
    "lab09_unsound_unsafe",
    "lab09_rust2c",
    "lab08_send_sync",
    "lab08_webserver",
    "lab08_channels",
    "lab08_train_game",
    "lab07_hooked",
    "lab07_currying",
    "lab07_repetition",
    "lab07_average_macro",
    "lab07_fun_types",
    "lab05_languages",
    "lab05_dungeons_and_dragons",
    "lab05_pointy",
    "lab04_modularity",
    "lab04_vector_operations",
    "lab04_doctor_who",
    "lab03_christmas_tree",
    "lab03_type_lifetimes",
    "lab03_annotate_lifetimes",
    "lab03_pusheen",
    "lab03_my_first_borrow",
    "lab02_data_analysis",
    "lab02_collections",
    "lab02_to_upper",
    "lab02_tribonacci",
    "lab01_io",
    "lab01_picasso",
    "lab01_dall_e_rs",
    "lab01_carnival",
    "lab01_multiverse",
    "lab01_mini_grep",
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
