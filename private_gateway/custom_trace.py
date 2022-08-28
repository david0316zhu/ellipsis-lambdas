import sys
import traceback


def log_trace_message():
    """ This function helps to log the stack trace for error."""
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)