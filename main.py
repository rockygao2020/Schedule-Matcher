from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QRadioButton, QButtonGroup, QLineEdit, QPlainTextEdit
from PyQt6.QtCore import Qt
from schedule_matcher import getStrings, getLists, getLists2, findLCS

'''
Run this File to start the program
Frontend PyQt6 Code

The following 2 PyQt functions <deleteItemsOfLayout> and <Window.boxDelete> are taken from The Trowser and Brendan Abel at
https://stackoverflow.com/questions/37564728/pyqt-how-to-remove-a-layout-from-a-layout. These 2 functions 
helped me trememdously when it came to swapping layouts for the GUI
'''

def deleteItemsOfLayout(layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.setParent(None)
             else:
                 deleteItemsOfLayout(item.layout())

class Window(QMainWindow):
	

	def __init__(self):
		super().__init__()

		#Main Window Settings
		self.setMinimumSize(900, 700)
		self.setWindowTitle("Schedule Matcher")
		
		#General Font for all widgets
		self.font = self.font()
		self.font.setPointSize(15)
		self.font.setBold(False)

		#Super Layout (switch between Layout 1 and 2)
		self.layout_super = QVBoxLayout()

		#Super Layout Row 0, Col 0 (Description of Algorithm)
		self.description = QPlainTextEdit()
		self.description.setPlainText("Given 2 ordered sequences, this program finds their longest common sequence (LCS). For example, the sequences \'ABGHCDL\' and \'BDLGHC\' have an LCS of \'BGHC\'. The \'Symbols\' mode takes in 2 strings, and matches the symbols.  The \'Strings\' mode takes in 2 LISTS of strings, and matches the strings.")
		self.description.setReadOnly(True)
		self.description.setFont(self.font)
		self.description.setMaximumSize(550, 200)


		#Super Layout Row 0, Col 1 (Super controls, for switching)
		#	Button Group for 2 button widgets (choose between strings or spaces)
		#		Symbols matches longest substring; matches characters with one another
		#		Strings interprets each word, separated by a space, as an symbol to match
		self.buttonGroupSuper = QButtonGroup()
		self.buttonGroupSuper.setExclusive(True)
		self.buttonGroupSuper.buttonClicked.connect(self.super_clicked_handler)

		self.radioButtonSymbols = QRadioButton("Symbols")
		self.radioButtonSymbols.setFont(self.font)
		self.radioButtonSymbols.setChecked(True)

		self.radioButtonStrings = QRadioButton("Strings")
		self.radioButtonStrings.setFont(self.font)
		

		#Try Formatting Row0 by shrinking Button width
		self.radioButtonSymbols.setMaximumWidth(100)
		self.radioButtonStrings.setMaximumWidth(100)

        
		self.buttonGroupSuper.addButton(self.radioButtonStrings)
		self.buttonGroupSuper.addButton(self.radioButtonSymbols)

		#Put the Buttons in their own sub-layout
		layout_radioButtons_super = QVBoxLayout()
		layout_radioButtons_super.addWidget(self.radioButtonSymbols)
		layout_radioButtons_super.addWidget(self.radioButtonStrings)


		#Combine Both Super Layer Row0Col0 and Row0Col1:
		layout_super_row0 = QHBoxLayout()
		layout_super_row0.addWidget(self.description)
		layout_super_row0.addLayout(layout_radioButtons_super)

		#Add Super Layer Row0(ultimate) to Super Layout
		self.layout_super.addLayout(layout_super_row0)

		#Make layout 1
		self.make_layout1()
		#Make layout 2
		self.make_layout2()

		#Add Layout 1 to Super Layout
		self.layout_super.addLayout(self.layout1)

		#Link main layout to a temp widget > this becomes the center widget
		#	required for the layout to actually show up
		centerWidget = QWidget()
		centerWidget.setLayout(self.layout_super)
		self.setCentralWidget(centerWidget)

		'''=========================================================================='''
		#note that when the user clicks the superswitch to the 'strings' option, we shall
		#	abandon layout 1 in favor of layout 2

	def make_layout1(self):
		'''=========================================================================='''	
		#Main Layout #1
		self.layout1 = QGridLayout()

		#First 3 Rows (SeqA, SeqB, LCS output)
		self.aLabel = QLabel("Seq A: ")
		self.aLabel.setFont(self.font)
		self.aLabel.setMaximumWidth(130)
		self.bLabel = QLabel("Seq B: ")
		self.bLabel.setFont(self.font)
		self.cLabel = QLabel("LCS  : ")
		self.cLabel.setFont(self.font)

		self.aInput = QLineEdit()
		self.aInput.setFont(self.font)
		self.bInput = QLineEdit()
		self.bInput.setFont(self.font)
		self.cOutput = QLineEdit()
		self.cOutput.setReadOnly(True)
		self.cOutput.setFont(self.font)
		self.cOutput.setPlaceholderText("Returns Longest Common Seq between A and B")

		#Formatting and adding the 3 rows to the main layout
		self.cLabel.setMaximumHeight(50)
		self.cOutput.setMaximumHeight(50)

		self.layout1.addWidget(self.aLabel, 0, 0, 1, 1)
		self.layout1.addWidget(self.bLabel, 1, 0, 1, 1)
		self.layout1.addWidget(self.cLabel, 2, 0, 1, 1)
		self.layout1.addWidget(self.aInput, 0, 1, 1, 2)
		self.layout1.addWidget(self.bInput, 1, 1, 1, 2)
		self.layout1.addWidget(self.cOutput, 2, 1, 1, 2)

		#Button Group for 2 button widgets (choose between strings or spaces)z
		#	Strings matches longest substring; matches characters with one another
		#	Spaces interprets each word, separated by a space, as an symbol to match
		self.buttonGroup = QButtonGroup()
		self.buttonGroup.setExclusive(True)
		self.checkBoxStrings = QRadioButton("Symbols")
		self.checkBoxStrings.setFont(self.font)
		self.checkBoxLists = QRadioButton("Strings")
		self.checkBoxLists.setFont(self.font)
		self.checkBoxStrings.setChecked(True)
        
		self.buttonGroup.addButton(self.checkBoxStrings)
		self.buttonGroup.addButton(self.checkBoxLists)

		#Put the Buttons in their own sub-layout
		layout_radioButtons = QVBoxLayout()
		layout_radioButtons.addWidget(self.checkBoxStrings)
		layout_radioButtons.addWidget(self.checkBoxLists)

		#Create 2 other widgets, Button and Length
		self.button = QPushButton("Find LCS")
		self.button.setFont(self.font)
		self.button.setMinimumSize(100,100)
		self.button.setMaximumSize(200,200)
		self.button.clicked.connect(self.clickHandler)

		self.length = QLabel("Length: ")
		self.length.setFont(self.font)

		#Put the Length widgets into a sub-layout
		self.lengthOutput = QLineEdit()
		self.lengthOutput.setReadOnly(True)
		self.lengthOutput.setPlaceholderText("Returns LCS length")
		self.lengthOutput.setFont(self.font)
		self.lengthOutput.setMaximumWidth(250)

		layout_length = QVBoxLayout()
		layout_length.addWidget(self.length)
		layout_length.addWidget(self.lengthOutput)

		#Add 2 sub-layouts (2 checkboxes and length display) and Button to main layout
		self.layout1.addLayout(layout_radioButtons, 3, 0)
		self.layout1.addWidget(self.button, 3, 1)
		self.layout1.addLayout(layout_length, 3, 2)

		#Formatting to keep the super switch at same y level
		self.layout1.setVerticalSpacing(120)

	def make_layout2(self):
		#Layout 2
		self.layout2 = QGridLayout()

		#Row 0
		self.seq_a2 = QLabel("Seq A:")
		self.seq_a2.setFont(self.font)
		self.seq_b2 = QLabel("Seq B:")
		self.seq_b2.setFont(self.font)
		self.LCS2 = QLabel("LCS:")
		self.LCS2.setFont(self.font)

		self.layout2.addWidget(self.seq_a2, 0, 0)
		self.layout2.addWidget(self.seq_b2, 0, 2)
		self.layout2.addWidget(self.LCS2, 0, 1)

		#Row 1
		self.seq_a2_input = QPlainTextEdit()
		self.seq_a2_input.setFont(self.font)
		self.seq_a2_input.setPlaceholderText("Input a sequence")
		self.seq_a2_input.setMinimumHeight(418)

		self.seq_b2_input = QPlainTextEdit()
		self.seq_b2_input.setFont(self.font)
		self.seq_b2_input.setPlaceholderText("Input a sequence")

		self.LCS2_output = QPlainTextEdit()
		self.LCS2_output.setFont(self.font)
		self.LCS2_output.setReadOnly(True)
		self.LCS2_output.setPlaceholderText("Returns the LCS")

		self.layout2.addWidget(self.seq_a2_input, 1, 0)
		self.layout2.addWidget(self.seq_b2_input, 1, 2)
		self.layout2.addWidget(self.LCS2_output, 1, 1)

		#Row 2
		self.button2 = QPushButton("Find LCS")
		self.button2.setFont(self.font)
		self.button2.setMinimumSize(100,100)
		self.button2.setMaximumSize(200,200)
		self.button2.clicked.connect(self.clickHandler2)

		self.length2 = QLabel("Length: ")
		self.length2.setFont(self.font)

		#Put the Length widgets into a sub-layout
		self.lengthOutput2 = QLineEdit()
		self.lengthOutput2.setReadOnly(True)
		self.lengthOutput2.setPlaceholderText("Returns LCS length")
		self.lengthOutput2.setFont(self.font)
		self.lengthOutput2.setMaximumWidth(250)

		self.layout_length2 = QVBoxLayout()
		self.layout_length2.addWidget(self.length2)
		self.layout_length2.addWidget(self.lengthOutput2)

		self.layout2.addWidget(self.button2, 2, 1)
		self.layout2.addLayout(self.layout_length2, 2, 2, 1, 1)

	def super_clicked_handler(self):
		self.super_mode = ""
		for button in self.buttonGroupSuper.buttons():
			if button.isChecked():
				self.super_mode = button.text()
				break
		if self.super_mode == "Symbols":
			#Remove unconditionally the layout 1 or 2
			self.boxdelete(self.layout1)
			self.boxdelete(self.layout2)
			#Replace whatever was removed with layout 1
			self.make_layout1()
			self.layout_super.addLayout(self.layout1)
		else:
			#Remove unconditionally the layout 1 or 2
			self.boxdelete(self.layout1)
			self.boxdelete(self.layout2)
			#Replace whatever was removed with layout 2
			self.make_layout2()
			self.layout_super.addLayout(self.layout2)


	def boxdelete(self, box):
	    for i in range(self.layout_super.count()):
	        layout_item = self.layout_super.itemAt(i)
	        if layout_item.layout() == box:
	            deleteItemsOfLayout(layout_item.layout())
	            self.layout_super.removeItem(layout_item)
	            break


	def clickHandler(self):
		self.mode = ""
		for button in self.buttonGroup.buttons():
			if button.isChecked():
				self.mode = button.text()
				break

		#Self is the actual front-end name of the checkbox (in ButtonGroup), not its variable name
		#getStrings and getLists splits up the sequences either by Strings or Spaces/Lists
		if self.mode == "Symbols":
			seq_a, len_a, seq_b, len_b = getStrings(self.aInput.text(), self.bInput.text())
		else:
			seq_a, len_a, seq_b, len_b = getLists(self.aInput.text(), self.bInput.text())

		#findLCS is the main backend function; dynamic programming LCS alg
		LCS, length = findLCS(seq_a, seq_b, len_a, len_b)
		
		self.cOutput.setText(f"{LCS}")
		self.lengthOutput.setText(f"{length}")

	def clickHandler2(self):

		seq_a, len_a, seq_b, len_b = getLists2(self.seq_a2_input.toPlainText(), self.seq_b2_input.toPlainText())

		#findLCS is the main backend function; dynamic programming LCS alg
		LCS, length = findLCS(seq_a, seq_b, len_a, len_b)
		
		LCS_formatted = ""
		for string in LCS:
			LCS_formatted += string + '\n'

		self.LCS2_output.setPlainText(f"{LCS_formatted}")
		self.lengthOutput2.setText(f"{length}")



app = QApplication([])
window = Window()

window.show()
app.exec()