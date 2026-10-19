import doctest

def run_all(*tasks : tuple) -> list[dict]:
    """Виконує список задач та повертає звіт про виконання кожної з них.
    >>> def half(x): return x / 2
    >>> run_all((half, 10), (int, "x"), (divmod, 7, 0), (max, [3, 9]))
    [{'name': 'half', 'result': 5.0, 'status': 'ok'}, {'name': 'int', 'error': 'ValueError'}, {'name': 'divmod', 'error': 'ZeroDivisionError'}, {'name': 'max', 'result': 9, 'status': 'ok'}]
    """
    
    results = []

    for task in tasks:

        funk = task[0]
        args = task[1:]
        entry = {}

        try:
            res = funk(*args)
        except Exception as e:
            entry = {
                "name": funk.__name__,
                "error": type(e).__name__,
            }
        else:
            entry = {
                "name": funk.__name__,
                "result": res,
                "status": "ok"
            }
        finally:
            results.append(entry)

    return results
    
    # try:
    #     result = []
    #     for task,arg in tasks:
    #         result.append(task(arg))
    # except Exception as e:
    #     print(f"err - {e.__class__}")
    # else:
    #     print(result)
    # finally:
    #     pass

if __name__ == "__main__":
    doctest.testmod(verbose=True)