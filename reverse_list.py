def reverseList(input):

    for i in input:
        if isinstance(i, list):
            reverseList(i)
            i=i.reverse()
        else:
            inputt.reverse()

inputt = [[1, 2], [3, 4], [5, 6, 7]]

reverseList(inputt)
print("reverse list: ", inputt)
