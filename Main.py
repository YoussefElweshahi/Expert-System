from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from frontend import Ui_Dialog
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.dom.minidom import Document
from xml.dom.minidom import *
import sys
import PySimpleGUI as sg


class FrontEND(Ui_Dialog, QMainWindow):
    def __init__(self):
        Ui_Dialog.__init__(self)
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        xmlFile = parse("Atrophy.xml")
        root = xmlFile.documentElement
        self.aDiseases = []
        self.aConcepts = []
        self.aProperties = []
        self.aValues = []
        self.allRules = root.getElementsByTagName("Rule")
        for rule in self.allRules:
            self.aDiseases.append(rule.getAttribute("name"))
            allTuples = rule.getElementsByTagName("Tuple")
            for tuplee in allTuples:
                concept = tuplee.getAttribute("Cpt")
                if concept in self.aConcepts:
                    continue
                else:
                    self.aConcepts.append(concept)
        self.allDiseases = self.aDiseases
        self.ui.disease_list.addItems(self.aDiseases)
        self.ui.concept_list.addItems(self.aConcepts)
        self.ui.concept_list.item(0).setSelected(True)

        self.ui.concept_list.itemSelectionChanged.connect(self.conceptSelected)

        self.ui.property_list.itemSelectionChanged.connect(self.propertySelected)

        self.ui.linkButton.clicked.connect(self.buttonClick)
        self.ui.clearmemory.clicked.connect(self.memoryClear)

    def conceptSelected(self):
        self.ui.property_list.reset()
        self.aProperties = []
        self.ui.property_list.clear()
        self.conceptSelected = self.ui.concept_list.selectedItems()
        self.conceptSelected = self.conceptSelected[0].text()
        for rule in self.allRules:
            allTuples = rule.getElementsByTagName("Tuple")
            for tuplee in allTuples:
                if tuplee.getAttribute("Cpt") == self.conceptSelected:
                    if tuplee.getAttribute("Prop") in self.aProperties:
                        continue
                    else:
                        self.aProperties.append(tuplee.getAttribute("Prop"))
                else:
                    continue
        self.ui.property_list.addItems(self.aProperties)
        self.ui.property_list.reset()

    def propertySelected(self):
        self.aValues = []
        self.ui.value_list.clear()
        self.conceptChanged = self.ui.concept_list.selectedItems()
        self.conceptChanged = self.conceptChanged[0].text()
        self.propertyChanged = self.ui.property_list.selectedItems()
        self.propertyChanged = self.propertyChanged[0].text()
        for rule in self.allRules:
            allTuples = rule.getElementsByTagName("Tuple")
            for tuplee in allTuples:
                if (
                    tuplee.getAttribute("Cpt") == self.conceptChanged
                    and tuplee.getAttribute("Prop") == self.propertyChanged
                ):

                    if tuplee.getAttribute("Val") in self.aValues:
                        continue
                    else:
                        self.aValues.append(tuplee.getAttribute("Val"))

                else:
                    continue
        self.ui.value_list.addItems(self.aValues)
        self.ui.value_list.item(0).setSelected(True)

    def buttonClick(self):
        self.memoryConcept = []
        memoryConcept = self.ui.concept_list.selectedItems()
        concept = memoryConcept[0].text()
        self.memoryConcept.append(memoryConcept[0].text())

        self.memoryProperty = []
        memoryProperty = self.ui.property_list.selectedItems()
        property = memoryProperty[0].text()
        self.memoryProperty.append(memoryProperty[0].text())

        self.memoryValue = []
        memoryValue = self.ui.value_list.selectedItems()
        value = memoryValue[0].text()
        self.memoryValue.append(memoryValue[0].text())

        self.memoryItems = []
        memory = concept + "-->" + property + "-->" + value
        self.memoryItems.append(memory)
        print(concept + property + value)
        self.ui.memory_list.addItems(self.memoryItems)
        count = 0
        self.temp = []
        for rule in self.allRules:
            if rule.getAttribute("name") in self.aDiseases:
                tuples = rule.getElementsByTagName("Tuple")
                for tuple in tuples:
                    if (
                        tuple.getAttribute("Cpt") == concept
                        and tuple.getAttribute("Prop") == property
                        and tuple.getAttribute("Val") == value
                    ):
                        self.temp.append(rule.getAttribute("name"))
            else:
                continue
        self.aDiseases = self.temp
        self.ui.disease_list.clear()
        self.ui.disease_list.addItems(self.aDiseases)
        self.ui.property_list.reset()

    def memoryClear(self):
        self.memoryItems = []
        self.ui.memory_list.clear()
        self.aDiseases = self.allDiseases
        self.ui.disease_list.clear()
        self.ui.disease_list.addItems(self.aDiseases)


def run_es():
    app = QApplication(sys.argv)
    FrontEND = FrontEND()
    FrontEND.show()
    app.exec_()


def edit_rules(xml_file):
    layout = [
        [sg.Text("Edit Rules")],
        [
            sg.Multiline(
                default_text=open(xml_file, "r").read(),
                size=(100, 50),
                key="-RULES-",
                font=("Arial", 10),
            )
        ],
        [sg.Push(), sg.Button("Save", key="-SAVE-")],
    ]

    window = sg.Window("Edit Rules", layout, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-SAVE-":
            with open(xml_file, "w") as f:
                f.write(values["-RULES-"])
            window.close()
            sg.popup("Saved")
            break


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
        app = QApplication(sys.argv)
        FrontEND = FrontEND()
        FrontEND.show()
        app.exec_()

    elif event == "-EDIT-":
        xml_file = sg.popup_get_file(
            "Select XML file",
            file_types=(("XML Files", "*.xml")),
            font=("Arial", 20),
        )
        edit_rules(xml_file)
