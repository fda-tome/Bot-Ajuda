import tweepy
import time

def guarda_id(banco,ultimo_id,controle):
    banco_escrita= open(banco,'r')
    intermed=banco_escrita.readlines()
    banco_escrita.close()
    banco_escrita=open(banco,'w')
    i=0
    for aux in intermed:
        if (i!=controle):

            banco_escrita.write(aux.strip()+'\n')
        if(i==controle):
            banco_escrita.write(str(ultimo_id).strip()+'\n')
        i+=1
    return

def retorna_id(banco,controle):
    banco_leitura=open(banco,'r')
    intermed=banco_leitura.readlines()
    banco_leitura.close()
    print(int(controle))
    return int(intermed[int(controle)].strip())

auth=tweepy.OAuthHandler('xpDreY4GClKh8YU9hmXy0syj4','WgBGz9vBKRhOzuDYQvK734RNn1XGX6wD6PQNIk1cKepreSqecc')
auth.set_access_token('1287810577914646530-CCiiQqzCsAS968mL84SYIwq10BGA9Y','A0ljEvdrJ8X1U44Fl3V6hNbit8PSjBfoZPPsnlwNQeR04')
api=tweepy.API(auth)
frases=open("frases.txt")

while(1):
    controle=0
    frases.seek(0)
    querys=frases.readlines()
    for query in querys:
        milestone=retorna_id("id.txt",controle)
        busca=api.search(q=query,lang='pt',since_id=milestone)
        for tweet in reversed(busca):
            print(str(tweet.id) + ' -- ' +'@'+tweet.user.screen_name+' : '+str(tweet.text))
            api.update_status('@'+tweet.user.screen_name +' '+'VO LHE ESBAGAÇA ,TODO DURO', tweet.id);
        if(busca):
            guarda_id("id.txt",tweet.id,controle)
        controle+=1
    time.sleep(60)


