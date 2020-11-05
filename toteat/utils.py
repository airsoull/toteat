import os


def get_or_create_log_folder(BASE_DIR) -> str:
    folder_path = f'{BASE_DIR}/logs/'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return folder_path
