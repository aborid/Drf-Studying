# pip install pyjwt
import datetime

import jwt

from muxi_shop_api2.settings import SECRET_KEY

SECRET_KEY

def create_token():
    headers ={
        'alg':"HS256",
        'typ':"jwt",
    }
    pyload ={
        'user_id':1,
        'username':"dazhou",
        'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1) ,#定义超时时间
    }
    result=jwt.encode(headers=headers,payload=pyload,key=SECRET_KEY,algorithm="HS256")
    return result
def get_payload(token):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        print("token认证失败了")
    except jwt.exceptions.ExpiredSignatureError:
        print("token过期了")
    except jwt.exceptions.InvalidTokenError:
        print("无效的，非法的token")
if __name__ == '__main__':
    # token=create_token()
    # print(token)
    token="""eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRhemhvdSIsImV4cCI6MTY5OTg2MzkwOX0.zUdQ3MV1IBZnP0WmHyC2WXPT8706vWVFKqRo9sM7BSU"""
    payload=get_payload(token)
    print(payload)