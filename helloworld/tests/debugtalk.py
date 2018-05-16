import hashlib
import hmac
import random
import string

SECRET_KEY = "DebugTalk"
default_request = {
    "base_url": "http://gate.test.51juban.cn",
    "headers": {
        "Content-Type": "application/x-www-form-urlencoded",
        "user_agent": "Owner/1.0.1.9.2 (iPhone; iOS 11.2.2; Scale/2.00)",
    }
}

def getBaseUrl():
    test_env = os.environ.get("test_env","TEST")
    if test_env == "TEST"
        return "http://gate.test.51juban.cn"
    else
        return "http://gate.juban.com"
def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign