import tiktoken
processing = tiktoken.get_encoding("cl100k_base")
text = "Hello, I am Sarah.And i love agentic AI"




e_tokens = processing.encode(text)
print(e_tokens)
print("Number of tokens:", len(e_tokens))
d_tokens=processing.decode(e_tokens)
print(d_tokens)
print("numbers of tokens: ",len(d_tokens))

for i in e_tokens:
    print(i,processing.decode([i]))

t1="agentic AI"
t2="""def a,b:
    return a*b"""

print(len(processing.encode[t1]))
print(len(processing.encode[t2]))
