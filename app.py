import PySimpleGUI as sg
import os


def load_xml():
    rule_tem = open("./temp/rule", "r").readlines()
    tup_tem = open("./temp/tup", "r").read()

    xml_file = open("Atrphy.xml", "r").readlines()
    return xml_file


def edit_rules():
    rule_tem = open("./temp/rule", "r").readlines()
    tup_tem = open("./temp/tup", "r").read()

    xml_file = open("Atrphy.xml", "r").read()
    tups = []
    rule_name = sg.popup_get_text("Enter Rule Name", font=("Arial", 20))
    how_many = sg.popup_get_text("How many tuples?", font=("Arial", 20))
    how_many = int(how_many)
    for i in range(how_many):
        cpt = sg.popup_get_text(f"Enter concept for tuple {i+1}", font=("Arial", 20))
        prop = sg.popup_get_text(f"Enter property for tuple {i+1}", font=("Arial", 20))
        val = sg.popup_get_text(f"Enter value for tuple {i+1}", font=("Arial", 20))
        tups.append({"cpt": cpt, "prop": prop, "value": val})

    rule = {"name": rule_name, "tuples": tups}
    rule_txt = rule_tem[0].format(**rule) + "\n"
    for tup in rule["tuples"]:
        rule_txt += tup_tem.format(**tup) + "\n"
    rule_txt += rule_tem[1]

    xml_file1 = xml_file.split('<rule name="one"/></Disease>')[0]
    xml_file1 = xml_file1 + "\n" + rule_txt + "\n" + '<rule name="one"/></Disease>'
    with open("Atrphy.xml", "w") as f:
        f.write(xml_file1)


def main():
    main_layout = [
        [sg.Button("Start", key="-START-", font=("Arial", 20))],
        [sg.Button("Edit Rules", key="-EDIT-", font=("Arial", 20))],
    ]

    window = sg.Window("Main Menu", main_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-START-":
            curr = os.getcwd()
            os.chdir(curr)
            os.system("python Main.py")

        elif event == "-EDIT-":
            edit_rules()


main()
