# Author : Zidane ZAOUI
# Github : https://github.com/Matsadura


import requests, json, os, stat, re
from getpass import getpass
from prompt_toolkit import prompt
from bs4 import BeautifulSoup


email = prompt('Enter your intranet email: ')
password = getpass('Enter your password: ')
# email = ""
# password = ""
session = requests.Session()
login_page_response = session.get('https://intranet.alxswe.com/auth/sign_in')
soup = BeautifulSoup(login_page_response.text, 'html.parser')
authenticity_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']

login_data = {
    'user[email]': email,
    'user[password]': password,
    'authenticity_token': authenticity_token
}

login_url = 'https://intranet.alxswe.com/auth/sign_in'

response = session.post(login_url, data=login_data)


next = "y"
while next == "y":
    link_js = list(input("Enter the number of Project: ").split())
    print(link_js)
    for link in link_js:
        data = session.get(f"https://intranet.alxswe.com/projects/{link}")
        PROJECT_PAGE = data.text
        PROJECT_NAME_found = re.findall(r'<title>Project: (.*?) \| ALX Africa Intranet</title>', PROJECT_PAGE)
        PROJECT_NAME = PROJECT_NAME_found[0].replace(" ", "_")
        print(PROJECT_NAME_found)
        # print(PROJECT_PAGE)
        # get task ID and correction ID
        C_ID = re.findall(r'data-correction-id="(.*?)"', PROJECT_PAGE)
        TASK_IDs = re.findall(r'<div class="task_progress_score_bar" data-task-id="(.*?)">', PROJECT_PAGE, re.MULTILINE | re.DOTALL)

        if not os.path.exists(PROJECT_NAME):
            os.makedirs(PROJECT_NAME)
        for T_ID in TASK_IDs:
            TASK_URL = f"https://intranet.alxswe.com/corrections/{C_ID[0]}/review.json?task_id={T_ID}"
            response = session.get(TASK_URL)
            TASK_CONTENT = json.loads(response.text)
            print(TASK_URL)
            # print(TASK_CONTENT)

            file_urls = []
            file_names = []
            for check in TASK_CONTENT['checks']:
                if 'files' in check:
                    files = check['files']
                    print(files)
                    if isinstance(files, list):
                        for file_info in files:
                            if 'url' in file_info:
                                url = file_info['url']
                                file_urls.append(url)
                            if 'name' in file_info:
                                name = file_info['name']
                                file_names.append(name)
            task_name = TASK_CONTENT["title"].replace(" ", "_")
            print(task_name)
            if not os.path.exists(f"{PROJECT_NAME}/{task_name}"):
                os.makedirs(f"{PROJECT_NAME}/{task_name}")

            for i, j in zip(file_urls, file_names):
                response = requests.get(i)
                file_path = os.path.join(task_name, j)
                file_path = os.path.join(PROJECT_NAME, file_path)
                with open(f"{file_path}", 'w') as file:
                    file.write(response.text)
                    if any(file_path.endswith(ext) for ext in (".py", ".sh", ".bash", ".rb")):
                        os.chmod(file_path, 0o777 | os.stat(file_path).st_mode)
            
                # print(i)
                # print(j)
                print(file_path)
            
            with open(f"{PROJECT_NAME}/{task_name}/review.txt", 'a', encoding="utf-8") as f:
                for checks in TASK_CONTENT['checks']:
                    TITLE_html = BeautifulSoup(checks['title'], 'html.parser')
                    TITLE = TITLE_html.get_text()
                    if 'files' in checks:
                        files = checks['files']
                        if isinstance(files, list):
                            for file_info in files:
                                if 'name' in file_info:
                                    name = file_info['name']
                        f.write(f"{checks['position']} - Title : {TITLE}\tType : {checks['check_label']}\n\tFile : {name}\n\n")
                    else:
                        f.write(f"{checks['position']} - Title : {TITLE}\tType : {checks['check_label']}\n\n")

    next = input("Extract more tests ? (y/n) : ")
