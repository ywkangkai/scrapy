# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : 02-demo.py
# @VX : tl210329
import rsa
import base64

def rsa_encrypt(pu_key, t):
    # 公钥加密
    rsas = rsa.encrypt(t.encode("utf-8"), pu_key)
    return base64.b64encode(rsas)

def rsa_decrypt(pr_key, t):
    # 私钥解密
    rsas = rsa.decrypt(base64.b64decode(t), pr_key).decode("utf-8")
    return rsas

if __name__ == "__main__":
    public_key, private_key = rsa.newkeys(512)   # 生成公钥、私钥
    print('公钥：', public_key)
    print('私钥：', private_key)
    text = 'I love Python!'  # 加密对象
    encrypted_str = rsa_encrypt(public_key, text)
    print('加密字符串：', encrypted_str)
    decrypted_str = rsa_decrypt(private_key, encrypted_str)
    print('解密字符串：', decrypted_str)