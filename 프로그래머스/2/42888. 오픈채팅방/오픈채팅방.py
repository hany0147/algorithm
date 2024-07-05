def solution(record):
    result = []
    data = {}
    tmp = []
    
    for i in record:
        lst = i.split(" ")
        if len(lst) == 2:
            command, uid = lst[0], lst[1]
        else:
            command, uid, nickname = lst[0], lst[1], lst[2]
            data[uid] = nickname
            
        tmp.append((command, uid))
        
            
    for command, uid in tmp:
        if command == "Enter":
            result.append(f"{data[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{data[uid]}님이 나갔습니다.")
            
    
    return result