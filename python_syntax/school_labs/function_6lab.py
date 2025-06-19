def wrap_in_tag(arg_tag,arg_content):
    return  "<"+arg_tag+">"+arg_content+"</"+arg_tag+">"
     

print(wrap_in_tag('p','hello'))
print(wrap_in_tag('p','world'))