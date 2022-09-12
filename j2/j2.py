#!/usr/bin/env python3

def read_file(file: str) -> dict:
    info = {}
    with open(file) as f:
        for line in f.readlines():
            # skip blank lines
            if line.strip() == "":
                continue
            # parse the line
            [heavier, lighter] = line.strip().split()
            # try to add the heavier to the list, create new list if it doesn't exist
            try:
                info[lighter].append(heavier)
            except KeyError:
                info[lighter] = [heavier]
    return info

def run_to_heaviest(info: dict, key: str) -> set:
    results = set()
    # check each container, that is heavier than the given one
    for heavier_container in info[key]:
        # if we can run further and find even heavier containers, then recurse
        if heavier_container in info:
            results.update(run_to_heaviest(info, heavier_container))
            continue
        # add to results, if this is the heaviest we can get
        results.add(heavier_container)
    return results

def run(example_number: int = 0) -> None:
    # read in the data
    info = read_file(f"./material/Junior2/container{example_number}.txt")
    print(f"{example_number}: Given (light->heavy): {info}")

    # for each container, run the path to the heaviest
    results = set()
    for container in info:
        results.update(run_to_heaviest(info, container))

    # if all paths run to the same container, we have the solution
    if len(results) == 1:
        print(f" => The heaviest container is {results.pop()}")
        return
    
    # if not, we print out possible solutions
    print(f"=> Possibilities for heaviest container: {results}")

if __name__ == "__main__":
    # run on all examples
    for i in [0, 1, 2, 3, 4]:
        run(i)
