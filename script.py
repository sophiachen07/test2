import os

# --- 全域設定 ---
PROJECT_NAME = "mysite"
APP_NAME_LS = ["polls", "polls2"]
SUPERUSER_NAME = "test"
SUPERUSER_EMAIL = "test@example.com"
SUPERUSER_PASSWORD = "qwer123456"
# -----------------------------

def add_app_to_settings(app_name, project_name):
    """
    自動將一個 app 添加到 settings.py 的 INSTALLED_APPS 列表中。
    """
    print(f"--- 執行：自動將 '{app_name}' 加入 INSTALLED_APPS ---")

    # 1. 找到 settings.py 的路徑
    # (假設我們在專案根目錄下，所以路徑是 "project_name/settings.py")
    settings_path = os.path.join(project_name, "settings.py")

    # 檢查檔案是否存在
    if not os.path.exists(settings_path):
        print(f"!!! 錯誤：找不到 {settings_path} !!!")
        return

    # 2. 讀取檔案內容
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"!!! 讀取 {settings_path} 失敗：{e} !!!")
        return

    # 3. 準備要替換的內容
    target_string = "INSTALLED_APPS = ["
    # \n 是換行符，前面加 4 個空白是為了排版
    replacement_string = f'INSTALLED_APPS = [\n    "{app_name}",'

    # 4. 檢查是否已經加過了 (避免重複執行)
    if f'"{app_name}"' in content or f"'{app_name}'" in content:
        print(f"--- '{app_name}' 已經在 INSTALLED_APPS 中，無需修改 ---")
        return

    # 5. 執行替換
    if target_string not in content:
        print(f"!!! 錯誤：在 {settings_path} 中找不到 'INSTALLED_APPS = [' !!!")
        return

    new_content = content.replace(target_string, replacement_string, 1)

    # 6. 將修改後的內容寫回檔案
    try:
        with open(settings_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"--- 成功將 '{app_name}' 加入 {settings_path} ---")
    except Exception as e:
        print(f"!!! 寫回 {settings_path} 失敗：{e} !!!")

os.system(f"django-admin startproject {PROJECT_NAME}")
os.chdir(PROJECT_NAME)  # 用 os.chdir() 取代 cd
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

# 為了讓 'createsuperuser --noinput' 能運作，我們必須在執行前設定環境變數
os.environ["DJANGO_SUPERUSER_PASSWORD"] = SUPERUSER_PASSWORD 
superuser_command = f"python manage.py createsuperuser --noinput --username {SUPERUSER_NAME} --email {SUPERUSER_EMAIL}"
os.system(superuser_command)
del os.environ["DJANGO_SUPERUSER_PASSWORD"]  # 執行後刪除，保持環境乾淨

for APP_NAME in APP_NAME_LS:
    os.system(f"python manage.py startapp {APP_NAME}")
    add_app_to_settings(APP_NAME, PROJECT_NAME)
    os.makedirs(f"{APP_NAME}/templates/{APP_NAME}", exist_ok=True)


