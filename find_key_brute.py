import string

f = open("output", "rb")
text = f.read()
f.close()

def keyLenght(text):
    for lenght in range(10, 16):
        d = {}
        for c in range(0, len(text), lenght):
            char = text[c]
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        d = sorted(d.values(), reverse = True)
        if 35 < sum(d[:4])/sum(d)*100 < 55:
            return lenght
     
key = ''    
key_lenght = keyLenght(text)
characters = valid_characters =  list(string.ascii_letters + string.digits)

for i in range(key_lenght):
    for char in characters:
        d = {}
        for c in range(i, len(text), key_lenght):
            x = chr(text[c]^ord(char))
            if x in d:
            	d[x] += 1
            else:
            	d[x] = 1
        try:
            s4 = d[' ']+d['a']+d['A']+d['e']+d['E']+d['i']+d['I']
            if 40 < s4/sum(d.values())*100 < 50:
                key += char
                break
        except:
            pass
print(key)
              	    	
