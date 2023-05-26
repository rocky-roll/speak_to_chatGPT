import os
from cryptography.fernet import Fernet

def key_paswoord():
    created_key_ = Fernet.generate_key()
    print(f"{created_key_.decode('utf-8')}")
     
    file_key = open("key_paswoord.txt", "w", encoding='utf-8')
    file_key.write(f"{created_key_.decode('utf-8')}")
    file_key.close

def key_cript(api_key__):
    count =0
    while True:
        if count >= 3:
            pass
            break
        if os.path.exists('key_paswoord.txt') == False:
            key_paswoord()
            count +=1
            continue

        
        try:
            file_key = open('key_paswoord.txt', "r", encoding='utf-8')
            a12= file_key.read()
            created_key = Fernet(a12)
            cript = created_key.encrypt(str.encode(api_key__))
            file_key.close
            return cript
            #break
        except:
            key_paswoord()
            count +=1
            continue

        # created_key_ = Fernet.generate_key()
        # print(f"{created_key_.decode('utf-8')}")
        # created_key = Fernet(created_key_)
        ##created_key = Fernet('YIzLIHGUkYdb118zIYua6A2j7cdZ1ya9nAi--W7c59Y=')

        ##cript = created_key.encrypt(str.encode(api_key__))
        # print(api_key__)
        # print(f"{created_key.decode('utf-8')}")
        # print(f"{cript.decode('utf-8')}")
    


def key_decript():
    try:
        #created_key = Fernet('YIzLIHGUkYdb118zIYua6A2j7cdZ1ya9nAi--W7c59Y=')
        f1= open("key_paswoord.txt", "r", encoding='utf-8')
        created_key_ = f1.read()
        f1.close

        created_key = Fernet(created_key_ )
        f2 = open("api_key.txt", "r", encoding='utf-8')
        mk = f2.read()
        api_key_decrpt_ = created_key.decrypt(mk)
        f1.close
        print(api_key_decrpt_)
        return api_key_decrpt_
    except:
        pass

#print(key_cript("hola mundo"))
#print(key_decript().decode('utf-8'))
