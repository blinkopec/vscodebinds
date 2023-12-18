# output vscode keybinds in terminal
from art import tprint
import tabulate
from InquirerPy import inquirer
import os

def search():
    bind = input()

    with open(path, 'r') as file:
        content = file.readlines()

        for line in content:
            if bind in line.strip():
                print(line.strip())

def deleteInFile(theme, bind):
    result = list()
    with open(path, "r") as file:
        content = file.readlines()
        isTheme = False

        for line in content:
            if isTheme:
                if line.strip() == bind:
                    result = moveFileTextDelete(content.index(line), content)

            if line.strip() == theme:
                isTheme = True

    with open(path, "w") as file:
        for line in result:
            for i in line:
                file.write(i)


def selectDeleteLine(theme):
    with open(path, "r") as file:
        content = file.readlines()
        isTheme = False
        result = []
        for line in content:
            if isTheme:
                if line.strip() == "end":
                    break

                result.append(line.strip())

            if line.strip() == theme:
                isTheme = True

        inputTextBind = inquirer.select(
            message="select delete keybind",
            choices=result,
        ).execute()

        return inputTextBind


def moveFileTextDelete(number, text):
    result = list()
    truefalse = False

    for line in text:
        if text.index(line) == number:
            continue
        result.append(line)

    return result


def writeInFile(theme, text, bind):
    result = list()
    with open(path, "r") as file:
        content = file.readlines()
        isTheme = False
        for line in content:
            if isTheme:
                if line.strip() == "end":
                    break

                if content.index(line) == len(content) - 1:
                    result = moveFileText(content, content.index(line), text, bind)
                    break

                if content.index(line) < len(content) - 1:
                    if content[content.index(line) + 1].strip() == "end":
                        result = moveFileText(content, content.index(line), text, bind)
                        break

            if line.strip() == theme:
                isTheme = True

    if len(result) > 0:
        with open(path, "w") as file:
            for line in result:
                for i in line:
                    file.write(i)


def moveFileText(text, number, inputText, inputBind):
    tmp = len(text)
    result = list()
    tmplist = list()
    truefalse = False

    for line in text:
        if truefalse:
            tmplist.append(line)
        else:
            result.append(line)

        if text.index(line) == number:
            truefalse = True
            x = [inputText + ", ", inputBind + "\n"]
            result.append(x)

    result.extend(tmplist)
    return result


def readfile(theme):
    with open(path, "r") as file:
        content = file.readlines()
        isTheme = False
        result = []
        for line in content:
            if isTheme:
                if line.strip() == "end":
                    break

                result.append(line.split(","))

            if line.strip() == theme:
                isTheme = True

        out = tabulate.tabulate(result)
        print(out)


def select_theme():
    inputString = inquirer.select(
        message="[s] shortcuts [e] editor tips [b] basic [h] hm [ext] extensions [srch] search keybind [add] add keybind [del] delete keybind [exit] exit",
        choices=["s", "e", "b", "h", "ext", "srch", "add", "del", "exit"],
    ).execute()

    match inputString:
        case "s":
            return "shortcuts"
        case "e":
            return "tips"
        case "b":
            return "basics"
        case "h":
            return "hms"
        case "ext":
            return "exts"
        case "srch":
            return 'srch'
        case "add":
            return "add"
        case "del":
            return "del"
        case "exit":
            exit()


if __name__ == "__main__":
    tprint("vscodebinds")
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + 'data.txt'

    theme = select_theme()
    if theme == "add":
        inputTheme = inquirer.select(
            message="insert bind theme: [s] shortcuts [e] editor tips [b] basic [h] hm [ext] extensions",
            choices=["s", "e", "b", "h", "ext", "exit"],
        ).execute()
        tmpTheme = "null"

        match inputTheme:
            case "s":
                tmpTheme = "shortcuts"
            case "e":
                tmpTheme = "tips"
            case "b":
                tmpTheme = "basics"
            case "h":
                tmpTheme = "hms"
            case "ext":
                tmpTheme = "exts"
            case "exit":
                exit()

        print("insert bind text: ")
        text = input()
        print("insert keybind: ")
        bind = input()
        writeInFile(tmpTheme, text, bind)

    if theme == "del":
        inputTheme = inquirer.select(
            message="insert bind theme: [s] shortcuts [e] editor tips [b] basic [h] hm [ext] extensions",
            choices=["s", "e", "b", "h", "ext", "exit"],
        ).execute()
        tmpTheme = "null"

        match inputTheme:
            case "s":
                tmpTheme = "shortcuts"
            case "e":
                tmpTheme = "tips"
            case "b":
                tmpTheme = "basics"
            case "h":
                tmpTheme = "hms"
            case "ext":
                tmpTheme = "exts"
            case "exit":
                exit()

        bind = selectDeleteLine(tmpTheme)
        deleteInFile(tmpTheme, bind)

    if theme == 'srch':
        search()

    readfile(theme)
