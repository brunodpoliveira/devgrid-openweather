import pyowm
from tkinter import *


def omw():
    api_key = "b56313ea4d28f614df3e9483fb47ac4a"
    owm_obj = pyowm.OWM(api_key)
    city_name = city_f.get()
    obs_obj = owm_obj.weather_at_place(city_name)
    weather = obs_obj.get_weather()
    temp = weather.get_temperature('celsius')["temp"]
    humidity = weather.get_humidity()
    description = weather.get_detailed_status()
    temp_f.insert(15, str(temp) + " Celcius ")
    humid_f.insert(15, str(humidity) + " %")
    desc_f.insert(10, str(description))


def clear():
    city_f.delete(0, END)
    temp_f.delete(0, END)
    humid_f.delete(0, END)
    desc_f.delete(0, END)


# Driver code
root = Tk()
root.title("Weather")
root.configure(background="#a1dbcd")
root.geometry("500x480")
label = Label(root, text="Weather Script", fg='#a1dbcd', bg='#383a39')
label1 = Label(root, text="Enter the City :", fg='black', bg='#a1dbcd')
label2 = Label(root, text="Temperature :", fg='black', bg='#a1dbcd')
label3 = Label(root, text="Humidity :", fg='black', bg='#a1dbcd')
label4 = Label(root, text="Description  :", fg='black', bg='#a1dbcd')
city_f = Entry(root)
temp_f = Entry(root)
humid_f = Entry(root)
desc_f = Entry(root)
b1 = Button(root, text="Tell Weather!", bg='#383a39', fg='#a1dbcd', command=omw)
b2 = Button(root, text="Clear", bg='#383a39', fg='#a1dbcd', command=clear)
label.grid(row=0, column=2)
label1.grid(row=2, column=2)
label2.grid(row=5, column=2)
label3.grid(row=7, column=2)
label4.grid(row=9, column=2)
city_f.grid(row=3, column=2, ipadx="180")
temp_f.grid(row=6, column=2, ipadx="180")
humid_f.grid(row=8, column=2, ipadx="180")
desc_f.grid(row=10, column=2, ipadx="180")
b1.grid(row=4, column=2)
b2.grid(row=11, column=2)
root.mainloop()
