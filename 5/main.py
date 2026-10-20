import doctest

def run_all(*tasks : tuple) -> list[dict]:
    """Виконує список задач та повертає звіт про виконання кожної з них.

    >>> def half(x): return x / 2
    >>> run_all((half, 10), (int, "x"), (divmod, 7, 0), (max, [3, 9]))
    [{'name': 'half', 'result': 5.0, 'status': 'ok'}, {'name': 'int', 'error': 'ValueError'}, {'name': 'divmod', 'error': 'ZeroDivisionError'}, {'name': 'max', 'result': 9, 'status': 'ok'}]
    
    >>> run_all()
    []

    >>> def get_zero(): return 0
    >>> def bad_index(): return [][0]
    >>> run_all((get_zero,), (bad_index,), (len, 123))
    [{'name': 'get_zero', 'result': 0, 'status': 'ok'}, {'name': 'bad_index', 'error': 'IndexError'}, {'name': 'len', 'error': 'TypeError'}]
    
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


if __name__ == "__main__":
    doctest.testmod(verbose=True)