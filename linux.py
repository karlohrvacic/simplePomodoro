import notify2
import time
import beepy


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


def send_notification(title, content, duration):
    notify2.init("Simple Pomodoro Notification")
    notification = notify2.Notification("Simple Pomodoro Notifier")
    notification.set_urgency(notify2.URGENCY_NORMAL)
    notification.set_timeout(duration * 1000)
    notification.update(title, content)
    notification.show()
    beepy.beep(sound=1)


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
    work_time = 25
    small_break_time = 5
    big_break_time = 15
    toast_duration = 5

    cycle_number = get_input("Enter number of cycles: ")
    work_time = get_input('Enter work time (default: {0}): '.format(work_time))
    if cycle_number > 1:
        small_break_time = get_input('Enter break time (default: {0}): '.format(small_break_time))
    if cycle_number > 4:
        big_break_time = get_input('Enter big break time (default: {0}): '.format(big_break_time))

    for cycleNo in range(1, cycle_number + 1):
        print('Starting cycle {0}/{1}' .format(cycleNo, cycle_number))
        send_notification('[{0}/{1}]'.format(cycleNo, cycle_number), 'Work timer has started\nTimer running: {0} '
                                                                     'minutes left.'.format(work_time), toast_duration)
        countdown(work_time * 60)
        if cycleNo != cycle_number:
            if cycleNo % 4 != 0:
                send_notification('[{0}/{1}]'.format(cycleNo, cycle_number),
                                  'Break timer has started\nTimer running: {0} minutes left.'.format(small_break_time),
                                  toast_duration)
                countdown(small_break_time * 60)
            elif cycleNo % 4 == 0:
                send_notification('[{0}/{1}]'.format(cycleNo, cycle_number),
                                  'Big break timer has started'
                                  '\nTimer running: {0} minutes left.'.format(big_break_time), toast_duration)
                countdown(big_break_time * 60)

    send_notification("Timer is Done!", "Pomodoro Timer is Done!", toast_duration)


if __name__ == "__main__":
    main()
