def split_string(str, char):
    words = []
    s = ""
    for i in str:
        if i == char:
            words.append(s)
            s = ""
            continue
            
        s += i
        
    words.append(s) 
    return words

def join_string(words, char):
        
    str = ""
    for i in range(len(words)-1):
        str += words[i]
        str += char
        
    str += words[len(words)-1]
    return str

str = "Hello Bhai"
print(split_string(str,' '))

words = ["Hello" , "Bhai"]
print(join_string(words , ' '))



      
