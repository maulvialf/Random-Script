import r2pipe
r2 = r2pipe.open('./out')
r2.cmd('aaa')
function_info = r2.cmdj(f'afij sym.validate')
function_size = function_info[0]['size']
function_offset = function_info[0]['offset'] r2.quit()
