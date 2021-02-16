from win10toast import ToastNotifier
import time

workTime = 25
breakTime = 5


def countdown(t):
    print('Timer running: {0} minutes'.format(t / 60))
    while t:
        minute, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minute, secs)
        print('\r', timer, end='')
        time.sleep(1)
        t -= 1
    print("\n")


def show_toaster(cycle, cycles, status, time_left, toast_duration, title_text):
    title = '{0}/{1} {2} timer {3}!'.format(cycle, cycles, status, title_text)
    message = 'You have {0} minutes of {1} time'.format(time_left, status)
    ToastNotifier().show_toast(title, message, None, toast_duration)


def get_input(text):
    running = True
    while running:
        try:
            tmp = int(input(text))
            running = False
            return tmp
        except ValueError:
            print("Wrong input!")


cycleNumber = get_input("Enter number of cycles: ")
workTime = get_input('Enter work time (default: {0}): '.format(workTime))
if cycleNumber > 1:
    breakTime = get_input('Enter break time (default: {0}): '.format(breakTime))

for cycleNo in range(1, cycleNumber + 1):
    print('Starting cycle {0}/{1}' .format(cycleNo, cycleNumber))
    show_toaster(cycleNo, cycleNumber, "work", workTime, 10, "has started")
    countdown(workTime * 60)
    if cycleNo != cycleNumber:
        show_toaster(cycleNo, cycleNumber, "break", breakTime, 10, "has started")
        countdown(breakTime * 60)

ToastNotifier().show_toast("Done", "Pomodoro timer is done", None, 10)
