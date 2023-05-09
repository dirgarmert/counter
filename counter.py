import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('YOU ARE DONE IN', seconds, 'SECONDS')


t = input("Enter the time in seconds: ")
seconds: t
for seconds in t:
    if seconds <= "30":
        print("Do you really think that 0_0  ? ")
        break
    else:
        print("I bet you can do better")
        break

countdown(int(t))
