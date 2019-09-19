"""
假设你在跳格子，你必须跳N格才能完成任务，但是你每次只能跳一格，两格或者三格，那么你有多少种方法完成？
"""

def dump(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dump(n-1) + dump(n-1) + dump(n-3)    

    pass
