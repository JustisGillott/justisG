def product(numbers1):
    f = open(numbers1, "r")
    for line in f:
        answer = answer * int(line)
    f.close()
    return answer

answer = 1

