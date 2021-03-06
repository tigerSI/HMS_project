from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from Base.Widget_ComboBox import comboBoxClass


class WidgetManageAppointment(QWidget):
    def __init__(self, Person, parent=None):
        QWidget.__init__(self, None)
        self.Person = Person
        self.parent = parent
        self.initUI()
        self.initLayout()
        self.initConnect()
        self.setProxyView()
        self.setProxyModel()

    def initUI(self):
        path = 'Roommanager/View/Widget_ManagePersonUI.ui'
        pathForDev = './View/Widget_ManagePersonUI.ui'
        form = QUiLoader().load(path, self)
        self.proxyView = form.findChild(QTreeView, 'treeView')
        self.layoutSearch = form.findChild(QHBoxLayout, 'layout_search')
        self.b_edit = form.findChild(QPushButton, 'b_edit')
        self.b_newPerson = QPushButton("new " + self.Person)
        self.filterColumnComboBox = comboBoxClass.ComboBoxWithTypingSearch()
        self.filterPatternLineEdit = QLineEdit()

    def initLayout(self):
        self.layoutSearch.addWidget(self.filterColumnComboBox)
        self.layoutSearch.addWidget(self.filterPatternLineEdit)
        self.layoutSearch.addWidget(self.b_newPerson)

    def initConnect(self):
        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        self.b_edit.clicked.connect(self.editPerson)

    def editPerson(self):
        selection = self.proxyView.selectionModel().selectedRows()
        if selection is not None:
            case_id = selection[0].data()
            self.parent.editButtonPressed(case_id)

    "init Table"
    def setProxyView(self):
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setSortingEnabled(True)

    def setProxyModel(self):
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyView.setModel(self.proxyModel)

    def setComboBox(self, lstHead):
        model = QStandardItemModel()
        for i, word in enumerate(lstHead):
            item = QStandardItem(word)
            model.setItem(i, 0, item)
        self.filterColumnComboBox.setModel(model)
        self.filterColumnComboBox.setModelColumn(0)

    def setSourceModel(self, lstHead, lst_appointment):
        self.sizeOFHead = len(lstHead)
        self.setComboBox(lstHead)
        self.createBarSort(lstHead)
        self.addAllPerson(lst_appointment)
        self.proxyModel.setSourceModel(self.model)

    def createBarSort(self, lstHead):
        self.model = QStandardItemModel(0, len(lstHead), self)
        for i in range(self.sizeOFHead):
            self.model.setHeaderData(i, Qt.Horizontal, lstHead[i])

    def addAllPerson(self, lst_appointment):
        count = 0
        for appointment in lst_appointment:
            text = appointment.getDataForRoomManager()
            self.model.insertRow(count)
            for i in range(self.sizeOFHead):
                self.model.setData(self.model.index(count, i), text[i])
            count += 1

    def filterRegExpChanged(self):
        regExp = QRegExp(self.filterPatternLineEdit.text())
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tab1_widget = WidgetManageAppointment("Doctor")
    lstHead = ["NAME", "ID", "Position", "Phone"]
    allRow = [("Atichat", "001", "Brain", "0971249197"), ("Tiger", "002", "Chest", "0971249194")]
    tab1_widget.setSourceModel(lstHead, allRow)
    tab1_widget.show()
    sys.exit(app.exec_())

