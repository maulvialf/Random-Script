jsondata = open('astfile').read()
jsondata = jsondata.split("\n")
whitelist = ["index", "inc", "stmts","field_name","ast_type", '"op":', '"tok_kind":', '"val":	', '"name":	"', '"stmts":	[{', '"right":	[{', '"left":	[{', '"right":	{', '"left":	{', "left_type", "right_type", '"cond":	{', "next_token"]
for i in jsondata:
    for x in whitelist:
        if(x in i):
            try:
                x = i.split('token:')[0] + i.split('(')[1].split(")")[0]
                # print('$$$$$$$$$$$$$')
                # print(i)
                # print(x)
                i = x
                # print('$$$$$$$$$$$$$')
            except:
                i = i
            # print i.split('token:')[0] 
            i = i.replace('"', '')
            i = i.replace(',', '')
            i = i.replace(':\t', ' ')
            i = i.replace('\t', '  ')
#             i = i.replace('name varname', 'name SOMEMEMORABLEVARNAME')
            if("ast_type" in i and "stmt" in i.lower()):
                print("")
            print(i)
            break
