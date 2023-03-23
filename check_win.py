def check_win(arr, sign):
    zeroes = 0
    for row in arr:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if arr[0][col] == sign and arr[1][col] == sign and arr[2][col] == sign:
            return sign
    if arr[0][0] == sign and arr[1][1] == sign and arr[2][2] == sign:
        return sign
    if arr[0][2] == sign and arr[1][1] == sign and arr[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Draw'
    return False