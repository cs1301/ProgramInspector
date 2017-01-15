def basic_program():
    x = 5
    while x > 0:
        x -= 1


def optimized_case():
    while False:
        pass


def nested_cases():
    while True:
        while True:
            print("test")

    def test():
        x = 3
        while x < 5:
            print("x < 5")
            while True:
                pass

    class Test:
        def __init__(self):
            while True:
                print("pass")


def mixed_loops():
    for x in range(5):
        while True:
            while 5 in [x for x in range(5)]:
                for x in [x for x in range(5)]:
                    while [x for x in range(5)]:
                        pass

x = 0
while x < 5:
    x += 1
