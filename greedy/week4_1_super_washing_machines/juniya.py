

machines = [0,0,11,5]

def findMinMoves(machines):
    if sum(machines) % len(machines) != 0:
        return -1
    avg = sum(machines) // len(machines)
    move = 0
    diff = 0
    for i in range(len(machines)):
        diff += machines[i] - avg
        move = max(move, abs(diff), machines[i] - avg)
    return move

findMinMoves(machines)