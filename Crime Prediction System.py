import tkinter as tk
from tkinter import *

import os
import pandas as pd
import numpy as np
import random
import matplotlib
import pickle

matplotlib.use('TkAgg')
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import Figure
from PIL import ImageTk, Image

global cr, months, rate, city_names

cr = ['Burglary', 'Kidnapping', 'Murder', 'Rape', 'Theft']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

city_names = ["Agra", "Aligarh", "Allahabad", "Amroha", "Aonla", "Auraiya", "Ayodhya", "Azamgarh", "Baheri", "Bahraich",
              "Ballia", "Balrampur", "Banda", "Baraut", "Bareli", "Basti", "Behta Hajipur", "Bela", "Bhadohi", "Bijnor",
              "Bisalpur", "Biswan", "Budaun", "Bulandshahar", "Chandausi", "Chandpur", "Chhibramau", "Chitrakut", "Dadri",
              "Deoband", "Deoria", "Etah", "Etawah", "Faizabad", "Faridpur", "Farrukhabad", "Fatehpur", "Firozabad",
              "Gajraula", "Ganga Ghat", "Gangoh", "Ghaziabad", "Ghazipur", "Gola Gokarannath", "Gonda", "Gorakhpur",
              "Hapur", "Hardoi", "Hasanpur", "Hathras", "Jahangirabad", "Jalaun", "Jaunpur", "Jhansi", "Kadi", "Kairana",
              "Kannauj", "Kanpur", "Kanpur Cantonment", "Kasganj", 'Khatauli', 'Khora', 'Khurja', 'Kiratpur', 'Kosi Kalan',
              'Laharpur', 'Lakhimpur', 'Lucknow', 'Lucknow Cantonment', 'Lalitpur', 'Loni', 'Mahoba', 'Mainpuri',
              'Mathura', 'Mau', 'Mauranipur', 'Mawana', 'Mirat', 'Mirat Cantonment', 'Mirzapur', 'Modinagar', 'Moradabad',
              'Mubarakpur', 'Mughal Sarai', 'Muradnagar', 'Muzaffarnagar', 'Nagina', 'Najibabad', 'Nawabganj', 'Noida',
              'Obra', 'Orai', 'Pilibhit', 'Pilkhuwa', 'Raebareli', 'Ramgarh', 'Rampur', 'Rath', 'Renukut', 'Saharanpur',
              'Sahaswan', 'Sambhal', 'Sandila', 'Shahabad', 'Shahjahanpur', 'Shamli', 'Sherkot', 'Shikohabad',
              'Sikandarabad', 'Sitapur', 'Sukhmalpur Nizamabad', 'Sultanpur', 'Tanda', 'Tilhar', 'Tundla', 'Ujhani',
              'Unnao', 'Varanasi', 'Vrindavan']

rate = [[5, 19], [8, 28], [3, 11], [0, 5], [15, 49]]
pred = list()


