import os

for file_name in os.listdir():
    if os.path.isfile(file_name):
        print(file_name + ":")
        with open(file_name, "r") as fd:
            cnt = 0
            for line in fd.readlines():
                print(str(cnt) + ": " + line, end="")
                cnt += 1
        print()
