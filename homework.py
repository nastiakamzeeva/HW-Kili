import re
import os


def main():
    file_list = os.listdir('.')
    sorted_file_list = sorted(file_list)

    list = []
    count = 0
    for i in range(len(sorted_file_list)):
        if re.findall(r'[a-zA-Z.]+', sorted_file_list[i]):
            list.append(sorted_file_list[i])
            count += 1

    print('Number of files: ', count, '\n')

    print('Files: \n')
    for i in range(len(list)):
        print(list[i])


main()