def generate_plot():
    global top, table_string, crime_string, crime_listbox, freq_listbox
    global crime_label, freq_label

    ci = str(city.get().strip()).title()
    ye = int(float(year.get().strip()))
    mo = str(month.get().strip()).title()

    pred = checkCrime(temp, ci, ye, mo)

    ctype = pd.Series(cr)

    top = tk.Frame(dw)
    top.place(x=540, y=100)

    fig = matplotlib.pyplot.Figure(figsize=(7, 5))
    canvas = FigureCanvasTkAgg(fig, top)
    canvas.get_tk_widget().pack()

    ax1 = fig.add_subplot(111)

    # Create bars
    tab = pd.DataFrame()
    tab['Crime'] = cr
    tab['Frequency'] = pred

    table_string = tk.Label(dw, text="Table", bg='SkyBlue1', font=("calibri", 36, "bold"))
    table_string.place(x=180, y=390)

    x = 'Crimes in ' + ci + ' in ' + mo + ", " + str(ye)
    crime_string = tk.Label(dw, text=x, bg='SkyBlue1', font=("calibri", 21, "bold"))
    crime_string.place(x=90, y=450)

    crime_label = tk.Label(dw, text="Crime", font="times 21 bold", bg="SkyBlue1")
    crime_label.place(x=110, y=490)
    freq_label = tk.Label(dw, text="Frequency", font="times 21 bold", bg="SkyBlue1")
    freq_label.place(x=300, y=490)
    tk.Label(dw, text="", bg="SkyBlue1").place(x=100, y=505)

    crime_listbox = Listbox(dw, width=11, height=10, highlightthickness=0, selectbackground="SkyBlue1",
                            selectforeground="black", selectborderwidth=0, activestyle="none", bg="SkyBlue1", relief="solid", bd=0, font="times 21 bold")
    crime_listbox.insert(END, *cr)
    crime_listbox.place(x=110, y=530)

    freq_listbox = Listbox(dw, width=4, height=10, highlightthickness=0, selectbackground="SkyBlue1",
                           selectforeground="black", selectborderwidth=0, activestyle="none", bg="SkyBlue1", relief="solid", bd=0, font="times 21 bold")
    freq_listbox.insert(END, *pred)
    freq_listbox.place(x=300, y=530)

    # table = tk.Label(dw, text=tab.to_string(index=False), bg="SkyBlue1", font=("calibri", 21, "bold"))
    # table.place(x=120, y=500)

    background_label_dw.place_forget()
    tab.plot(kind='bar', legend=True, ax=ax1, width=0.6)
    ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=4, ncol=2, borderaxespad=0.)

    # Create names on the x-axis
    ax1.set_xticklabels(ctype.values, rotation=0)
    ax1.set_xlabel("Crimes", fontsize=14)
    ax1.set_ylabel("Frequency", fontsize=14)

    canvas.draw()


def sumascii(st):
    ans = 0
    for i in st:
        ans = ans + ord(i)
    return ans


def resetInput(inpu):
    inpu = pd.DataFrame([np.array(138 * [0])], columns=pd.Series(df.columns))
    inpu = inpu.iloc[:, :137]
    return inpu


def passInput(inpu, y, c, m, r):
    y = int(y)
    fre = rate[cr.index(r)]
    inpu.at[0, 'Yr'] = (y - 2000) * 12 + (months.index(m) + 1) * 17 + (random.randint(fre[0], fre[1])) * 3 + int(sumascii(c))
    inpu.at[0, 'City_' + c] = 5
    inpu.at[0, 'Month_' + m] = 5
    inpu.at[0, 'Crime' + r] = 5
    return inpu


def checkCrime(inpu, ct, yr, mn):
    ans = []

    for i in range(len(cr)):
        inpu = passInput(resetInput(inpu), yr, ct, mn, cr[i])
        freq = crime_model.predict(inpu)
        ans.append(round(freq[0]))
    return ans


# Designing data analysis window
def daw():
    global city, year, month, background_label_dw
    global dw, df
    global c1, c2, c3, c, y, m
    global temp
    global crime_model

    temp = pd.DataFrame()

    city = tk.StringVar()
    month = tk.StringVar()
    year = tk.StringVar()

    dw = tk.Toplevel(main_screen)
    dw.title("Crime Prediction")
    dw.geometry("1200x600")
    dw.configure(background='SkyBlue1')
    dw.state('zoomed')
    dw.overrideredirect(True)
    dw.focus_force()

    delete_login_screen()

    background_label_dw = tk.Label(dw, width=325, height=306, bg="SkyBlue1", image=filename)
    background_label_dw.place(x=1000, y=400)

    x = "Crime Prediction using Data Analysis - Welcome " + str(username_label_dw).upper()
    tk.Label(dw, text=x, width=137, height=2, fg="white", bg="DeepSkyBlue3", font="calibri 17 bold").place(x=0, y=0)

    # opening trained predictive model
    with open('crime_model.pkl', 'rb') as file:
        crime_model = pickle.load(file)

    tk.Label(dw, text="City", bg='SkyBlue1', font="calibri 18 bold").place(x=60, y=90)
    c1 = tk.Entry(dw, textvariable=city, font=("calibri", 16))
    c1.place(x=150, y=90)
    c1.bind("<Return>", c3_return)

    tk.Label(dw, text="Year", bg='SkyBlue1', font="calibri 18 bold").place(x=60, y=130)
    c2 = tk.Entry(dw, textvariable=year, font=("calibri", 16))
    c2.place(x=150, y=130)
    c2.bind("<Return>", c3_return)

    tk.Label(dw, text="Month", bg='SkyBlue1', font="calibri 18 bold").place(x=60, y=170)
    c3 = tk.Entry(dw, textvariable=month, font=("calibri", 16))
    c3.place(x=150, y=170)
    c3.bind("<Return>", c3_return)

    predict_button = tk.Button(dw, text="Predict", width=10, height=2, fg="black", bg="white", font="calibri 18 bold",
                               command=validate_entry_predict_button)
    predict_button.place(x=100, y=230)
    predict_button.bind("<Return>", predict_return)

    clear_button = tk.Button(dw, text="Clear", width=10, height=2, fg="black", bg="white", font="calibri 18 bold",
                             command=clear_screen)
    clear_button.place(x=265, y=230)
    clear_button.bind("<Return>", clear_return)

    sign_out_button = tk.Button(dw, text="Sign Out", width=6, height=1, fg="black", bg="white", font="calibri 11 bold",
                                command=back_to_main_screen_from_dw)
    sign_out_button.place(x=1305, y=10)
    sign_out_button.bind("<Return>", sign_out_return)


