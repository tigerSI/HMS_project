import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Tab2ManagePatient(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        form = loader.load('./view/tab2_manage_patient.ui', self)
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.sourceGroupBox = QGroupBox("All Patient's List")
        self.proxyGroupBox = QGroupBox("Selected Patient's List")

        self.proxyView = form.findChild(QTreeView, 'treeView')
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.sortCaseSensitivityCheckBox = QCheckBox("Case sensitive sorting")
        self.filterCaseSensitivityCheckBox = QCheckBox("Case sensitive filter")

        self.filterPatternLineEdit = form.findChild(QLineEdit, 'lineEdit_search')
        self.filterColumnComboBox = form.findChild(QComboBox, 'comboBox')

        ## checking
        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        self.filterCaseSensitivityCheckBox.toggled.connect(self.filterRegExpChanged)
        self.sortCaseSensitivityCheckBox.toggled.connect(self.sortChanged)

    def setSourceModel(self, model):
        self.proxyModel.setSourceModel(model)


    def filterRegExpChanged(self):
        if self.filterCaseSensitivityCheckBox.isChecked():
            caseSensitivity = Qt.CaseSensitive
        else:
            caseSensitivity = Qt.CaseInsensitive

        regExp = QRegExp(self.filterPatternLineEdit.text(), caseSensitivity)
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex())

    def sortChanged(self):
        if self.sortCaseSensitivityCheckBox.isChecked():
            caseSensitivity = Qt.CaseSensitive
        else:
            caseSensitivity = Qt.CaseInsensitive

        self.proxyModel.setSortCaseSensitivity(caseSensitivity)


def addMail(model, Name, Date, Doctor, Phone, Status):
    model.insertRow(0)
    model.setData(model.index(0, 0), Name)
    model.setData(model.index(0, 1), Date)
    model.setData(model.index(0, 2), Doctor)
    model.setData(model.index(0, 3), Phone)
    model.setData(model.index(0, 4), Status)


def createMailModel(parent):
    model = QStandardItemModel(0, 5, parent)
    model.setHeaderData(0, Qt.Horizontal, "Name")
    model.setHeaderData(1, Qt.Horizontal, "Date")
    model.setHeaderData(2, Qt.Horizontal, "Doctor")
    model.setHeaderData(3, Qt.Horizontal, "Phone")
    model.setHeaderData(4, Qt.Horizontal, "Status")

    addMail(model, "tiger", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    addMail(model, "boss", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    addMail(model, "gift", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    addMail(model, "red", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    addMail(model, "red1", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    addMail(model, "red2", QDate(2006, 12, 31), 'Ph.D. Tiger', '123456789', 'okay')
    return model


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setSourceModel(createMailModel(window))
    window.show()
    sys.exit(app.exec_())

