#!/usr/bin/python3

def read_file(file):
    info = {}
    with open(f"./material/Junior2/container{file}.txt") as f:
        for l in f.readlines():
            if l.strip() == "":
                continue
            [larger, smaller] = l.strip().split()
            try:
                info[smaller].append(larger)
            except KeyError:
                info[smaller] = [larger]
    return info

def run_to_end(info, key, trace):
    results = set()
    for c in info[key]:
        if c in info:
            _trace = trace + [c]
            results.update(run_to_end(info, c, _trace))
            continue
        #print("adding final res: " + c + ", " + str(trace))
        results.add(c)
    return results

def run(n):
    info = read_file(n)
    print(info)

    results = set()
    for c in info:
        results.update(run_to_end(info, c, [c]))

    print("Results: ", results)

for i in [0, 1, 2, 3, 4]:
    run(i)
