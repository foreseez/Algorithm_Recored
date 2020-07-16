


def run(x,y):
    print(x,y)


if __name__ == "__main__":
    try:
        ls = input("输入x,y\n").split("|")
        x = int(ls[0])
        y = int(ls[-1])
        run(x,y)
    except EXception as e:
        print(e)


