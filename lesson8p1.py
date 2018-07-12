def fix_machine(string,target):
    adding_variable = 0
    while adding_variable <= len(target):
        #get first character of target
        find_charac = string.find(target[adding_variable])
        if find_charac == -1:
            return "Give me something that's not useless next time."
        elif adding_variable == len(target) -1:
            return target
        else:
             adding_variable = adding_variable + 1
