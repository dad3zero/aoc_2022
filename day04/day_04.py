src_file = "input.txt"

def get_section_values(section:str):
    start, stop = section.split('-')
    return list(range(int(start), int(stop)+1))

def is_contained(section1:list, section2:list):
    s1 = set(section1)
    s2 = set(section2)
    return s1.issuperset(s2) or s2.issuperset(s1)

def is_ovelapping(section1, section2):
    s1 = set(section1)
    s2 = set(section2)

    return not s1.isdisjoint(s2)

if __name__ == "__main__":
    with open(src_file) as game_input:
        total_overlap = 0
        total_contained = 0
        for line in game_input:
            section1, section2 = line.strip().split(',')

            sec1_values = get_section_values(section1)
            sec2_values = get_section_values(section2)

            total_contained += is_contained(sec1_values, sec2_values)
            total_overlap += is_ovelapping(sec1_values, sec2_values)
            print()

    print(total_contained)
    print(total_overlap)

