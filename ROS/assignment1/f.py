import math

def converter(val):
    w = val[3]
    x = val[0]
    y = val[1]
    z = val[2]
    return_val = 'euler('
    #roll
    sinr_cosp = 2*(w*x + y*z)
    cosr_cosp = 1 - 2*(x*x + y*y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    return_val += (str(roll) + ',')
    #pitch
    sinp = 2*(w*y - z*x)
    if sinp >= 1 or sinp <= -1 :
        pitch = 90
    else:
        pitch = math.asin(sinp)
    return_val += (str(pitch) + ',')
    #yaw
    siny_cosp = 2*(w*z + x*y)
    cosy_cosp = 1 - 2*(y*y + z*z)
    yaw = math.atan2(siny_cosp,cosy_cosp)
    return_val += (str(yaw) + ')')
    return return_val

def data_collector(message):
    message_info = message
    data = [] 
    dustbin = ['q', 'u', 'a', 't', 'e', 'r', 'i', 'o', 'n', 's', '(', 'x',  'y',  'z',  'w', ')']
    for i in message_info:
        t = True
        for j in dustbin:
            if i == j:
                t = False       
        if t :
            data.append(i)
    temp_val = str()
    return_val = []
    for i in data:
        if i == ',':
            return_val.append(float(temp_val))
            temp_val = str()
        else:
            temp_val += i
    return_val.append(float(temp_val))
    return converter(return_val)

