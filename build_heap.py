# python3


def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n//2, -1, -1):
        j = i
        while True:
            k = j
            if 2*k+1 <= n-1 and data[k]>data[2*k+1]:
                j = 2*k+1
            if 2*k+2 <= n-1 and data[j]>data[2*k+2]:
                j = 2*k+2
            if k != j:
                swaps.append((k, j))
                data[k], data[j] = data[j], data[k]
            else:
                break

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    mode = input()
    if mode[0] =="I":

    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif mode[0] == "F":
        file_name = input()
        file_name = 'tests/' + file_name
        with open(file_name, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        return
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
