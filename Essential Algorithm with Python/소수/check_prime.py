def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1

    if i == n:
        print("{}는 소수\n".format(n))
    else:
        print("{}는 합성수\n".format(n))


if __name__ == '__main__':
    check_prime(19)
    check_prime(130)
    check_prime(37)
    check_prime(20)
    check_prime(21)