def validate_entry_predict_button():
    global city_label, month_label, year_label, wrong_city_label, wrong_year_label, wrong_year_input_label, wrong_month_label

    city_label = tk.Label(dw, text="Please enter the city name!", font="times 14 bold", bg="SkyBlue1", fg="black")
    wrong_city_label = tk.Label(dw, text="Please enter cities of Uttar Pradesh only!", font="times 14 bold", bg="SkyBlue1", fg="black")

    year_label = tk.Label(dw, text="Please enter the year!", font="times 14 bold", bg="SkyBlue1", fg="black")
    wrong_year_label = tk.Label(dw, text="Please enter valid year! (>2018 and only 4 digits)", font="times 14 bold", bg="SkyBlue1", fg="black")
    wrong_year_input_label = tk.Label(dw, text="Please enter only digits for year!", font="times 14 bold", bg="SkyBlue1", fg="black")

    month_label = tk.Label(dw, text="Please enter the month name!", font="times 14 bold", bg="SkyBlue1", fg="black")
    wrong_month_label = tk.Label(dw, text="Please enter correct month name!", font="times 14 bold", bg="SkyBlue1", fg="black")

    if not city.get().strip():
        city_label.place(x=400, y=91)
        city_label.after(1500, destroy_label)
        c1.delete(0, END)
        return

    if city.get().strip().title() not in city_names:
        wrong_city_label.place(x=400, y=91)
        wrong_city_label.after(2000, destroy_label)
        c1.delete(0, END)
        return

    if not year.get().strip():
        year_label.place(x=400, y=131)
        year_label.after(1500, destroy_label)
        c2.delete(0, END)
        return

    temp_year = year.get().strip()
    if temp_year.isnumeric():
        length = len(temp_year)
        temp_year = int(temp_year)
        if temp_year <= 2018 or length != 4:
            wrong_year_label.place(x=400, y=131)
            wrong_year_label.after(2000, destroy_label)
            c2.delete(0, END)
            return

    elif not temp_year.isnumeric():
        wrong_year_input_label.place(x=400, y=131)
        wrong_year_input_label.after(1500, destroy_label)
        c2.delete(0, END)
        return

    if not month.get().strip():
        month_label.place(x=400, y=171)
        month_label.after(1500, destroy_label)
        c3.delete(0, END)
        return

    if month.get().strip().title() not in months:
        wrong_month_label.place(x=400, y=171)
        wrong_month_label.after(2000, destroy_label)
        c3.delete(0, END)
        return

    generate_plot()


def destroy_label():
    city_label.destroy()
    year_label.destroy()
    month_label.destroy()
    wrong_city_label.destroy()
    wrong_year_label.destroy()
    wrong_year_input_label.destroy()
    wrong_month_label.destroy()


def c3_return(event=None):
    validate_entry_predict_button()


def predict_return(event=None):
    generate_plot()


def clear_return(event=None):
    clear_screen()


