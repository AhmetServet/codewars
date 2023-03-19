def wave(people):
    wave = []

    for i in range(0, len(people)):
        if people[i] != " ":
            wave.append(people[:i] + people[i].upper() + people[i+1:])
    
    return wave
