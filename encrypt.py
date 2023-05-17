from cryptography.fernet import Fernet


def key_cript(api_key__):

    # created_key_ = Fernet.generate_key()
    # print(f"{created_key_.decode('utf-8')}")
    # created_key = Fernet(created_key_)
    created_key = Fernet('YIzLIHGUkYdb118zIYua6A2j7cdZ1ya9nAi--W7c59Y=')

    cript = created_key.encrypt(str.encode(api_key__))
    # print(api_key__)
    # print(f"{created_key.decode('utf-8')}")
    # print(f"{cript.decode('utf-8')}")
    return cript


def key_decript():
    created_key = Fernet('YIzLIHGUkYdb118zIYua6A2j7cdZ1ya9nAi--W7c59Y=')

    f2 = open("api_key.txt", "r", encoding='utf-8')
    mk = f2.read()
    api_key_decrpt_ = created_key.decrypt(mk)
    f2.close
    return api_key_decrpt_


# print(key_decript().decode('utf-8'))