def sign_out_return(event=None):
    back_to_main_screen_from_dw()


def clear_screen():
    c1.delete(0, END)
    c2.delete(0, END)
    c3.delete(0, END)
    top.destroy()
    table_string.destroy()
    crime_string.destroy()
    crime_label.destroy()
    freq_label.destroy()
    crime_listbox.destroy()
    freq_listbox.destroy()
    background_label_dw.place(x=1000, y=400)


def back_to_main_screen_from_dw():
    main_screen.deiconify()
    dw.destroy()


# Designing window for registration
def register():
    main_screen.withdraw()
    global register_screen
    register_screen = tk.Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("600x450")
    register_screen.resizable(False, False)
    register_screen.configure(background="SkyBlue1")
    register_screen.focus_force()

    global username
    global password
    global username_Entry
    global password_Entry
    global register_button, info_button, back_button_reg_scr, info_button_username

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, width="800", height="2", text="Please enter details below", fg="white", bg="DeepSkyBlue3", font="calibri 15 bold").pack()
    tk.Label(register_screen, text="", bg="SkyBlue1").pack()

    background_label_2 = tk.Label(register_screen, width=325, height=306, bg="SkyBlue1", image=filename)
    background_label_2.place(x=25, y=90)

    username_label = tk.Label(register_screen, bg='SkyBlue1', text="Username * ")
    username_label.place(x=425, y=150)
    username_Entry = tk.Entry(register_screen, textvariable=username)
    username_Entry.place(x=400, y=175)

    info_button_username = tk.Label(register_screen, text="info", bg='SkyBlue1', border=0)
    info_button_username.place(x=535, y=177)
    info_button_username.bind("<Enter>", enter_username)
    info_button_username.bind("<Leave>", close_username)

    tk.Label(register_screen, text="", bg="SkyBlue1").place(x=400, y=200)

    password_label = tk.Label(register_screen, bg='SkyBlue1', text="Password * ")
    password_label.place(x=425, y=210)
    password_Entry = tk.Entry(register_screen, textvariable=password, show='*')
    password_Entry.place(x=400, y=235)
    password_Entry.bind("<Return>", password_entry_return)

    info_button = tk.Label(register_screen, text="info", bg='SkyBlue1', border=0)
    info_button.place(x=535, y=237)
    info_button.bind("<Enter>", enter_password)
    info_button.bind("<Leave>", close_password)

    # tk.Label(register_screen, text="", bg="SkyBlue1").pack()

    register_button = tk.Button(register_screen, text="Register", width=10, height=1, bg="DeepSkyBlue3", fg="white", command=register_user)
    register_button.place(x=422, y=290)
    register_button.bind("<Return>", register_button_return)

    back_button_reg_scr = tk.Button(register_screen, text="Back", width=5, height=1, bg="DeepSkyBlue3", fg="white", command=back_to_main_screen_from_reg_scr)
    back_button_reg_scr.place(x=440, y=328)
    back_button_reg_scr.bind("<Return>", back_button_reg_scr_return)


def password_entry_return(event=None):
    register_user()


def register_button_return(event=None):
    register_user()


def back_button_reg_scr_return(event=None):
    back_to_main_screen_from_reg_scr()


def enter_username(event=None):
    global hover1

    x, y, cx, cy = info_button_username.bbox("insert")
    x += info_button_username.winfo_rootx() + 20
    y += info_button_username.winfo_rooty() + 15

    hover1 = tk.Toplevel(info_button_username)

    # Leaves only the label and removes the app window
    hover1.wm_overrideredirect(True)
    hover1.wm_geometry("+%d+%d" % (x, y))
    label = tk.Label(hover1, text="Only alpha-numeric allowed", justify='left', background='yellow', relief='solid',
                     borderwidth=1, font=("times", "8"))
    label.pack(ipadx=1)
    label.after(4000, close_username)


def close_username(event=None):
    if hover1:
        hover1.destroy()


