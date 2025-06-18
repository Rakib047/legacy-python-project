# legacy_task_scheduler.py

import time

# A simple task decorator (old way)
def task_decorator(func):
    def wrapper(*args, **kwargs):
        print "Starting task: %s" % func.__name__
        result = func(*args, **kwargs)
        print "Task %s completed." % func.__name__
        return result
    return wrapper

@task_decorator
def run_task(task_name):
    time.sleep(2)  # Simulate a task taking time
    print "Task %s is running." % task_name

def main():
    tasks = ['Task 1', 'Task 2', 'Task 3']
    for task in tasks:
        try:
            run_task(task)
        except Exception, e:
            print "Error while executing task %s: %s" % (task, e)

if __name__ == "__main__":
    main()
