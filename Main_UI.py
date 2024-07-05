from User import user
import Validation
import sqlite3 as sql

# This class contains the main menu of the app, including the revenue, expence, category, search, report and setting pages as well as exit button.
class MainUI(Validation.QMainWindow, user, Validation.check_validation):
    default_type_combo = ['Cash', 'Cheque', 'Digital currency']
    months = {"January": '31', "February": '29', "March": '31',
              "April": '30', "May": '31', "June": '30',
              "July": '31', "August": '31', "September": '30',
              "October": '31', "November": '30', "December": '31'}
    category_combo = ['wage', 'saving', 'allowance']
    dark_mode = ["Lite", "Dark"]
    delete_information =["user", "transaction", "just revenue", "just expense"]
    
    def __init__(self):
        super().__init__()   
        self.rev_amount = ""
        self.rev_day = ""
        self.rev_month = ""
        self.rev_year = ""
        self.rev_source = ""
        self.rev_desc = ""
        self.rev_type = ""
        self.exp_amount = ""
        self.exp_day = ""
        self.exp_month = ""
        self.exp_year = ""
        self.exp_source = ""
        self.exp_desc = ""
        self.exp_type = ""
        self.searched_word = ""
        self.revenue_file = self.user_name + f"_revenue.db"
        self.expense_file = self.user_name + f"_expense.db"
        self.category_file = self.user_name + f"_category.db"
        self.Main_window()

    def Main_window(self):
        
        self.setGeometry(400, 100, 600, 300)
        self.mainWidget = Validation.QWidget(self)
        self.mainLayout = Validation.QHBoxLayout(self.mainWidget)

        self.leftWidget = Validation.QWidget(self)
        self.leftWidget.setStyleSheet("background-color: #FBE870;")
        self.leftLayout = Validation.QVBoxLayout(self.leftWidget)
        self.hlayout = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout1 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout2 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout3 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout4 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout5 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout6 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout7 = Validation.QHBoxLayout(self.leftWidget)

        self.leftLayout.addLayout(self.hlayout)
        self.leftLayout.addLayout(self.hlayout2)
        self.leftLayout.addLayout(self.hlayout3)
        self.leftLayout.addLayout(self.hlayout4)
        self.leftLayout.setContentsMargins(0, 60, 90, 250)
        self.line_main_style = """
        QLineEdit {
           background-color: #c9a8ce; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """
        self.mainLayout.addWidget(self.leftWidget, 80)  

        self.rightWidget = Validation.QWidget(self)
        self.rightWidget.setStyleSheet("background-color: #52afb6;")
        self.rightLayout = Validation.QVBoxLayout(self.rightWidget)
        self.btn_main_style ="""
       QPushButton {
          background-color: #C53151; 
          color: #76D7EA;
          border: 3px solid #0081AB;    
          border-radius: 10px;        
          padding: 4px;
        }
        QPushButton:hover {
            background-color: #B768A2; 
        }
        """
        self.combo_main_style ="""
        QComboBox {
          background-color: #FF4681; 
          color: #76D7EA;
          border: 3px solid #0081AB;    
          border-radius: 10px;        
          padding: 4px;         
        }
        QComboBox QAbstractItemView {
            background-color: skyblue;
            color: red 
        }
        """
        self.check_box_style ="""
        QCheckBox {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QCheckBox:hover {
            background-color: #0081AB;  
        }
        """
        
        self.view_style ="""
        QTextBrowser {
           background-color: #93CCEA;  
           color: red;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QTableView:hover {
            background-color: #0081AB;  
        }
        """
        
        self.timer_label = Validation.QLabel("Elapsed Time: 00:00:00", self)
        self.timer_label.setStyleSheet("background-color:#FBE870 ;  color : #ED0A3F ")
        self.timer_label.setFixedSize(200, 40)
        self.timer_label.setAlignment(Validation.Qt.AlignmentFlag.AlignCenter)
        self.start_time = Validation.QTime.currentTime()
        self.timer = Validation.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.rightLayout.addWidget(self.timer_label)

        self.btn_revenue = Validation.QPushButton("Revenue")
        self.btn_revenue.setStyleSheet(self.btn_main_style)
        self.btn_expense = Validation.QPushButton("Expense")
        self.btn_expense.setStyleSheet(self.btn_main_style)
        self.btn_category = Validation.QPushButton("Category")
        self.btn_category.setStyleSheet(self.btn_main_style)
        self.btn_search = Validation.QPushButton("Search")
        self.btn_search.setStyleSheet(self.btn_main_style)
        self.btn_report = Validation.QPushButton("Report")
        self.btn_report.setStyleSheet(self.btn_main_style)
        self.btn_settings = Validation.QPushButton("Setting")
        self.btn_settings.setStyleSheet(self.btn_main_style)
        self.btn_exit = Validation.QPushButton("Exit")
        self.btn_exit.setStyleSheet(self.btn_main_style)

        self.rightLayout.addWidget(self.btn_revenue)
        self.rightLayout.addWidget(self.btn_expense)
        self.rightLayout.addWidget(self.btn_category)
        self.rightLayout.addWidget(self.btn_search)
        self.rightLayout.addWidget(self.btn_report)
        self.rightLayout.addWidget(self.btn_settings)
        self.rightLayout.addWidget(self.btn_exit)
        self.mainLayout.addWidget(self.rightWidget, 20)  

        self.btn_revenue.clicked.connect(self.revenue)
        self.btn_expense.clicked.connect(self.expense)
        self.btn_category.clicked.connect(self.category)
        #self.btn_search.clicked.connect(self.search)
        #self.btn_report.clicked.connect(self.report)
        #self.btn_settings.clicked.connect(self.settings)
        #self.btn_exit.clicked.connect(self.exit)

        self.setCentralWidget(self.mainWidget)
        self.show()

        self.current_layout = None
        
    def update_timer(self):
        elapsed_time = Validation.QTime(0, 0).addSecs(self.start_time.secsTo(Validation.QTime.currentTime()))
        self.timer_label.setText(f"Elapsed Time: {elapsed_time.toString('hh:mm:ss')}")    

    def revenue(self):
        if self.current_layout == 'revenue':
            return
        self.current_layout = 'revenue'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.amount_of_revenue_line = Validation.QLineEdit()
        self.amount_of_revenue_label = Validation.QLabel()
        self.amount_of_revenue_label.setVisible(False)
        self.amount_of_revenue_label.setText("please enter a valid amount(just digits)!")
        self.amount_of_revenue_label.setStyleSheet('color: red')
        self.amount_of_revenue_line.setPlaceholderText("Amount Of Revenue")
        self.amount_of_revenue_line.setStyleSheet(self.line_main_style)
        self.day_of_revenue_line = Validation.QLineEdit()
        self.day_of_revenue_line.setPlaceholderText("Day")
        self.day_of_revenue_line.setStyleSheet(self.line_main_style)
        self.day_of_revenue_label = Validation.QLabel()
        self.day_of_revenue_label.setVisible(False)
        self.day_of_revenue_label.setText("please enter a valid day")
        self.day_of_revenue_label.setStyleSheet('color: red')
        self.month_of_revenue_line = Validation.QLineEdit()
        self.month_of_revenue_line.setPlaceholderText("Month")
        self.month_of_revenue_line.setStyleSheet(self.line_main_style)
        self.month_of_revenue_label = Validation.QLabel()
        self.month_of_revenue_label.setVisible(False)
        self.month_of_revenue_label.setText("please enter a valid mont(just letters)!")
        self.month_of_revenue_label.setStyleSheet('color: red')
        self.year_of_revenue_line = Validation.QLineEdit()
        self.year_of_revenue_line.setPlaceholderText("Year")
        self.year_of_revenue_line.setStyleSheet(self.line_main_style)
        self.year_of_revenue_label = Validation.QLabel()
        self.year_of_revenue_label.setVisible(False)
        self.year_of_revenue_label.setText("please enter a valid year")
        self.year_of_revenue_label.setStyleSheet('color: red')
        self.source_of_revenue_line = Validation.QLineEdit()
        self.source_of_revenue_line.setPlaceholderText("Source Of Revenue")
        self.source_of_revenue_line.setStyleSheet(self.line_main_style)
        self.source_of_revenue_label = Validation.QLabel()
        self.source_of_revenue_label.setVisible(False)
        self.source_of_revenue_label.setText("please fill the gap!")
        self.source_of_revenue_label.setStyleSheet('color: red')
        self.close_rev_file_label = Validation.QLabel()
        self.close_rev_file_label.setText("please close the revenue file first!")
        self.close_rev_file_label.setStyleSheet('color: red')
        self.close_rev_file_label.setVisible(False)
        self.source_of_revenue_combo_box = Validation.QComboBox()
        self.source_of_revenue_combo_box.setStyleSheet(self.combo_main_style)

        self.add_item_category_combo()

        self.description_revenue_line = Validation.QLineEdit()
        self.description_revenue_line.setPlaceholderText("Description Of Revenue")
        self.description_revenue_line.setStyleSheet(self.line_main_style)
        self.desc_of_revenue_label = Validation.QLabel()
        self.desc_of_revenue_label.setText('please enter a sentence with less than equal 100 characters!')
        self.desc_of_revenue_label.setStyleSheet('color: red')
        self.desc_of_revenue_label.setVisible(False)
        self.type_of_revenue_line = Validation.QLineEdit()
        self.type_of_revenue_line.setPlaceholderText("Type Of Revenue")
        self.type_of_revenue_line.setStyleSheet(self.line_main_style)
        self.type_of_revenue_line.setReadOnly(True)
        self.type_of_revenue_label = Validation.QLabel()
        self.type_of_revenue_label.setVisible(False)
        self.type_of_revenue_label.setText("please fill the gap!")
        self.type_of_revenue_label.setStyleSheet('color: red')

        self.type_of_revenue_combo_box = Validation.QComboBox()
        self.type_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.year_of_revenue_combo_box = Validation.QComboBox()
        self.year_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_revenue_combo_box = Validation.QComboBox()
        self.month_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_revenue_combo_box = Validation.QComboBox()
        self.day_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.btn_sub_revenue = Validation.QPushButton("Submit")
        self.btn_sub_revenue.setStyleSheet(self.btn_main_style)
        
        self.leftLayout.addWidget(self.amount_of_revenue_label)
        self.leftLayout.addWidget(self.amount_of_revenue_line)
        self.leftLayout.addLayout(self.hlayout1)
        self.hlayout1.addWidget(self.year_of_revenue_label)
        self.hlayout1.addWidget(self.month_of_revenue_label)
        self.hlayout1.addWidget(self.day_of_revenue_label)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.year_of_revenue_line)
        self.hlayout.addWidget(self.month_of_revenue_line)
        self.hlayout.addWidget(self.day_of_revenue_line)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.year_of_revenue_combo_box)
        self.hlayout2.addWidget(self.month_of_revenue_combo_box)
        self.hlayout2.addWidget(self.day_of_revenue_combo_box)

        for i in range(1, 32):
            self.day_of_revenue_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_revenue_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_revenue_combo_box.addItem(f"{i}")

        self.year_of_revenue_combo_box.activated[int].connect(self.set_year_revenue_line)
        self.month_of_revenue_combo_box.activated[int].connect(self.set_month_revenue_line)
        self.day_of_revenue_combo_box.activated[int].connect(self.set_day_revenue_line)

        self.source_of_revenue_combo_box.activated[int].connect(self.set_source_line)
        
        self.leftLayout.addWidget(self.source_of_revenue_label)
        self.leftLayout.addWidget(self.source_of_revenue_line)
        self.leftLayout.addWidget(self.source_of_revenue_combo_box)
        self.leftLayout.addWidget(self.desc_of_revenue_label)
        self.leftLayout.addWidget(self.description_revenue_line)
        self.leftLayout.addWidget(self.type_of_revenue_label)
        self.leftLayout.addWidget(self.type_of_revenue_line)
        self.leftLayout.addWidget(self.type_of_revenue_combo_box)
        self.leftLayout.addWidget(self.btn_sub_revenue)
        self.leftLayout.addWidget(self.close_rev_file_label)

        self.type_of_revenue_combo_box.addItems(self.default_type_combo)
        self.type_of_revenue_line.textChanged.connect(self.update_type_combo_box)
        self.source_of_revenue_combo_box.addItems(self.category_combo)

        self.type_of_revenue_combo_box.activated[int].connect(self.set_revenue_line)
        
        #self.btn_sub_revenue.clicked.connect(self.take_rev)
        
    def set_rev_attr(self):
        self.rev_amount = self.amount_of_revenue_line.text()
        self.rev_day = self.day_of_revenue_line.text()
        self.rev_month = self.month_of_revenue_line.text()
        self.rev_year = self.year_of_revenue_line.text()
        self.rev_source = self.source_of_revenue_line.text()
        self.rev_desc = self.description_revenue_line.text()
        self.rev_type = self.type_of_revenue_line.text()  
        
    def take_rev(self):
        rev_amount = self.amount_of_revenue_line.text()
        rev_day = self.day_of_revenue_line.text()
        rev_month = self.month_of_revenue_line.text()
        rev_year = self.year_of_revenue_line.text()
        rev_source = self.source_of_revenue_line.text()
        rev_desc = self.description_revenue_line.text()
        rev_type = self.type_of_revenue_line.text()
         
        rev_amount_val = self.digit_val(rev_amount)
        rev_day_val = self.day_val(rev_day, rev_month)
        rev_month_val = self.mounth_val(rev_month)
        rev_year_val = self.revexp_year_val(rev_year)
        if rev_source != "":
            rev_source_val = True
        else:
            rev_source_val = False
        if len(rev_desc) <= 100 :        
            rev_desc_val = True
        else :
            rev_desc_val = False 
        if rev_type != "":    
            rev_type_val = True
        else :
             rev_type_val = False   
         
        rev_val_list = [rev_amount_val, rev_day_val, rev_month_val, 
                        rev_year_val, rev_source_val, rev_desc_val, rev_type_val]
         
        if False in rev_val_list:
            if not rev_val_list[0]:
                if not self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(True)
            else:
                if self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(False)       
            if not rev_val_list[1]:
                if not self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(True)
            else:
                if self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(False) 
            if not rev_val_list[2]:
                if not self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(True)
            else:
                if self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(False) 
            if not rev_val_list[3]:
                if not self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(True)
            else:
                if self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(False) 
            if not rev_val_list[4]:
                if not self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(True)
            else:
                if self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(False) 
            if not rev_val_list[5]:
                if not self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(True)
            else:
                if self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(False) 
            if not rev_val_list[6]:
                if not self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(True)
            else:
                if self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(False)        
        else:
            if self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(False)
            if self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(False) 
            if self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(False)                 
            if self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(False)   
            if self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(False) 
            if self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(False)   
            if self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(False)
            self.set_rev_attr()
            self.create_user_revenue_databse()  
            
    def expense(self):
        if self.current_layout == 'expense':
            return
        self.current_layout = 'expense'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.amount_of_expense_line = Validation.QLineEdit()
        self.amount_of_expense_line.setPlaceholderText("Amount Of Expense")
        self.amount_of_expense_line.setStyleSheet(self.line_main_style)
        self.amount_of_expense_label = Validation.QLabel()
        self.amount_of_expense_label.setVisible(False)
        self.amount_of_expense_label.setText("please enter a valid amount(just digits)!")
        self.amount_of_expense_label.setStyleSheet('color: red')
        self.day_of_expense_line = Validation.QLineEdit()
        self.day_of_expense_line.setPlaceholderText("Day")
        self.day_of_expense_line.setStyleSheet(self.line_main_style)
        self.day_of_expense_label = Validation.QLabel()
        self.day_of_expense_label.setVisible(False)
        self.day_of_expense_label.setText("please enter a valid day!")
        self.day_of_expense_label.setStyleSheet('color: red')
        self.month_of_expense_line = Validation.QLineEdit()
        self.month_of_expense_line.setPlaceholderText("Month")
        self.month_of_expense_line.setStyleSheet(self.line_main_style)
        self.month_of_expense_label = Validation.QLabel()
        self.month_of_expense_label.setVisible(False)
        self.month_of_expense_label.setText("please enter a valid month(just letters)!")
        self.month_of_expense_label.setStyleSheet('color: red')
        self.year_of_expense_line = Validation.QLineEdit()
        self.year_of_expense_line.setPlaceholderText("Year")
        self.year_of_expense_line.setStyleSheet(self.line_main_style)
        self.year_of_expense_label = QLabel()
        self.year_of_expense_label.setVisible(False)
        self.year_of_expense_label.setText("please enter a valid year!")
        self.year_of_expense_label.setStyleSheet('color: red')
        self.source_of_expense_line = Validation.QLineEdit()
        self.source_of_expense_line.setPlaceholderText("Source Of Expense")
        self.source_of_expense_line.setStyleSheet(self.line_main_style)
        self.source_of_expense_label = Validation.QLabel()
        self.source_of_expense_label.setVisible(False)
        self.source_of_expense_label.setText("please fill the gap!")
        self.source_of_expense_label.setStyleSheet('color: red')
        self.description_expense_line = Validation.QLineEdit()
        self.description_expense_line.setPlaceholderText("Description Of Expense")
        self.description_expense_line.setStyleSheet(self.line_main_style)
        self.desc_of_expense_label = Validation.QLabel()
        self.desc_of_expense_label.setText('please enter a sentence with less than equal 100 characters!')
        self.desc_of_expense_label.setStyleSheet('color: red')
        self.desc_of_expense_label.setVisible(False)
        self.type_of_expense_line = Validation.QLineEdit()
        self.type_of_expense_line.setPlaceholderText("Type Of Expense")
        self.type_of_expense_line.setStyleSheet(self.line_main_style)
        self.type_of_expense_line.setReadOnly(True)
        self.type_of_expense_label = Validation.QLabel()
        self.type_of_expense_label.setVisible(False)
        self.type_of_expense_label.setText("please fill the gap!")
        self.type_of_expense_label.setStyleSheet('color: red')

        self.type_of_expense_combo_box = Validation.QComboBox()
        self.type_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.year_of_expense_combo_box = Validation.QComboBox()
        self.year_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_expense_combo_box = Validation.QComboBox()
        self.month_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_expense_combo_box = Validation.QComboBox()
        self.day_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.btn_sub_expense = Validation.QPushButton("Submit")
        self.btn_sub_expense.setStyleSheet(self.btn_main_style)
        
        self.leftLayout.addWidget(self.amount_of_expense_label)
        self.leftLayout.addWidget(self.amount_of_expense_line)
        self.leftLayout.addLayout(self.hlayout1)
        self.hlayout1.addWidget(self.year_of_expense_label)
        self.hlayout1.addWidget(self.month_of_expense_label)
        self.hlayout1.addWidget(self.day_of_expense_label)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.year_of_expense_line)
        self.hlayout.addWidget(self.month_of_expense_line)
        self.hlayout.addWidget(self.day_of_expense_line)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.year_of_expense_combo_box)
        self.hlayout2.addWidget(self.month_of_expense_combo_box)
        self.hlayout2.addWidget(self.day_of_expense_combo_box)

        for i in range(1, 32):
            self.day_of_expense_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_expense_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_expense_combo_box.addItem(f"{i}")

        self.year_of_expense_combo_box.activated[int].connect(self.set_year_expense_line)
        self.month_of_expense_combo_box.activated[int].connect(self.set_month_expense_line)
        self.day_of_expense_combo_box.activated[int].connect(self.set_day_expense_line)
        
        self.leftLayout.addWidget(self.source_of_expense_label)
        self.leftLayout.addWidget(self.source_of_expense_line)
        self.leftLayout.addWidget(self.desc_of_expense_label)
        self.leftLayout.addWidget(self.description_expense_line)
        self.leftLayout.addWidget(self.type_of_expense_label)
        self.leftLayout.addWidget(self.type_of_expense_line)
        self.leftLayout.addWidget(self.type_of_expense_combo_box)
        self.leftLayout.addWidget(self.btn_sub_expense)
        
        self.close_exp_file_label = Validation.QLabel()
        self.close_exp_file_label.setText("please close the exp_file first!")
        self.close_exp_file_label.setVisible(False)
        self.close_exp_file_label.setStyleSheet('color: red')

        self.type_of_expense_combo_box.addItems(self.default_type_combo)
        self.type_of_expense_line.textChanged.connect(self.update_combo_box_expense)
        self.type_of_expense_combo_box.activated[int].connect(self.set_expense_line)
        
        self.btn_sub_expense.clicked.connect(self.take_exp)             
        
    def set_exp_attr(self):
        self.exp_amount = self.amount_of_expense_line.text()
        self.exp_day = self.day_of_expense_line.text()
        self.exp_month = self.month_of_expense_line.text()
        self.exp_year = self.year_of_expense_line.text()
        self.exp_source = self.source_of_expense_line.text()
        self.exp_desc = self.description_expense_line.text()
        self.exp_type = self.type_of_expense_line.text()     
        
    def take_exp(self):
        exp_amount = self.amount_of_expense_line.text()
        exp_day = self.day_of_expense_line.text()
        exp_month = self.month_of_expense_line.text()
        exp_year = self.year_of_expense_line.text()
        exp_source = self.source_of_expense_line.text()
        exp_desc = self.description_expense_line.text()
        exp_type = self.type_of_expense_line.text()
         
        exp_amount_val = self.digit_val(exp_amount)
        exp_day_val = self.day_val(exp_day, exp_month)
        exp_month_val = self.mounth_val(exp_month)
        exp_year_val = self.revexp_year_val(exp_year)
        if exp_source != "" :
            exp_source_val = True
        else :
            exp_source_val = False
        if len(exp_desc) <= 100 :        
            exp_desc_val = True
        else :
            exp_desc_val = False 
        if exp_type != "" :    
            exp_type_val = True
        else :
             exp_type_val = False
         
        exp_val_list = [exp_amount_val, exp_day_val, exp_month_val, 
                        exp_year_val, exp_source_val, exp_desc_val, exp_type_val]
         
        if False in exp_val_list :
            if not exp_val_list[0] :
                if not self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(True)
            else :
                if self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(False)       
            if not exp_val_list[1] :
                if not self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(True)
            else :
                if self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(False) 
            if not exp_val_list[2] :
                if not self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(True)
            else :
                if self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(False) 
            if not exp_val_list[3] :
                if not self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(True)
            else :
                if self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(False) 
            if not exp_val_list[4] :
                if not self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(True)
            else :
                if self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(False) 
            if not exp_val_list[5] :
                if not self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(True)
            else :
                if self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(False) 
            if not exp_val_list[6] :
                if not self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(True)
            else :
                if self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(False) 
        else :
            if self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(False)
            if self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(False) 
            if self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(False)                 
            if self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(False)   
            if self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(False) 
            if self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(False)   
            if self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(False)                           
            self.set_exp_attr()
            #self.create_user_expense_file()  
            
    def category(self):
        if self.current_layout == 'category':
            return
        self.current_layout = 'category'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.add_category_line = Validation.QLineEdit()
        self.add_category_line.setPlaceholderText("Category")
        self.add_category_line.setStyleSheet(self.line_main_style)
        self.add_btn = Validation.QPushButton("Add")
        self.add_btn.setStyleSheet(self.btn_main_style)
        self.category_label = Validation.QLabel("The category added before")
        self.category_label.setStyleSheet("color : red")
        self.category_label_err = Validation.QLabel("please close the file and try again")
        self.category_label_err.setStyleSheet("color : red")
        #self.category_label_err.setVisible(True)


        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.add_category_line)
        self.hlayout.addWidget(self.add_btn)
        self.leftLayout.addWidget(self.category_label)
        self.leftLayout.addWidget(self.category_label_err)
        self.category_label.hide()
        self.category_label_err.hide()

        #self.add_btn.clicked.connect(self.add_text_to_excel)
        #self.df = pd.DataFrame(columns = ['Category'])        
            
    def search(self):
        if self.current_layout == 'search':
            return
        self.current_layout = 'search'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.leftLayout.addLayout(self.hlayout)
        self.search_line = Validation.QLineEdit()
        self.search_line.setStyleSheet(self.line_main_style)
        self.search_line.setPlaceholderText("Search")
        self.btn_searching = Validation.QPushButton("Searching")
        self.btn_searching.setStyleSheet(self.btn_main_style)
        self.day_revenue_check = Validation.QCheckBox("day_revenue")
        self.day_revenue_check.setStyleSheet(self.check_box_style)
        self.day_expense_check = Validation.QCheckBox("day_expense")
        self.day_expense_check.setStyleSheet(self.check_box_style)
        self.month_revenue_check = Validation.QCheckBox("month_revenue")
        self.month_revenue_check.setStyleSheet(self.check_box_style)
        self.month_expense_check = Validation.QCheckBox("month_expense")
        self.month_expense_check.setStyleSheet(self.check_box_style)
        self.year_revenue_check = Validation.QCheckBox("year_revenue")
        self.year_revenue_check.setStyleSheet(self.check_box_style)
        self.year_expense_check = Validation.QCheckBox("year_expense")
        self.year_expense_check.setStyleSheet(self.check_box_style)
        self.value_0_100_dollar_check = Validation.QCheckBox("0 - 100 $")
        self.value_0_100_dollar_check.setStyleSheet(self.check_box_style)
        self.value_100_1000_dollar_check = Validation.QCheckBox("100 - 1000 $")
        self.value_100_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.value_more_than_1000_dollar_check = Validation.QCheckBox("More Than 1000 $")
        self.value_more_than_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.wage_check = Validation.QCheckBox("Wage")
        self.wage_check.setStyleSheet(self.check_box_style)
        self.type_revenue_check = Validation.QCheckBox("Type Revenue")
        self.type_revenue_check.setStyleSheet(self.check_box_style)
        self.type_expense_check = Validation.QCheckBox("Type Expensee")
        self.type_expense_check.setStyleSheet(self.check_box_style)
        self.source_revenue_check = Validation.QCheckBox("Source Revenue")
        self.source_revenue_check.setStyleSheet(self.check_box_style)
        self.source_expense_check = Validation.QCheckBox("Source Expense")
        self.source_expense_check.setStyleSheet(self.check_box_style)
        self.revenue_desc_check = Validation.QCheckBox("revenue_description")
        self.revenue_desc_check.setStyleSheet(self.check_box_style)
        self.expense_desc_check = Validation.QCheckBox("expense_description")
        self.expense_desc_check.setStyleSheet(self.check_box_style)
        self.revenue_check = Validation.QCheckBox("revenue")
        self.revenue_check.setStyleSheet(self.check_box_style)
        self.expense_check = Validation.QCheckBox("expense")
        self.expense_check.setStyleSheet(self.check_box_style)
        
        self.hlayout.addWidget(self.search_line)
        self.hlayout.addWidget(self.btn_searching)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.day_revenue_check)
        self.hlayout2.addWidget(self.month_revenue_check)
        self.hlayout2.addWidget(self.year_revenue_check)
        self.hlayout2.addWidget(self.value_0_100_dollar_check)
        self.hlayout2.addWidget(self.value_100_1000_dollar_check)
        self.hlayout2.addWidget(self.value_more_than_1000_dollar_check)
        self.leftLayout.addLayout(self.hlayout3)
        self.hlayout3.addWidget(self.day_expense_check)
        self.hlayout3.addWidget(self.month_expense_check)
        self.hlayout3.addWidget(self.year_expense_check)
        self.hlayout3.addWidget(self.type_expense_check)
        self.hlayout3.addWidget(self.source_expense_check)
        self.leftLayout.addLayout(self.hlayout4)
        self.hlayout4.addWidget(self.type_revenue_check)
        self.hlayout4.addWidget(self.source_revenue_check)
        self.hlayout4.addWidget(self.revenue_check)
        self.hlayout4.addWidget(self.revenue_desc_check)
        self.hlayout4.addWidget(self.expense_check )
        self.hlayout4.addWidget(self.expense_desc_check)
        self.search_view = Validation.QTextBrowser()
        self.leftLayout.addWidget(self.search_view)
        self.search_view.setStyleSheet(self.view_style)
        #self.btn_searching.clicked.connect(self.search_logic)          
        
    def report(self):
        if self.current_layout == 'report':
            return
        self.current_layout = 'report'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.year_of_report_combo_box = Validation.QComboBox()
        self.year_of_report_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_report_combo_box = Validation.QComboBox()
        self.month_of_report_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_report_combo_box = Validation.QComboBox()
        self.day_of_report_combo_box.setStyleSheet(self.combo_main_style)

        self.year_of_report_combo_box2 = Validation.QComboBox()
        self.year_of_report_combo_box2.setStyleSheet(self.combo_main_style)
        self.month_of_report_combo_box2 = Validation.QComboBox()
        self.month_of_report_combo_box2.setStyleSheet(self.combo_main_style)
        self.day_of_report_combo_box2 = Validation.QComboBox()
        self.day_of_report_combo_box2.setStyleSheet(self.combo_main_style)

        for i in range(1, 32):
            self.day_of_report_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_report_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_report_combo_box.addItem(f"{i}")

        for i in range(1, 32):
            self.day_of_report_combo_box2.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_report_combo_box2.addItem(month)

        for i in range(1930, 2051):
            self.year_of_report_combo_box2.addItem(f"{i}")

        self.year_of_report_combo_box.activated[int].connect(self.set_year_report_line)
        self.month_of_report_combo_box.activated[int].connect(self.set_month_report_line)
        self.day_of_report_combo_box.activated[int].connect(self.set_day_report_line)

        self.year_of_report_combo_box2.activated[int].connect(self.set_year_report_line2)
        self.month_of_report_combo_box2.activated[int].connect(self.set_month_report_line2)
        self.day_of_report_combo_box2.activated[int].connect(self.set_day_report_line2)

        self.from_report_line = Validation.QLineEdit()
        self.from_report_line.setText("From")
        self.from_report_line.setStyleSheet("""
        QLineEdit {
           background-color: #AD4379; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """)
        self.from_report_line.setReadOnly(True)
        self.day_of_report_line = Validation.QLineEdit()
        self.day_of_report_line.setPlaceholderText("Day")
        self.day_of_report_line.setStyleSheet(self.line_main_style)
        self.month_of_report_line = Validation.QLineEdit()
        self.month_of_report_line.setPlaceholderText("Month")
        self.month_of_report_line.setStyleSheet(self.line_main_style)
        self.year_of_report_line = Validation.QLineEdit()
        self.year_of_report_line.setPlaceholderText("Year")
        self.year_of_report_line.setStyleSheet(self.line_main_style)

        self.until_report_line = Validation.QLineEdit()
        self.until_report_line.setText("Until")
        self.until_report_line.setStyleSheet("""
        QLineEdit {
           background-color: #AD4379; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """)
        self.until_report_line.setReadOnly(True)
        self.day_of_report_line2 = Validation.QLineEdit()
        self.day_of_report_line2.setPlaceholderText("Day")
        self.day_of_report_line2.setStyleSheet(self.line_main_style)
        self.month_of_report_line2 = Validation.QLineEdit()
        self.month_of_report_line2.setPlaceholderText("Month")
        self.month_of_report_line2.setStyleSheet(self.line_main_style)
        self.year_of_report_line2 = Validation.QLineEdit()
        self.year_of_report_line2.setPlaceholderText("Year")
        self.year_of_report_line2.setStyleSheet(self.line_main_style)

        self.day_report_check = Validation.QCheckBox("day_report")
        self.day_report_check.setStyleSheet(self.check_box_style)
        self.month_report_check = Validation.QCheckBox("month_report")
        self.month_report_check.setStyleSheet(self.check_box_style)
        self.year_report_check = Validation.QCheckBox("year_report")
        self.year_report_check.setStyleSheet(self.check_box_style)
        self.report_0_100_dollar_check = Validation.QCheckBox("0 - 100 $")
        self.report_0_100_dollar_check.setStyleSheet(self.check_box_style)
        self.report_100_1000_dollar_check = Validation.QCheckBox("100 - 1000 $")
        self.report_100_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.report_more_than_1000_dollar_check = Validation.QCheckBox("More Than 1000 $")
        self.report_more_than_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.cash_check = Validation.QCheckBox("Cash")
        self.cash_check.setStyleSheet(self.check_box_style)
        self.cheque_check = Validation.QCheckBox("Cheque")
        self.cheque_check.setStyleSheet(self.check_box_style)
        self.digital_check = Validation.QCheckBox("digital_currency")
        self.digital_check.setStyleSheet(self.check_box_style)
        self.saving_check = Validation.QCheckBox("Saving")
        self.saving_check.setStyleSheet(self.check_box_style)
        self.wage_check = Validation.QCheckBox("wage")
        self.wage_check.setStyleSheet(self.check_box_style)
        self.report_revenue_check = Validation.QCheckBox("Revenue")
        self.report_revenue_check.setStyleSheet(self.check_box_style)
        self.report_expense_check = Validation.QCheckBox("Expense")
        self.report_expense_check.setStyleSheet(self.check_box_style)
        self.btn_report = Validation.QPushButton("Report")
        self.btn_report.setStyleSheet(self.btn_main_style)
    
        self.leftLayout.addWidget(self.from_report_line)

        self.leftLayout.addLayout(self.hlayout4)
        
        self.hlayout4.addWidget(self.day_of_report_line)
        self.hlayout4.addWidget(self.month_of_report_line)
        self.hlayout4.addWidget(self.year_of_report_line)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.day_of_report_combo_box)
        self.hlayout.addWidget(self.month_of_report_combo_box)
        self.hlayout.addWidget(self.year_of_report_combo_box)

        self.leftLayout.addWidget(self.until_report_line)
        self.leftLayout.addLayout(self.hlayout5)
        self.hlayout5.addWidget(self.day_of_report_line2)
        self.hlayout5.addWidget(self.month_of_report_line2)
        self.hlayout5.addWidget(self.year_of_report_line2)
        self.leftLayout.addLayout(self.hlayout6)
        self.hlayout6.addWidget(self.day_of_report_combo_box2)
        self.hlayout6.addWidget(self.month_of_report_combo_box2)
        self.hlayout6.addWidget(self.year_of_report_combo_box2)

        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.day_report_check)
        self.hlayout2.addWidget(self.month_report_check)
        self.hlayout2.addWidget(self.year_report_check)
        self.hlayout2.addWidget(self.report_0_100_dollar_check)
        self.hlayout2.addWidget(self.report_100_1000_dollar_check)
        self.hlayout2.addWidget(self.report_more_than_1000_dollar_check)
        self.leftLayout.addLayout(self.hlayout3)
        self.hlayout3.addWidget(self.cash_check)
        self.hlayout3.addWidget(self.cheque_check)
        self.hlayout3.addWidget(self.digital_check)
        self.hlayout3.addWidget(self.wage_check)
        self.hlayout3.addWidget(self.saving_check)
        self.hlayout3.addWidget(self.report_revenue_check)
        self.hlayout3.addWidget(self.report_expense_check)
        self.leftLayout.addWidget(self.btn_report)
        self.report_view = Validation.QTextBrowser()
        self.leftLayout.addWidget(self.report_view)
        self.report_view.setStyleSheet(self.view_style)
        
        #self.btn_report.clicked.connect(self.report_logic) 
        
    def settings(self):
        if self.current_layout == 'settings':
            return
        self.current_layout = 'settings'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)

        self.first_name_line_edit2 = Validation.QLineEdit()
        self.first_name_line_edit2.setPlaceholderText("firs name")
        self.first_name_line_edit2.setStyleSheet(self.line_main_style)
        self.last_name_line_edit2 = Validation.QLineEdit()
        self.last_name_line_edit2.setPlaceholderText('last name')
        self.last_name_line_edit2.setStyleSheet(self.line_main_style)
        self.password_line_edit2 = Validation.QLineEdit()
        self.password_line_edit2.setPlaceholderText('password')
        self.password_line_edit2.setStyleSheet(self.line_main_style)
        self.password_line_edit2.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeat_password_line_edit2 = Validation.QLineEdit()
        self.repeat_password_line_edit2.setPlaceholderText('repeat password')
        self.repeat_password_line_edit2.setStyleSheet(self.line_main_style)
        self.repeat_password_line_edit2.setEchoMode(QLineEdit.EchoMode.Password)
        self.email_line_edit2 = Validation.QLineEdit()
        self.email_line_edit2.setPlaceholderText('email')
        self.email_line_edit2.setStyleSheet(self.line_main_style)
        self.phone_number_line_edit2 = Validation.QLineEdit()
        self.phone_number_line_edit2.setPlaceholderText('phone')
        self.phone_number_line_edit2.setStyleSheet(self.line_main_style)
        self.city_line_edit2 = Validation.QLineEdit()
        self.city_line_edit2.setPlaceholderText('city')
        self.city_line_edit2.setStyleSheet(self.line_main_style)
        self.day_line_edit2 = Validation.QLineEdit()
        self.day_line_edit2.setStyleSheet(self.line_main_style)
        self.day_line_edit2.setPlaceholderText('day')
        self.mounth_line_edit2 = Validation.QLineEdit()
        self.mounth_line_edit2.setStyleSheet(self.line_main_style)
        self.mounth_line_edit2.setPlaceholderText('month ***please enter letters***')
        self.year_line_edit2 = Validation.QLineEdit()
        self.year_line_edit2.setStyleSheet(self.line_main_style)
        self.year_line_edit2.setPlaceholderText('year')

        self.label_image = Validation.QLabel()
        self.label_image.setFixedSize(200, 100)
        self.label_image.setScaledContents(True)
        self.add_image_btn = Validation.QPushButton("Add Image")
        self.add_image_btn.setStyleSheet(self.btn_main_style)
        self.leftLayout.addWidget(self.add_image_btn)
        #self.add_image_btn.clicked.connect(self.upload_image)
        self.leftLayout.addWidget(self.label_image)

        self.leftLayout.addLayout(self.hlayout5)
        self.err_lab_firstname = Validation.QLabel("NAME ERROR")
        self.err_lab_firstname.setStyleSheet("color : red")
        self.err_lab_firstname.hide()
        self.hlayout5.addWidget(self.err_lab_firstname)
        self.err_lab_lastname = Validation.QLabel("NAME ERROR")
        self.err_lab_lastname.setStyleSheet("color : red")
        self.err_lab_lastname.hide()
        self.hlayout5.addWidget(self.err_lab_lastname)
        self.err_lab_password = Validation.QLabel("PASSWORD ERROR")
        self.err_lab_password.setStyleSheet("color : red")
        self.err_lab_password.hide()
        self.hlayout5.addWidget(self.err_lab_password)

        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.first_name_line_edit2)
        self.hlayout.addWidget(self.last_name_line_edit2)
        self.hlayout.addWidget(self.password_line_edit2)

        self.leftLayout.addLayout(self.hlayout6)
        self.err_lab_repassword = Validation.QLabel("PASSWORD ERROR")
        self.err_lab_repassword.setStyleSheet("color : red")
        self.err_lab_repassword.hide()
        self.hlayout6.addWidget(self.err_lab_repassword)
        self.err_lab_email = Validation.QLabel("EMAIL ERROR")
        self.err_lab_email.setStyleSheet("color : red")
        self.err_lab_email.hide()
        self.hlayout6.addWidget(self.err_lab_email)
        self.err_lab_phone = Validation.QLabel("PHONE ERROR")
        self.err_lab_phone.setStyleSheet("color : red")
        self.err_lab_phone.hide()
        self.hlayout6.addWidget(self.err_lab_phone)
        self.err_lab_city = Validation.QLabel("please fill the gap!")
        self.err_lab_city.setStyleSheet("color : red")
        self.err_lab_city.hide()

        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.repeat_password_line_edit2)
        self.hlayout2.addWidget(self.email_line_edit2)
        self.hlayout2.addWidget(self.phone_number_line_edit2)
        self.leftLayout.addWidget(self.err_lab_city)
        self.leftLayout.addWidget(self.city_line_edit2)

        self.leftLayout.addLayout(self.hlayout7)
        self.err_lab_day = Validation.QLabel("DAY ERROR")
        self.err_lab_day.setStyleSheet("color : red")
        self.err_lab_day.hide()
        self.hlayout7.addWidget(self.err_lab_day)
        self.err_lab_month = Validation.QLabel("NAME ERROR")
        self.err_lab_month.setStyleSheet("color : red")
        self.err_lab_month.hide()
        self.hlayout7.addWidget(self.err_lab_month)
        self.err_lab_year = Validation.QLabel("NAME ERROR")
        self.err_lab_year.setStyleSheet("color : red")
        self.err_lab_year.hide()
        self.hlayout7.addWidget(self.err_lab_year)
        self.leftLayout.addLayout(self.hlayout4)
        self.hlayout4.addWidget(self.day_line_edit2)
        self.hlayout4.addWidget(self.mounth_line_edit2)
        self.hlayout4.addWidget(self.year_line_edit2)

        self.leftLayout.addLayout(self.hlayout3)
        self.year_of_edit_combo_box = Validation.QComboBox()
        self.year_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_edit_combo_box = Validation.QComboBox()
        self.month_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_edit_combo_box = Validation.QComboBox()
        self.day_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        for i in range(1, 32):
            self.day_of_edit_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_edit_combo_box.addItem(month)

        for i in range(1920, 2006):
            self.year_of_edit_combo_box.addItem(f"{i}")

        self.year_of_edit_combo_box.activated[int].connect(self.set_year_edit_line)
        self.month_of_edit_combo_box.activated[int].connect(self.set_month_edit_line)
        self.day_of_edit_combo_box.activated[int].connect(self.set_day_edit_line)

        self.hlayout3.addWidget(self.day_of_edit_combo_box)
        self.hlayout3.addWidget(self.month_of_edit_combo_box)
        self.hlayout3.addWidget(self.year_of_edit_combo_box)

        self.change_info_btn = Validation.QPushButton("Change")
        self.change_info_btn.setStyleSheet(self.btn_main_style)
        self.leftLayout.addWidget(self.change_info_btn)

        self.Dark_mode = Validation.QComboBox()
        self.Dark_mode.setStyleSheet(self.combo_main_style)
        self.Dark_mode.addItems(self.dark_mode)
        self.leftLayout.addWidget(self.Dark_mode)
        self.Dark_mode.currentTextChanged.connect(self.dark_lite_mode)
        
        self.delete_err = Validation.QLabel("please fill the gap!")
        self.delete_err.setVisible(False)
        self.delete_err.setStyleSheet("color: red")
        self.leftLayout.addWidget(self.delete_err)
        self.delete_info_line = Validation.QLineEdit()
        self.delete_info_line.setPlaceholderText("Delete the ...")
        self.delete_info_line.setStyleSheet(self.line_main_style)
        self.delete_info_line.setReadOnly(True)
        self.leftLayout.addWidget(self.delete_info_line)

        self.delete_info_combo = Validation.QComboBox()
        self.delete_info_combo.setStyleSheet(self.combo_main_style)
        self.delete_info_combo.addItems(self.delete_information)
        self.delete_info_combo.activated[int].connect(self.set_delete_line)
        self.leftLayout.addWidget(self.delete_info_combo)

        self.delete_user = Validation.QPushButton("Delete")
        self.delete_user.setStyleSheet(self.btn_main_style)
        self.leftLayout.addWidget(self.delete_user)
        
        #self.change_info_btn.clicked.connect(self.change_information)
        #self.delete_user.clicked.connect(self.Delete_User)
        
    def create_user_revenue_databse(self): 
        conn =  sql.connect(self.revenue_file)   
        cursor = conn.cursor()
        
        create_query = '''CREATE TABLE IF NOT EXISTS REVENUE (amount INT NOT NULL, source TEXT NOT NULL,
                          description TEXT, type TEXT , year INT, month TEXT, day INT)
                          VALUE (?, ?, ?, ?, ?, ?, ?)'''
        
        try:       
            rev_info = [self.rev_amount, self.rev_source, self.rev_desc, 
                        self.rev_type, self.rev_year, self.rev_month, self.rev_day] 
            cursor.execute(create_query, rev_info)
            conn.commit()
        except:
            if not self.close_rev_file_label.isVisible():
                self.close_rev_file_label.setVisible(True)     
        try :
            if self.close_rev_file_label.isVisible():
                self.close_rev_file_label.setVisible(False)
        except:
            if not self.close_rev_file_label.isVisible():
                self.close_rev_file_label.setVisible(True) 
                
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  
                
    def set_day_report_line2(self, index):
        day = self.day_of_report_combo_box2.itemText(index)
        self.day_of_report_line2.setText(day)

    def set_expense_line(self, index):
        expense_type = self.type_of_expense_combo_box.itemText(index)
        self.type_of_expense_line.setText(expense_type)

    def update_combo_box_expense(self):
        text = self.type_of_expense_line.text()
        if text and self.type_of_expense_combo_box.findText(text) == -1:
            self.type_of_expense_combo_box.addItems(text)                                          