def enter_password(event=None):
    global hover2

    # x = y = 0
    x, y, cx, cy = info_button.bbox("insert")
    x += info_button.winfo_rootx() + 20
    y += info_button.winfo_rooty() + 15

    hover2 = tk.Toplevel(info_button)

    # Leaves only the label and removes the app window
    hover2.wm_overrideredirect(True)
    hover2.wm_geometry("+%d+%d" % (x, y))
    label = tk.Label(hover2, text="!%^()+=-/~`* not allowed", justify='left', background='yellow', relief='solid',
                     borderwidth=1, font=("times", "8"))
    label.pack(ipadx=1)
    label.after(4000, close_password)


def close_password(event=None):
    if hover2:
        hover2.destroy()


def back_to_main_screen_from_reg_scr():
    main_screen.deiconify()
    register_screen.destroy()


# Implementing event on register tk.Button
def register_user():
    username_info = username.get()
    password_info = password.get()

    if not username_info.isalnum():
        invalid_username()
        return

    sym = ['!', '%', '^', '(', ')', '+', '=', '-', '/', '~', '`', '*']
    for i in sym:
        if i in password_info:
            invalid_password()
            return

    if len(password_info) < 4:
        invalid_password_length()
        return

    list_of_files = os.listdir()
    if username_info in list_of_files:
        invalid_username2()
        return

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    register_button.destroy()
    back_button_reg_scr.destroy()

    tk.Label(register_screen, text="Registration Success login to continue", fg="forest green", bg="SkyBlue1", font=("calibri", 11, "bold")).place(x=345, y=275)

    reg_login_button = tk.Button(register_screen, text="Login", width=10, height=1, bg="DeepSkyBlue3", fg="white", command=delete_register_screen)
    reg_login_button.place(x=435, y=310)
    reg_login_button.focus_set()
    reg_login_button.bind("<Return>", reg_login_button_return)


def reg_login_button_return(event=None):
    delete_register_screen()


def invalid_username():
    global invalid_username_screen
    global invalid_username_label
    invalid_username_screen = tk.Toplevel(main_screen)
    invalid_username_screen.geometry("180x100")
    invalid_username_screen.configure(background="DeepSkyBlue3")
    invalid_username_screen.resizable(False, False)
    invalid_username_screen.title("Invalid Username")
    invalid_username_screen.focus_force()

    invalid_username_label = tk.Label(invalid_username_screen, bg="DeepSkyBlue3", text="Enter only alphabets\n and numbers!", fg="black",
                                      font=("times", 12, "bold"))
    invalid_username_label.pack()

    tk.Label(invalid_username_screen, bg="DeepSkyBlue3", text="").pack()

    ok_button_invalid_username = tk.Button(invalid_username_screen, text="OK", width=7, height=1, command=clear_username)
    ok_button_invalid_username.pack()
    ok_button_invalid_username.bind("<Return>", ok_button_invalid_username_return)


def invalid_username2():
    global invalid_username_screen
    global invalid_username_label
    invalid_username_screen = tk.Toplevel(main_screen)
    invalid_username_screen.geometry("180x100")
    invalid_username_screen.configure(background="DeepSkyBlue3")
    invalid_username_screen.resizable(False, False)
    invalid_username_screen.title("Invalid Username")
    invalid_username_screen.focus_force()

    invalid_username_label = tk.Label(invalid_username_screen, bg="DeepSkyBlue3", text="Username already exists!", fg="black",
                                      font=("times", 12, "bold"))
    invalid_username_label.pack()

    tk.Label(invalid_username_screen, bg="DeepSkyBlue3", text="").pack()

    ok_button_invalid_username = tk.Button(invalid_username_screen, text="OK", width=7, height=1, command=clear_username)
    ok_button_invalid_username.pack()
    ok_button_invalid_username.bind("<Return>", ok_button_invalid_username_return)


def ok_button_invalid_username_return(event=None):
    clear_username()


def clear_username():
    invalid_username_screen.destroy()
    username_Entry.delete(0, END)
    password_Entry.delete(0, END)


