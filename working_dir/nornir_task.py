from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# A task is a reusable piece of code that implements some functionality for a single host.
# In python terms it is a function that takes a Task as first paramater and returns a Result.

def say(task: Task, text: str, text2: str) -> Result:
    return Result(
        host = task.host,
        result = f"{task.host.name} says {text} and {text2}"
    )

# Tasks can also take any number of arguments to extend their functionality.
# This example specifies the value for the extra argument "text"
result = nr.run(
    # The "name" argument gives the task a descriptive name.
    name = "Kids holiday",
    task = say,
    text = "Happy Halloween",
    text2 = "Bye!"
)

print_result(result)
