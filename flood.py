import sys
import heapq

def main():
    #Read input file
    if len(sys.argv) < 2:
        print("Usage: python flood.py <inputfile>")
        return
    filename = sys.argv[1]
    with open(filename, "r") as f:
        data = f.read().split()

    it = iter(data)
    n = int(next(it))
    threshold = int(next(it))
    drain = int(next(it))

    events = [(int(next(it)), int(next(it))) for _ in range(n)]

    i = 0
    current_time = 0
    flood = 0
    max_flood = 0

    heap = []       
    sum_bases = 0    
    heap_size = 0

    def add_events(t):
        nonlocal i, sum_bases, heap_size
        while i < n and events[i][0] == t:
            appear_t, size = events[i]
            base = size - appear_t
            heapq.heappush(heap, -base)
            sum_bases += base
            heap_size += 1
            i += 1

    if i < n and events[0][0] > 0:
        current_time = events[0][0]

    while i < n or heap_size > 0:
        if heap_size == 0 and i < n and events[i][0] > current_time:
            gap = events[i][0] - current_time
            flood = max(0, flood - drain * gap)
            current_time = events[i][0]
            continue

        add_events(current_time)

        if heap_size > 0:
            base = -heapq.heappop(heap)
            sum_bases -= base
            heap_size -= 1

        inflow = sum_bases + current_time * heap_size
        flood += inflow
        flood = max(0, flood - drain)

        if flood >= threshold:
            print("FLOOD")
            print(current_time)
            print(flood)
            return

        max_flood = max(max_flood, flood)
        current_time += 1

        if i >= n and heap_size == 0:
            break

    print("SAFE")
    print(max_flood)

if __name__ == "__main__":
    main()




