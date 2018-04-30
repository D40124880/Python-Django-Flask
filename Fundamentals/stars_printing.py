def multiply(arr):
    for x in range(0, len(arr)):
        if isinstance(arr[x], int):
            print arr[x] * '*'
        elif isinstance(arr[x], str):
            print len(arr[x]) * arr[x].lower()[0]

multiply([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])