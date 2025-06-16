def wrap_in_tag(arg_tag,arg_content):
    result = "<"+arg_tag+">"+arg_content+"</"+arg_tag+">"
    return result

print(wrap_in_tag('p','hello'))
print(wrap_in_tag('p','world'))