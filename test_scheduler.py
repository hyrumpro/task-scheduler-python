import datetime
import pytest
from smart_schedule_pro import SmartScheduler

def test_submit_task():
    scheduler = SmartScheduler()
    scheduler.name_var.set('Task 1')
    scheduler.duration_var.set('3')
    scheduler.deadline_var.set('2023-07-15')
    scheduler.priority_var.set('3')

    scheduler.submit_task()

    assert len(scheduler.tasks) == 1
    assert scheduler.tasks[0]['name'] == 'Task 1'
    assert scheduler.tasks[0]['duration'] == 3
    assert scheduler.tasks[0]['deadline'] == datetime.datetime.strptime('2023-07-15', '%Y-%m-%d').date()
    assert scheduler.tasks[0]['priority'] == 3
    assert scheduler.tasks[0]['completed'] is False

def test_complete_task():
    scheduler = SmartScheduler()
    task = {'name': 'Task 1', 'duration': 3, 'deadline': datetime.date.today(), 'priority': 3, 'completed': False}
    scheduler.tasks.append(task)

    scheduler.complete_task(0)

    assert scheduler.tasks[0]['completed'] is True

def test_delete_task():
    scheduler = SmartScheduler()
    task1 = {'name': 'Task 1', 'duration': 3, 'deadline': datetime.date.today(), 'priority': 3, 'completed': False}
    task2 = {'name': 'Task 2', 'duration': 2, 'deadline': datetime.date.today(), 'priority': 2, 'completed': False}
    scheduler.tasks.extend([task1, task2])

    scheduler.delete_task(1)

    assert len(scheduler.tasks) == 1
    assert scheduler.tasks[0]['name'] == 'Task 1'


# Run Test pro
if __name__ == "__main__":
    pytest.main()


