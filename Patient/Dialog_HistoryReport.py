from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
import Setting as s

class HistoryReport(QDialog):
    def __init__(self, part_pre, part_intra, part_post, parent=None):
        super(HistoryReport, self).__init__(parent)
        posX, posY, sizeW, sizeH = s.GEOMETRY_DIALOG_HISTORY_REPORT
        self.setGeometry(posX, posY, sizeW, sizeH)
        self.part_pre = part_pre
        self.part_intra = part_intra
        self.part_post = part_post
        self.initUI()
        self.initLayout()
        self.show()

    def initUI(self):
        self.loader = QUiLoader()
        self.ui = self.loader.load('../Patient/view/Widget_HistoryReport.ui', self)
        self.b_cancel = self.ui.findChild(QPushButton, "b_cancel")
        self.b_cancel.clicked.connect(self.cancel)

    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def setPreData(self):
        self.part_pre
        #For loop self.part_pre get
         #set label
        pass

    def setIntraData(self):
        self.part_intra
        # For loop self.part_intra get
        # set label
        pass

    def setPostData(self):
        self.part_post
        # For loop self.part_post get
        # set label
        pass

    def forDev(self):
        pass

    def cancel(self):
        pass

