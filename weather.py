from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root  = Tk()
root.title('VB Weather Forecasting App')
root.geometry('890x470+300+200')
root.configure(bg='#1974D2')
root.resizable(False,False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f'{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E')

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I : %M %p')
    clock.config(text=current_time)

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=6442700e8816c4110158c787eb10c317"

    result = requests.get(api)
      
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp = json['main']['temp']
        humidity = json['main']['humidity']
        pressure = json['main']['pressure']
        wind = json['wind']['speed']
        description = json['weather'][0]['main']
        final = [city, country, temp, humidity, pressure, wind, description]
        print(final)

        t.config(text=(temp, "°C"))
        h.config(text=(humidity, '%'))
        p.config(text=(pressure, 'hPa'))
        w.config(text=(wind, 'm/s'))
        d.config(text=description)

        #first cell
        firstdayimage = json['weather'][0]['icon']
        print(firstdayimage)
        
        img = (Image.open(f'icon/{firstdayimage}@2x.png'))
        photo1 = ImageTk.PhotoImage(img)
        firstimage.config(image=photo1)
        firstimage.image = photo1

        tempdaymin1 = json['main']['temp_min']
        tempdaymax1 = json['main']['temp_max']

        day1temp.config(text=f'Min: {tempdaymin1}\n Max: {tempdaymax1}')

        #second cell
        seconddayimage = json['weather'][0]['icon']
        print(seconddayimage)

        img = (Image.open(f'icon/{seconddayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image = photo2

        tempdaymin2 = json['main']['temp_min']
        tempdaymax2 = json['main']['temp_max']

        day2temp.config(text=f'Min: {tempdaymin2}\n Max: {tempdaymax2}')

        #third cell
        thirddayimage = json['weather'][0]['icon']
        print(thirddayimage)

        img = (Image.open(f'icon/{thirddayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo3 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo3)
        thirdimage.image = photo3

        tempdaymin3 = json['main']['temp_min']
        tempdaymax3 = json['main']['temp_max']

        day3temp.config(text=f'Min: {tempdaymin3}\n Max: {tempdaymax3}')

        #fourth cell
        fourthdayimage = json['weather'][0]['icon']
        print(fourthdayimage)

        img = (Image.open(f'icon/{fourthdayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo4 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo4)
        fourthimage.image = photo4

        tempdaymin4 = json['main']['temp_min']
        tempdaymax4 = json['main']['temp_max']

        day4temp.config(text=f'Min: {tempdaymin4}\n Max: {tempdaymax4}')

        #fifth cell
        fifthdayimage = json['weather'][0]['icon']
        print(fifthdayimage)

        img = (Image.open(f'icon/{fifthdayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo5 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo5)
        fifthimage.image = photo5

        tempdaymin5 = json['main']['temp_min']
        tempdaymax5 = json['main']['temp_max']

        day5temp.config(text=f'Min: {tempdaymin5}\n Max: {tempdaymax5}')

        #sixth cell
        sixthdayimage = json['weather'][0]['icon']
        print(sixthdayimage)

        img = (Image.open(f'icon/{sixthdayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo6 = ImageTk.PhotoImage(resized_image)
        sixthimage.config(image=photo6)
        sixthimage.image = photo6

        tempdaymin6 = json['main']['temp_min']
        tempdaymax6 = json['main']['temp_max']

        day6temp.config(text=f'Min: {tempdaymin6}\n Max: {tempdaymax6}')

        #seventh cell
        seventhdayimage = json['weather'][0]['icon']
        print(seventhdayimage)

        img = (Image.open(f'icon/{seventhdayimage}@2x.png'))
        resized_image = img.resize((40,40))
        photo7 = ImageTk.PhotoImage(resized_image)
        seventhimage.config(image=photo7)
        seventhimage.image = photo7

        tempdaymin7 = json['main']['temp_min']
        tempdaymax7 = json['main']['temp_max']

        day7temp.config(text=f'Min: {tempdaymin7}\n Max: {tempdaymax7}')

        #days
        first = datetime.now()
        day1.config(text=first.strftime('%A'))

        second = first+timedelta(days=1)
        day2.config(text=second.strftime('%A'))

        third = first+timedelta(days=2)
        day3.config(text=third.strftime('%A'))

        fourth = first+timedelta(days=3)
        day4.config(text=fourth.strftime('%A'))

        fifth = first+timedelta(days=4)
        day5.config(text=fifth.strftime('%A'))

        sixth = first+timedelta(days=5)
        day6.config(text=sixth.strftime('%A'))

        seventh = first+timedelta(days=6)
        day7.config(text=seventh.strftime('%A'))


    else:
        print("NO Content Found")



##icon
image_icon = PhotoImage(file='images/logo.png')
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file='images/Rounded Rectangle 1.png')
Label(root, image=Round_box, bg='#1974D2', height=120, width=180 ).place(x=50, y=110)

#label
label1 = Label(root, text='Temperature:', font=('Helvetica', 11), fg='white', bg='#203243')
label1.place(x=60, y=120)

label2 = Label(root, text='Humidity:', font=('Helvetica', 11), fg='white', bg='#203243')
label2.place(x=60, y=140)

label3 = Label(root, text='Pressure:', font=('Helvetica', 11), fg='white', bg='#203243')
label3.place(x=60, y=160)

label4 = Label(root, text='Wind Speed:', font=('Helvetica', 11), fg='white', bg='#203243')
label4.place(x=60, y=180)

label5 = Label(root, text='Description:', font=('Helvetica', 11), fg='white', bg='#203243')
label5.place(x=60, y=200)

##search box
Search_image = PhotoImage(file='images/Rounded Rectangle 3.png')
myimage = Label(image=Search_image, bg='#1974D2')
myimage.place(x=290, y=120)

weat_image = PhotoImage(file='images/Layer 7.png')
weather_image = Label(root, image=weat_image, bg='#203243')
weather_image.place(x=310, y=127)

textfield = tk.Entry(root, justify='center', width=18, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
textfield.place(x=380, y=130)
textfield.focus()

Search_icon = PhotoImage(file='images/Layer 6.png')
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg='#203243', command=getWeather)
my_image_icon.place(x=655, y=125)

##Bottom Box
frame = Frame(root, width=900, height=180, bg='#000000')
frame.pack(side=BOTTOM)

#bottom boxes
firstbox = PhotoImage(file='images/Rounded Rectangle 2.png')
secondbox = PhotoImage(file='images/Rounded Rectangle 2 copy.png')

Label(frame, image=firstbox, bg='#000000').place(x=30, y=20)
Label(frame, image=secondbox, bg='#000000').place(x=300, y=30)
Label(frame, image=secondbox, bg='#000000').place(x=400, y=30)
Label(frame, image=secondbox, bg='#000000').place(x=500, y=30)
Label(frame, image=secondbox, bg='#000000').place(x=600, y=30)
Label(frame, image=secondbox, bg='#000000').place(x=700, y=30)
Label(frame, image=secondbox, bg='#000000').place(x=800, y=30)

#clock(time)
clock = Label(root, font=('Helvetica', 30, 'bold'), fg='white', bg='#1974D2')
clock.place(x=30, y=20)

#timezone
timezone = Label(root, font=('Helvetica', 20), fg='white', bg='#1974D2')
timezone.place(x=700, y=20)

long_lat = Label(root, font=('Helvetica', 10), fg='white', bg='#1974D2')
long_lat.place(x=700, y=50)

#thpwd
t = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
t.place(x=150, y=120)
h = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
h.place(x=150, y=140)
p = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
p.place(x=150, y=160)
w = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
w.place(x=150, y=180)
d = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
d.place(x=150, y=200)

#first cell
firstframe = Frame(root, width=230, height=132, bg='#38ACEC')
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font='arial 20', bg='#38ACEC', fg='#000000')
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg='#38ACEC')
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg='#38ACEC', fg='#FFFF00', font='arial 15 bold')
day1temp.place(x=100, y=50)

#second cell
secondframe = Frame(root, width=70, height=115, bg='#38ACEC')
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg='#38ACEC', fg='#000000')
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg='#38ACEC')
secondimage.place(x=7, y=20)

day2temp = Label(secondframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day2temp.place(x=-5, y=60)

#third cell
thirdframe = Frame(root, width=70, height=115, bg='#38ACEC')
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, bg='#38ACEC', fg='#000000')
day3.place(x=10, y=5)

thirdimage = Label(thirdframe, bg='#38ACEC')
thirdimage.place(x=7, y=20)

day3temp = Label(thirdframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day3temp.place(x=-5, y=60)

#fourth cell
fourthframe = Frame(root, width=70, height=115, bg='#38ACEC')
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg='#38ACEC', fg='#000000')
day4.place(x=10, y=5)

fourthimage = Label(fourthframe, bg='#38ACEC')
fourthimage.place(x=7, y=20)

day4temp = Label(fourthframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day4temp.place(x=-5, y=60)

#fifth cell
fifthframe = Frame(root, width=70, height=115, bg='#38ACEC')
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg='#38ACEC', fg='#000000')
day5.place(x=10, y=5)

fifthimage = Label(fifthframe, bg='#38ACEC')
fifthimage.place(x=7, y=20)

day5temp = Label(fifthframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day5temp.place(x=-5, y=60)

#sixth cell
sixthframe = Frame(root, width=70, height=115, bg='#38ACEC')
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg='#38ACEC', fg='#000000')
day6.place(x=10, y=5)

sixthimage = Label(sixthframe, bg='#38ACEC')
sixthimage.place(x=7, y=20)

day6temp = Label(sixthframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day6temp.place(x=-5, y=60)

#seventh cell
seventhframe = Frame(root, width=70, height=115, bg='#38ACEC')
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg='#38ACEC', fg='#000000')
day7.place(x=10, y=5)

seventhimage = Label(seventhframe, bg='#38ACEC')
seventhimage.place(x=7, y=20)

day7temp = Label(seventhframe, bg='#38ACEC', fg='#00008B', font='arial 10 bold')
day7temp.place(x=-5, y=60)

root.mainloop()