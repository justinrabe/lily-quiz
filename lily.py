from tkinter import *
from tkinter import ttk
from decouple import config
import mysql.connector
print('Hello World!')
db = mysql.connector.connect(
  host=config('host', default=''),
  user=config('user', default=''),
  password=config('password', default='')
)
print(db)