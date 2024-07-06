import base64
import sqlite3
import re, os, sys, time, pandas as pd, numpy as np
from datetime import datetime
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (QPushButton, QWidget, QMainWindow, QFileDialog, 
                             QApplication, QLabel, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QComboBox, QCompleter, QListView, 
                             QRadioButton, QButtonGroup, QTextBrowser, QCheckBox)
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt6.QtCore import Qt, QStringListModel, QTimer, QTime, QDateTime, QDate
from Main_UI import MainUI
from User import user
from Validation import check_validation



# ***********  START SIGNUP_LOGIN CLASS   ************
class signup_login(MainUI) :
    
    mounths = {"January": '31', "February": '29', "March": '31',
               "April": '30', "May": '31', "June": '30',
               "July": '31', "August": '31', "September": '30',
               "October": '31', "November": '30', "December": '31'}
    
    def __init__(self):
        user.__init__(self)
        check_validation.__init__(self)
        MainUI.__init__(self)
        self.max_error = 0
        self.countdown = 15
        
    
    # ***********  START SIGN UP WINDOW   ************

    def sign_up_window(self):
        self.signup_window = QMainWindow(self)
        self.signup_window.setGeometry(300, 100, 500, 400)
        self.signup_window.setStyleSheet("background-color: #33CC99")
        self.background_signup = QLabel(self.window)

        self.security_question_line_edit = QLineEdit(self.signup_window)
        self.security_question_line_edit.setPlaceholderText("WHAT IS YOUR FAVORITE WORD ?")

        self.first_name_line_edit = QLineEdit(self.signup_window)
        self.first_name_line_edit.setPlaceholderText('first_name')
        self.last_name_line_edit = QLineEdit(self.signup_window)
        self.last_name_line_edit.setPlaceholderText('last_name')
        self.user_name_line_edit = QLineEdit(self.signup_window)
        self.user_name_line_edit.setPlaceholderText('user_name')
        self.password_line_edit = QLineEdit(self.signup_window)
        self.password_line_edit.setPlaceholderText('password')
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeat_password_line_edit = QLineEdit(self.signup_window)
        self.repeat_password_line_edit.setPlaceholderText('repeat_password')
        self.repeat_password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.email_line_edit = QLineEdit(self.signup_window)
        self.email_line_edit.setPlaceholderText('email_address')
        self.phone_number_line_edit = QLineEdit(self.signup_window)
        self.phone_number_line_edit.setPlaceholderText('phone_number')
        self.city_line_edit = QLineEdit(self.signup_window)
        self.city_line_edit.setPlaceholderText('city')
        self.day_line_edit = QLineEdit(self.signup_window)
        self.day_line_edit.setPlaceholderText('day')
        self.mounth_line_edit = QLineEdit(self.signup_window)
        self.mounth_line_edit.setPlaceholderText('month')
        self.year_line_edit = QLineEdit(self.signup_window)
        self.year_line_edit.setPlaceholderText('year')
        
        self.close_excel_file_label = QLabel("please close the user's_file first!", self.signup_window)
        self.close_excel_file_label.setVisible(False)
        self.close_excel_file_label.setStyleSheet('color: red')
        self.first_name_label = QLabel("first_name is not valid!", self.signup_window)
        self.first_name_label.setVisible(False)
        self.first_name_label.setStyleSheet('color: red')
        self.last_name_label = QLabel("last_name is not valid!", self.signup_window)
        self.last_name_label.setVisible(False)
        self.last_name_label.setStyleSheet('color: red')
        self.password_label = QLabel("password is not valid!", self.signup_window)
        self.password_label.setVisible(False)
        self.password_label.setStyleSheet('color: red')
        self.repeat_password_label = QLabel("repeated_password is not valid!", self.signup_window)
        self.repeat_password_label.setVisible(False)
        self.repeat_password_label.setStyleSheet('color: red')
        self.security_question_label = QLabel("please answer the question", self.signup_window)
        self.security_question_label.setVisible(False)
        self.security_question_label.setStyleSheet('color: red')
        self.email_label = QLabel("email address is not valid!", self.signup_window)
        self.email_label.setVisible(False)
        self.email_label.setStyleSheet('color: red')
        self.phone_number_label = QLabel("phone_number is not valid!", self.signup_window)
        self.phone_number_label.setVisible(False)
        self.phone_number_label.setStyleSheet('color: red')
        self.city_label = QLabel("plese fill the gap", self.signup_window)
        self.city_label.setVisible(False)
        self.city_label.setStyleSheet('color: red')
        self.day_label = QLabel("birth_day is not valid!", self.signup_window)
        self.day_label.setVisible(False)
        self.day_label.setStyleSheet('color: red')
        self.mounth_label = QLabel("birth_month is not valid!", self.signup_window)
        self.mounth_label.setVisible(False)
        self.mounth_label.setStyleSheet('color: red')
        self.year_label = QLabel("birth_year is not valid!", self.signup_window)
        self.year_label.setVisible(False)
        self.year_label.setStyleSheet('color: red')

        self.line_style ="""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """

        self.day_line_edit.setStyleSheet(self.line_style)
        self.city_line_edit.setStyleSheet(self.line_style)
        self.email_line_edit.setStyleSheet(self.line_style)
        self.year_line_edit.setStyleSheet(self.line_style)
        self.first_name_line_edit.setStyleSheet(self.line_style)
        self.last_name_line_edit.setStyleSheet(self.line_style)
        self.mounth_line_edit.setStyleSheet(self.line_style)
        self.password_line_edit.setStyleSheet(self.line_style)
        self.repeat_password_line_edit.setStyleSheet(self.line_style)
        self.security_question_line_edit.setStyleSheet(self.line_style)
        self.user_name_line_edit.setStyleSheet(self.line_style)
        self.phone_number_line_edit.setStyleSheet(self.line_style)

        self.central = QWidget(self)
        self.layout = QVBoxLayout(self.central)
        self.hlayout = QHBoxLayout(self.central)
        self.hlayout1 = QHBoxLayout(self.central)
        self.hlayout2 = QHBoxLayout(self.central)
    
        self.day_combo_box = QComboBox(self.signup_window)
        self.day_combo_box.setStyleSheet("""
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
        """)

        self.mounth_combo_box = QComboBox(self.signup_window)
        self.mounth_combo_box.setStyleSheet("""
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
        """)

        self.year_combo_box = QComboBox(self.signup_window)
        self.year_combo_box.setStyleSheet("""
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
        """)

        self.year_combo_box.activated[int].connect(self.set_year_line_edit)
        self.mounth_combo_box.activated[int].connect(self.set_mounth_line_edit)
        self.day_combo_box.activated[int].connect(self.set_day_line_edit)

        self.day_list = QListView(self.signup_window)
        self.mounth_list = QListView(self.signup_window)
        self.year_list = QListView(self.signup_window)

        for i in range(1, 32) :
            self.day_combo_box.addItem(f"{i}")

        for mounth in self.mounths.keys() :
            self.mounth_combo_box.addItem(mounth)

        for i in range(1920, 2006) :
            self.year_combo_box.addItem(f"{i}")
            
        self.hlayout1.addWidget(self.year_label)
        self.hlayout1.addWidget(self.mounth_label)
        self.hlayout1.addWidget(self.day_label)    

        self.hlayout.addWidget(self.year_line_edit)
        self.hlayout.addWidget(self.mounth_line_edit)
        self.hlayout.addWidget(self.day_line_edit)

        self.hlayout2.addWidget(self.year_combo_box)
        self.hlayout2.addWidget(self.mounth_combo_box)
        self.hlayout2.addWidget(self.day_combo_box)
        
        self.layout.addWidget(self.close_excel_file_label)
        self.layout.addWidget(self.first_name_label)
        self.layout.addWidget(self.first_name_line_edit)
        self.layout.addWidget(self.last_name_label)
        self.layout.addWidget(self.last_name_line_edit)
        self.layout.addWidget(self.user_name_line_edit)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_line_edit)
        self.layout.addWidget(self.repeat_password_label)
        self.layout.addWidget(self.repeat_password_line_edit)
        self.layout.addWidget(self.security_question_label)
        self.layout.addWidget(self.security_question_line_edit)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_line_edit)
        self.layout.addWidget(self.phone_number_label)
        self.layout.addWidget(self.phone_number_line_edit)
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_line_edit)
        
        self.city_combo_box = QComboBox(self.signup_window)
        self.city_combo_box.setStyleSheet("""
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
        """)
        self.city_combo_box.addItems(self.default_cities)
    
        self.city_line_edit.textChanged.connect(self.update_combo_box)
        self.city_combo_box.activated[int].connect(self.set_city_line_edit)
        self.layout.addWidget(self.city_combo_box)
        
        self.layout.addLayout(self.hlayout1)
        self.layout.addLayout(self.hlayout)
        self.layout.addLayout(self.hlayout2)
        self.central.setLayout(self.layout)
        self.layout.setContentsMargins(200, 100, 200, 100)
        
        self.submit_btn = QPushButton("submit")
        self.submit_btn.setStyleSheet("""
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
        """)
      
        self.layout.addWidget(self.submit_btn)
        self.submit_btn.clicked.connect(self.close_signup_open_login)
        
        self.signup_window.setCentralWidget(self.central)
        self.signup_window.setWindowTitle('Signup_Login')
        self.signup_window.show()

        # ***********  END SIGN UP WINDOW   ************ 
