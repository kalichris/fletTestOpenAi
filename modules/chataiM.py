import uuid
from fake_useragent import UserAgent
import requests
import json
class ChatAi():
    def __init__(self):       
        self.url = "https://chat-shared3.zhile.io/api/loads"
        self.User_Agent = UserAgent(os="windows").random

    def sendAi(self,msg):
        self.msg=msg
        headers = {
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Referer': 'https://chat-shared3.zhile.io/shared.html?v=2',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': self.User_Agent,
            'sec-ch-ua-platform': '"Windows"'
        }
        response = requests.request("GET", self.url, headers=headers)
        print(response.status_code)
        if response.ok:
            
            loads = response.json()["loads"]
            url = "https://chat-shared3.zhile.io/auth/login"
            password = "Am12345678"
            token_key = loads[0]["token_id"]
            payload = f'token_key={token_key}&session_password={password}'
            headers = {
                'authority': 'chat-shared3.zhile.io',
                'accept': '*/*',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://chat-shared3.zhile.io',
                'referer': 'https://chat-shared3.zhile.io/shared.html?v=2',
                'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': self.User_Agent
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.status_code)
            if response.ok:
                #print("credential", response.cookies.get("credential"))
                credential = response.cookies.get("credential")
                url = "https://chat-shared3.zhile.io/api/conversation"
                parent_id = str(uuid.uuid4())
                messages_id = str(uuid.uuid4())
                message = self.msg
                payload = json.dumps({
                    "action": "next",
                    "messages": [
                        {
                            "id": messages_id,
                            "author": {
                                "role": "user"
                            },
                            "content": {
                                "content_type": "text",
                                "parts": [
                                    message
                                ]
                            },
                            "metadata": {}
                        }
                    ],

                    "parent_message_id": parent_id,
                    "model": "text-davinci-002-render-sha",
                    "plugin_ids": [],
                    "timezone_offset_min": -120,
                    "suggestions": [
                    ],
                    "history_and_training_disabled": False,
                    "arkose_token": "", #"385179324d049dfa2.6360493101|r=us-east-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|guitextcolor=%23000000|pk=0A1D34FC-659D-4E23-B17B-694DCFCF6A6C|at=40|sup=1|rid=53|ag=101|cdn_url=https%3A%2F%2Fclient-api.arkosetoken.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-us-east-1.arkoselabs.com|surl=https%3A%2F%2Fclient-api.arkosetoken.com|smurl=https%3A%2F%2Fclient-api.arkosetoken.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager",
                    "force_paragen": False,
                    "stream": False,
                })
                headers = {
                    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                    'DNT': '1',
                    'Accept-Language': 'en-US',
                    'sec-ch-ua-mobile': '?0',
                    'User-Agent': self.User_Agent,
                    'Content-Type': 'application/json',
                    'accept': 'text/event-stream',
                    'Referer': 'https://chat-shared3.zhile.io/?v=2',
                    'X-Authorization': f'Bearer {credential}',
                    'sec-ch-ua-platform': '"Windows"',
                    'Cookie': f'credential={credential}'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.status_code)
                if response.ok:
                    lines = response.content.split(b"\n")
                    # error = None
                    message = ""
                    for line in lines:
                        # remove b' and ' at the beginning and end and ignore case
                        line = str(line)[2:-1]
                        if line.lower() == "internal server error":
                            print(f"Internal Server Error: {line}")
                            raise Exception(f"Internal Server Error: {line}")

                        if not line or line is None:
                            continue
                        if "data: " in line:
                            line = line[6:]
                        if line == "[DONE]":
                            break

                        # DO NOT REMOVE THIS
                        line = line.replace('\\"', '"')
                        line = line.replace("\\'", "'")
                        line = line.replace("\\\\", "\\")

                        try:
                            line = json.loads(line)
                        except json.decoder.JSONDecodeError:
                            continue

                        if not line.get("message"):
                            continue

                        if line.get("message").get("author").get("role") != "assistant":
                            continue

                        cid = line["conversation_id"]
                        pid = line["message"]["id"]
                        metadata = line["message"].get("metadata", {})
                        message_exists = False
                        author = {}
                        if line.get("message"):
                            author = metadata.get("author", {}) or line["message"].get("author", {})
                            if (
                                    line["message"].get("content")
                                    and line["message"]["content"].get("parts")
                                    and len(line["message"]["content"]["parts"]) > 0
                            ):
                                message_exists = True

                        message: str = (
                            line["message"]["content"]["parts"][0] if message_exists else ""
                        )
                        model = metadata.get("model_slug", None)
                        finish_details = metadata.get("finish_details", {"type": None})["type"]
                        
        return message
#ChatAi("ماهو الحيون صاحب ذاكرة قويه ")
