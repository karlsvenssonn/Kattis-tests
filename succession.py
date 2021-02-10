import sys
from collections import defaultdict

def blood_level(person, fam_tree, founder):

    if person == founder:
        return 20.0

    level = 0.0
    for p in fam_tree[person]:
        level += blood_level(p, fam_tree, founder) / 2.0

    return level

def main():
    # Retreive data from input
    in_data = sys.stdin.readline().split()
    n = int(in_data[0])
    m = int(in_data[1])
    founder = sys.stdin.readline().rstrip()
    fam_tree = defaultdict(list)
    # Create families and family tree for each child
    for i in range(n):
        fam = sys.stdin.readline().split()
        child = fam[0]
        p1 = fam[1]
        p2 = fam[2]
        fam_tree[child] = [p1, p2]
    # List of claimants
    heirs = []
    for i in range(m):
        heirs.append(sys.stdin.readline().rstrip())
    # Election of new king
    new_king = None
    best_blood = -1
    # Check each childs blood status
    for child in heirs:
        heir_level = blood_level(child, fam_tree, founder)
        if heir_level > best_blood:
            new_king = child
            best_blood = heir_level
            
    print(new_king)
    
if __name__ == '__main__':
    main()



