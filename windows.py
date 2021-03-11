from win10toast import ToastNotifier
import time


def countdown(t):
    print('Timer running: {0} minutes\nPress Ctrl + C for pause!'.format(t / 60))
    t -= 1
    while t > -1:
        try:
            minute, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(minute, secs)
            print('\r', timer, end=' remaining')
            time.sleep(1)
            t -= 1
        except KeyboardInterrupt:
            input('\nPlease press enter to continue')
    print("\n")


def show_toaster(cycle, cycles, status, time_left, title_text, toast_duration):
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


def main():
    workTime = 25
    smallBreakTime = 5
    bigBreakTime = 15
    toastDuration = 5

    cycleNumber = get_input("Enter number of cycles: ")
    workTime = get_input('Enter work time (default: {0}): '.format(workTime))
    if cycleNumber > 1:
        smallBreakTime = get_input('Enter break time (default: {0}): '.format(smallBreakTime))
    if cycleNumber > 4:
        bigBreakTime = get_input('Enter big break time (default: {0}): '.format(bigBreakTime))

    for cycleNo in range(1, cycleNumber + 1):
        print('Starting cycle {0}/{1}' .format(cycleNo, cycleNumber))
        show_toaster(cycleNo, cycleNumber, "work", workTime, "has started", toastDuration)
        countdown(workTime * 60)
        if cycleNo != cycleNumber:
            if cycleNo % 4 != 0:
                show_toaster(cycleNo, cycleNumber, "break", smallBreakTime, "has started", toastDuration)
                countdown(smallBreakTime * 60)
            elif cycleNo % 4 == 0:
                show_toaster(cycleNo, cycleNumber, "big break", bigBreakTime, "has started", toastDuration)
                countdown(bigBreakTime * 60)

    ToastNotifier().show_toast("Done", "Pomodoro timer is done", None, 10)


if __name__ == "__main__":
    main()
