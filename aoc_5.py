
with open("aoc_5.txt") as fp:
    lines = [l.rstrip() for l in fp]

seeds = lines[0][7:].split()
print("seeds", seeds)

def find_closest_source(source, map, lines):
    active = False
    closest = None
    dist = None
    ret_nums = None
    for line in lines[2:]:
        if map == "s2s" and line == "seed-to-soil map:":
            active = True
            continue
        elif map == "s2f" and line == "soil-to-fertilizer map:":
            active = True
            continue
        elif map == "f2w" and line == "fertilizer-to-water map:":
            active = True
            continue
        elif map == "w2l" and line == "water-to-light map:":
            active = True
            continue
        elif map == "l2t" and line == "light-to-temperature map:":
            active = True
            continue
        elif map == "t2h" and line == "temperature-to-humidity map:":
            active = True
            continue
        elif map == "h2l" and line == "humidity-to-location map:":
            active = True
            continue
        elif active and not line:
            break
        elif active:
            nums = line.split()
            current_dist = source - int(nums[1])
            # print("source", source, "current_dist", current_dist, f"range {int(nums[1])} {int(nums[1]) + int(nums[2])-1}", "nums ->", nums)
            if current_dist >= 0 and (source >= int(nums[1]) and source < int(nums[1]) + int(nums[2])):
                if not dist or current_dist < dist:
                    dist = current_dist
                    closest = int(nums[1])
                    ret_nums = nums

    # print("source", source, "closest", closest)

    if closest is None:
        return source
    else:
        diff = source - int(closest)
        # print("source", source, "closest", closest, "diff", diff)
        if diff <= int(ret_nums[2]):
            mapped_dest = int(ret_nums[0]) + diff
            return mapped_dest
        else:
            return source

locations = []
flow = ["s2s", "s2f", "f2w", "w2l", "l2t", "t2h", "h2l"]
for seed in seeds:
    source = int(seed)

    for map in flow:
        dest = find_closest_source(source, map, lines)
        # print(map, source, dest)
        source = dest
    
    # print(dest)
    locations.append(dest)

locations.sort()
print("Lowest seed location:", locations[0])
