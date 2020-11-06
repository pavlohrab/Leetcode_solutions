def reverse(x):
        x_str = str(x)
        if x < 0:
            x_str = x_str[1:]
            rev = int("-"+x_str[::-1])
        else:
            rev = int(x_str[::-1])
        if (rev <= -2**31) or (rev >= 2**31 - 1):
            return 0
        else:
            return rev