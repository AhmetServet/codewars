def make_readable(seconds):
    
    l = lambda t: ("0" + str(t)) if t < 10 else str(t) 
    
    s = l(seconds % 60)
    m = l(seconds // 60 % 60)
    h = l(seconds // 3600)
    
    return h + ":" + m +":" + s