
def read_file ():
    chat = []
    with open('C:/Users/Also_Lenovo/Desktop/coding/chat/lINE_viki.txt', 'r', encoding='utf-8-sig') as lines:
        for line in lines:  
            chat.append(line.strip())
    print(chat)
    return chat

def convert(chat):
    Allen_word = 0 
    Viki_word = 0
    Allen_post=0
    Viki_post=0
    Allen_picture=0
    Viki_picture=0
    for line in chat:
        s = line.split(' ')
        time=s[0]
        name=s[1]
        if name == 'Allen':

            if s[2] == '貼圖':
                Allen_post+=1

            elif s[2] == '圖片':
                Allen_picture+=1

            else:
                for m in s[2:]:
                    Allen_word+=len(m)  

        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_post+=1
            elif s[2] == '圖片':
                Viki_picture+=1
            else:
                for m in s[2:]:
                    Viki_word+=len(m)
    print(Viki_word)
    print(Allen_word)
    print(Viki_post)
    print(Allen_post)
    print(Viki_picture)
    print(Allen_picture)

chat = read_file()
convert(chat)
#write_file(chat)

