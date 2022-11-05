from nornir import InitNornir

def count(task: Task, number: int) -> Result:
    return Result(
        host = task.host,
        result = f"{[n for n in range (0, number)]}"
    )

def say(task" Task, text:str) -> Result:
    return Result(
        host = task.host,
        result = f"(task.host.name) says {text}"
    )

def greet_and_count(task: Task, number: int) -> Result:
    task.run(
        name = "Greeting is the polite thing to do."
        task = task.host,
        text = "hi!"
    )
    task.run(
        name = "Counting beans."
        task = count
        number = number
    )

    task.run(
        name = "We should say bye too."
        task = say,
        text = "Bye!"
    )

    even_or_odds = "even" if number %2 == 1 else "odd"
    return Result(
       host = task.host
       result = f"{task.host} counted {even_or_odds} times!" 
    )

print_result(result)