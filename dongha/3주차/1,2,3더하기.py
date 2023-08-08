import sys
def addNumberFront(tuples_list, num):
    new_list = []
    for i in tuples_list:
        new_list.append((num,)+i)
    return new_list

def main():
    n_array=["DUMMY"]
    n_array.append([(1,)]) # n1
    n_array.append([(1,1), (2,)]) # n2
    n_array.append([(1,1,1), (1,2), (2,1), (3,)]) # n3
    for i in range(4, 11):
        new_element_list = addNumberFront(n_array[i-1], 1) + addNumberFront(n_array[i-2], 2) + addNumberFront(n_array[i-3],3)
        n_array.append(new_element_list)
    n, k = map(int, sys.stdin.readline().split(' '))
    if k > len(n_array[n]):
        sys.stdout.write("-1")
    else:
        sys.stdout.write('+'.join(list(map(str, n_array[n][k-1]))))
    sys.stdout.write("\n")
main()
