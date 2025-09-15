def fat(fatorial):
    if fatorial == 1:
        return 1
    else:
        return fatorial * fat(fatorial - 1)
        
print(fat(5))