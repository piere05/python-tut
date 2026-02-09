def demo(a, b, *args, **kwargs):
    print(a, str(b)+"sd")
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, name="Tom", age=30)