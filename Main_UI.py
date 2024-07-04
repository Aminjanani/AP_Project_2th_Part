from User import user
import Validation

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
        self.revenue_file = ""
        self.expense_file = ""
        self.category_file = ""
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

    def Main_window(self):
        self.revenue_file = self.user_name + f"_revenue.xlsx"
        self.expense_file = self.user_name + f"_expense.xlsx"
        self.category_file = self.user_name + f"_category.xlsx" 
        
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
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.btn_search.clicked.connect(self.search)
        self.btn_report.clicked.connect(self.report)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_exit.clicked.connect(self.exit)

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
        
    def set_rev_attr(self) :
        self.rev_amount = self.amount_of_revenue_line.text()
        self.rev_day = self.day_of_revenue_line.text()
        self.rev_month = self.month_of_revenue_line.text()
        self.rev_year = self.year_of_revenue_line.text()
        self.rev_source = self.source_of_revenue_line.text()
        self.rev_desc = self.description_revenue_line.text()
        self.rev_type = self.type_of_revenue_line.text()     