def invalid_password():
    global invalid_password_screen
    global invalid_password_label
    invalid_password_screen = tk.Toplevel(main_screen)
    invalid_password_screen.geometry("200x100")
    invalid_password_screen.configure(background="DeepSkyBlue3")
    invalid_password_screen.resizable(False, False)
    invalid_password_screen.title("Invalid Password")
    invalid_password_screen.focus_force()

    sym = ['!', '%', '^', '(', ')', '+', '=', '-', '/', '~', '`', '*']
    invalid_password_label = tk.Label(invalid_password_screen, bg="DeepSkyBlue3", text="Special symbol in password \n not allowed", fg="black",
                                      font=("times", 12, "bold"))
    invalid_password_label.pack()
    tk.Label(invalid_password_screen, bg="DeepSkyBlue3", fg="white", text=sym, font=("calibri", 11, "bold")).pack()

    ok_button_invalid_password_screen = tk.Button(invalid_password_screen, text="Ok", width=7, height=1, command=clear_password)
    ok_button_invalid_password_screen.pack()
    ok_button_invalid_password_screen.bind("<Return>", ok_button_invalid_password_screen_return)


def ok_button_invalid_password_screen_return(event=None):
    clear_password()


def invalid_password_length():
    global invalid_password_screen
    global invalid_password_length_label
    invalid_password_screen = tk.Toplevel(main_screen)
    invalid_password_screen.geometry("200x100")
    invalid_password_screen.resizable(False, False)
    invalid_password_screen.configure(background="DeepSkyBlue3")
    invalid_password_screen.title("Invalid Password")
    invalid_password_screen.focus_force()

    invalid_password_length_label = tk.Label(invalid_password_screen, bg="DeepSkyBlue3", text="Minimum password length \n should be 4",
                                             fg="black", font=("calibri", 12, "bold"))
    invalid_password_length_label.pack()

    tk.Label(invalid_password_screen, bg="DeepSkyBlue3", text="").pack()

    ok_button_invalid_password_screen = tk.Button(invalid_password_screen, text="Ok", width=7, height=1, command=clear_password_length)
    ok_button_invalid_password_screen.pack()
    ok_button_invalid_password_screen.bind("<Return>", ok_button_invalid_password_screen_return2)


def ok_button_invalid_password_screen_return2(event=None):
    clear_password_length()


def clear_password():
    invalid_password_screen.destroy()
    password_Entry.delete(0, END)


def clear_password_length():
    invalid_password_screen.destroy()
    password_Entry.delete(0, END)


# Designing window for login
def login():
    main_screen.withdraw()
    global login_screen
    global username_verify
    global password_verify
    global username_login_Entry
    global password_login_Entry

    login_screen = tk.Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("600x450")
    login_screen.resizable(False, False)
    login_screen.configure(background="SkyBlue1")
    login_screen.focus_force()

    tk.Label(login_screen, width="800", height="2", bg="DeepSkyBlue3", fg="white", text="Please enter details below to login", font="calibri 15 bold").pack()
    # tk.Label(login_screen, text="", bg="SkyBlue1").pack()

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    background_label_1 = tk.Label(login_screen, width=325, height=306, bg="SkyBlue1", image=filename)
    background_label_1.place(x=20, y=90)

    tk.Label(login_screen, bg="SkyBlue1", text="Username * ").place(x=425, y=150)
    username_login_Entry = tk.Entry(login_screen, textvariable=username_verify)
    username_login_Entry.place(x=400, y=175)

    tk.Label(login_screen, text="", bg="SkyBlue1").place(x=400, y=200)

    tk.Label(login_screen, bg="SkyBlue1", text="Password * ").place(x=425, y=210)
    password_login_Entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
    password_login_Entry.place(x=400, y=235)
    password_login_Entry.bind("<Return>", password_login_Entry_return)

    # tk.Label(login_screen, text="", bg="SkyBlue1").pack()

    login_button = tk.Button(login_screen, text="Login", width=10, height=1, bg="DeepSkyBlue3", fg="white", command=login_verify)
    login_button.place(x=422, y=290)
    login_button.bind("<Return>", login_button_return)

    back_button_log_scr = tk.Button(login_screen, text="Back", width=5, height=1, bg="DeepSkyBlue3", fg="white", command=back_to_main_screen_from_log_scr)
    back_button_log_scr.place(x=440, y=328)
    back_button_log_scr.bind("<Return>", back_button_log_scr_return)


def password_login_Entry_return(event=None):
    login_verify()


def login_button_return(event=None):
    login_verify()


