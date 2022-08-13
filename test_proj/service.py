from test_proj.model import Request


def sum_func(request: Request):
    if request.a == 1:
        raise Exception("Unwanted value for a")
    if request.b == 1:
        raise ValueError("Unwanted value for b")
    return request.a + request.b
