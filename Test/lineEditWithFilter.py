import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class SimpleListModel(QAbstractListModel):
    def __init__(self, contents):
        super(SimpleListModel, self).__init__()
        self.contents = contents

    def rowCount(self, parent):
        return len(self.contents)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self.contents[index.row()])


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        data = ['Red1', 'Red2', 'Blue', 'Yellow', 'boss', 'tiger', 'gift', 'eiei', 'wanna play ow']
        self.model = SimpleListModel(data)

        self.view = QListView(self)

        self.proxy = QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.proxy.setDynamicSortFilter(True)
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.view.setModel(self.proxy)

        self.search = QLineEdit(self)
        self.search.setFocus()

        layout = QGridLayout()
        layout.addWidget(self.search, 0, 0)
        layout.addWidget(self.view, 1, 0)

        self.setLayout(layout)

        # Connect search to proxy model
        self.connect(self.search, SIGNAL('textChanged(QString)'),
                     self.proxy.setFilterFixedString)

        # Moved after connect for self.proxy.setFilterFixedString
        self.connect(self.search, SIGNAL('textChanged(QString)'),
                     self.force_selection)

        self.connect(self.search, SIGNAL('returnPressed()'),
                     self.output_index)

    # @QtCore.Slot(QtCore.QModelIndex)
    Slot(str)
    def force_selection(self, ignore):
        """ If user has not made a selection, then automatically select top item.
        """
        selection_model = self.view.selectionModel()
        indexes = selection_model.selectedIndexes()

        if not indexes:
            index = self.proxy.index(0, 0)
            selection_model.select(index, QItemSelectionModel.Select)

    def output_index(self):
        print
        ('View Index:', self.view.currentIndex().row())
        print
        ('Selected Model Current Index:', self.view.selectionModel().currentIndex())
        print
        ('Selected Model Selected Index:', self.view.selectionModel().selectedIndexes())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
