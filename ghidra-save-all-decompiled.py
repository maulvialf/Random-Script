#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

# Import Ghidra Modules
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Create a new decompiler interface and initialize it
ifc = DecompInterface()
ifc.openProgram(currentProgram)

# Open the output file
with open('decompiled_code.txt', 'w') as f:
    # Iterate over each function in the program
    for function in currentProgram.getFunctionManager().getFunctions(True):
        # Decompile the function
        result = ifc.decompileFunction(function, 3600, ConsoleTaskMonitor())
        # Check for decompilation errors
        if result.decompileCompleted():
            # If no errors, get the decompiled code
            # highFunction = result.getHighFunction()
            # decomp = highFunction.getFunction().getPrototypeString(False, False) + '\n' + highFunction.getC()
            decomp = result.getDecompiledFunction().getC()		
            # Write the decompiled code to the file
            f.write(decomp + '\n')
        else:
            # Write an error message to the file
            f.write('Failed to decompile function at {}\n'.format(function.getEntryPoint()))
