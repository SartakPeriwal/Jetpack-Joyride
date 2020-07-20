"""Defining input class."""
import sys
import termios
import tty
import signal

# class Get:
#     """Class to get input."""

#     def __call__(self):
#         """Defining __call__."""
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


# def input_to(getch, timeout=0.1):
#     """Taking input from user."""
#     signal.signal(signal.SIGALRM, alarmHandler)
#     signal.setitimer(signal.ITIMER_REAL, timeout)
#     try:
#         text = getch()
#         signal.alarm(0)
#         return text
#     except AlarmException:
#         signal.signal(signal.SIGALRM, signal.SIG_IGN)
#         return None

class _getChUnix:
    '''class to take input'''

    def __call__(self):
        '''def to call function'''
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar

def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmHandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = _getChUnix()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
