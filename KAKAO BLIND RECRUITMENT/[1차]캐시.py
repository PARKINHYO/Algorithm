from sys import stdin


def solution(cacheSize, cities):
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer

    hit = False
    cacheHit = 0
    cacheMiss = 0
    cache = []
    time = []

    for i in range(0, len(cities)):
        cities[i] = cities[i].lower()

    for i in range(0, len(cities)):

        for j in range(0, len(cache)):

            if cache[j] == cities[i]:
                cacheHit += 1
                time[j] = 1
                hit = True
            else:
                time[j] += 1

        if bool(hit) == False:
            cacheMiss += 1
            if len(cache) < cacheSize:
                cache.append(cities[i])
                time.append(1)
            else:
                index = 0
                for j in range(1, len(cache)):
                    if time[j] > time[j - 1]:
                        index = j
                cache[index] = cities[i]
                time[index] = 1
        hit = False

    answer = cacheHit * 1 + cacheMiss * 5
    return answer


if __name__ == '__main__':
    cacheSize = int((stdin.readline()))
    cities = stdin.readline().split()
    solution(cacheSize, cities)
