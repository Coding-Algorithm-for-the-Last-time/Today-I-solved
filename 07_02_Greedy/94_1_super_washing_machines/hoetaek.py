def sol(machines):
    s = sum(machines)
    l = len(machines)

    if s % l != 0:
        return -1

    moves = 0
    target = s // l
    max_moves = max(machines) - target
    for m in machines:
        moves += m - target
        max_moves = max(max_moves, abs(moves))
    return max_moves


print(sol([0, 0, 4, 0, 5, 0, 5, 0, 4]))
