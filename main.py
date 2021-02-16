from win10toast import ToastNotifier
import time

workTime = 25
breakTime = 5


def countdown(t):
    print('Timer running: {0} minutes'.format(t / 60))
    while t:
        time.sleep(1)
        t -= 1


def show_toaster(cycle, cycles, status, time_left, toast_duration):
    title = '{0}/{1} {2} timer is Up!'.format(cycle, cycles, status)
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
breakTime = get_input('Enter break time (default: {0}): '.format(breakTime))

for cycleNo in range(1, cycleNumber + 1):
    print('Starting cycle {0}/{1}' .format(cycleNo, cycleNumber))
    countdown(workTime * 60)
    show_toaster(cycleNo, cycleNumber, "break", breakTime, 10)
    countdown(breakTime * 60)
    if cycleNo != cycleNumber:
        show_toaster(cycleNo, cycleNumber, "work", workTime, 5)

ToastNotifier().show_toast("Done", "Pomodoro timer is done", None, 10)