def back_button_log_scr_return(event=None):
    back_to_main_screen_from_log_scr()


def back_to_main_screen_from_log_scr():
    main_screen.deiconify()
    login_screen.destroy()


# Implementing event on login tk.Button
def login_verify():
    global username_label_dw

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_label_dw = username_verify.get()

    username_login_Entry.delete(0, tk.END)
    password_login_Entry.delete(0, tk.END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            daw()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.configure(background="DeepSkyBlue3")
    password_not_recog_screen.resizable(False, False)
    password_not_recog_screen.focus_force()

    tk.Label(password_not_recog_screen, bg="DeepSkyBlue3", width=150, height=1, text="Invalid Password", font="times 12 bold").pack()
    tk.Label(password_not_recog_screen, bg="DeepSkyBlue3", text="").pack()

    ok_button_password_not_recognised = tk.Button(password_not_recog_screen, text="OK", width=7, height=1, command=delete_password_not_recognised)
    ok_button_password_not_recognised.pack()
    ok_button_password_not_recognised.bind("<Return>", ok_button_password_not_recognised_return)


def ok_button_password_not_recognised_return(event=None):
    delete_password_not_recognised()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(login_screen)
    user_not_found_screen.title("User not found")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.configure(background="DeepSkyBlue3")
    user_not_found_screen.resizable(False, False)
    user_not_found_screen.focus_force()

    tk.Label(user_not_found_screen, bg="DeepSkyBlue3", width=150, height=2, text="User Not Found", fg="black", font="times 12 bold").pack()
    tk.Label(user_not_found_screen, bg="DeepSkyBlue3", text="").pack()

    ok_button_user_not_found_screen = tk.Button(user_not_found_screen, text="OK", width=7, height=1, command=delete_user_not_found_screen)
    ok_button_user_not_found_screen.pack()
    ok_button_user_not_found_screen.bind("<Return>", ok_button_user_not_found_screen_return)


def ok_button_user_not_found_screen_return(event=None):
    delete_user_not_found_screen()


# Deleting popups
def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_register_screen():
    login()
    register_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


def exit_application():
    main_screen.destroy()


# Designing Main(first) window
def main_account_screen():
    global df, filename, main_screen

    main_screen = tk.Tk()
    filename = ImageTk.PhotoImage(Image.open('police badge.png'))
    main_screen.geometry("600x450")
    main_screen.title("Account Login")
    main_screen.configure(background="SkyBlue1")
    main_screen.resizable(False, False)

    df = pd.read_excel('output_OLS_model.xlsx')
    df = df.drop(['Year'], axis=1)

    tk.Label(text="CRIME PREDICTION", fg="white", bg="DeepSkyBlue3", width="800", height="2", font="calibri 15 bold").pack()
    tk.Label(text="", bg="SkyBlue1").pack()

    # filename = ImageTk.PhotoImage(Image.open('police badge.png'))
    background_label = tk.Label(main_screen, width=325, height=306, bg="SkyBlue1", image=filename)
    background_label.place(x=25, y=90)

    login_button_main_screen = tk.Button(text="Login", height="2", width="20", bg="DeepSkyBlue3", fg="white", font="bold", command=login)
    login_button_main_screen.place(x=380, y=170)
    login_button_main_screen.bind("<Return>", login_button_main_screen_return)

    # tk.Label(text="", bg="SkyBlue1").pack()

    register_button_main_screen = tk.Button(text="Register", height="2", width="20", bg="DeepSkyBlue3", fg="white", font="bold", command=register)
    register_button_main_screen.place(x=380, y=250)
    register_button_main_screen.bind("<Return>", register_button_main_screen_return)

    exit_button_main_screen = tk.Button(text="Exit", height="1", width="5", bg="DeepSkyBlue3", fg="white", font="bold", command=exit_application)
    exit_button_main_screen.place(x=530, y=400)
    exit_button_main_screen.bind("<Return>", exit_button_main_screen_return)

    main_screen.mainloop()


def login_button_main_screen_return(event=None):
    login()


def register_button_main_screen_return(event=None):
    register()


def exit_button_main_screen_return(event=None):
    exit_application()


main_account_screen()
