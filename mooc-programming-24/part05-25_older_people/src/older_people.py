# Write your solution here
def older_people(people: list, year: int):
    older = []
    for i in people:
        if i[1] < year and i[0] not in older:
            older.append(i[0])
    return older


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)