from tkinter import *

import tkintermapview


waterf:list=[]
userw:list=[]
worker:list=[]
temporary:list=[]

class Water:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

class Worker():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]

class Userw():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

class temporarys:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

#temp_list_funct

def create_userw():

    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    temporary.clear()
    u=listbox_lista_obiketow.index(ACTIVE)
    d=waterf[u].name

    for idx,val in enumerate(worker):
        worker[idx].marker.delete()

    for idx,val in enumerate(userw):
        if userw[idx].location2==d:
            val=temporarys(name=userw[idx].name,location=userw[idx].location)
            temporary.append(val)
        userw[idx].marker.delete()


    show_userw_temp()
    button_pokaz_szczegoly_obiektu_userw.configure(command=show_userw_temp_details)

def show_userw_temp():
    listbox_lista_userw.delete(0,END)
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,val in enumerate(temporary):
        listbox_lista_userw.insert(idx,f'{idx+1}.{val.name}')

def show_userw_temp_details():
    o=listbox_lista_userw.index(ACTIVE)
    name=temporary[o].name
    location=temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0],temporary[o].coordinates[1])
    map_widget.set_zoom(17)


def create_workers():
    for idx, val in enumerate(temporary):
        temporary[idx].marker.delete()

    temporary.clear()
    u = listbox_lista_obiketow.index(ACTIVE)
    d = waterf[u].name

    for idx,val in enumerate(userw):
        userw[idx].marker.delete()

    for idx, val in enumerate(worker):
        if worker[idx].location2 == d:
            val = temporarys(name=worker[idx].name, location=worker[idx].location)
            temporary.append(val)

        worker[idx].marker.delete()

    show_worker_temp()
    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_temp_details)


def show_worker_temp():
    listbox_lista_userw.delete(0, END)
    listbox_lista_obiektow_worker.delete(0, END)
    for idx, val in enumerate(temporary):
        listbox_lista_obiektow_worker.insert(idx, f'{idx + 1}.{val.name}')


def show_worker_temp_details():
    o = listbox_lista_obiektow_worker.index(ACTIVE)
    name = temporary[o].name
    location = temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0], temporary[o].coordinates[1])
    map_widget.set_zoom(17)

def restore():
    show_userw()
    show_worker()

    for idx,val in enumerate(userw):
        userw[idx].marker.delete()

    for idx,val in enumerate(worker):
        worker[idx].marker.delete()

    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    for idx,val in enumerate(userw):
        userw[idx].coordinates=userw[idx].get_coordinates()
        userw[idx].marker=map_widget.set_marker(userw[idx].coordinates[0],userw[idx].coordinates[1])

    for idx,val in enumerate(worker):
        worker[idx].coordinates=worker[idx].get_coordinates()
        worker[idx].marker=map_widget.set_marker(worker[idx].coordinates[0],worker[idx].coordinates[1])

    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_details)
    button_pokaz_szczegoly_obiektu_userw.configure(command=show_userw_details)




#water_facility

def add_waterf():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    user= Water(name=zmienna_imie, location=zmienna_miejscowosc)
    waterf.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_waterf()



def show_waterf():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(waterf):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name}')


def remove_waterf():
    i=listbox_lista_obiketow.index(ACTIVE)
    waterf[i].marker.delete()
    waterf.pop(i)
    show_waterf()

def edit_waterf():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=waterf[i].name
    location=waterf[i].location

    entry_name.insert(0,name)
    entry_location.insert(0,location)

    button_dodaj_placowke.config(text='Zapisz',command=lambda: update_waterf(i))

def update_waterf(i):
    new_name=entry_name.get()
    new_location=entry_location.get()

    waterf[i].name=new_name
    waterf[i].location=new_location

    waterf[i].marker.delete()
    waterf[i].coordinates=waterf[i].get_coordinates()
    waterf[i].marker=map_widget.set_marker(waterf[i].coordinates[0],waterf[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_placowke.config(text='Dodaj obiekt',command=add_waterf)
    show_waterf()


def show_waterf_workers():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=waterf[i].name
    location=waterf[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_workers()

    map_widget.set_position(waterf[i].coordinates[0],waterf[i].coordinates[1])
    map_widget.set_zoom(17)

def show_waterf_userw():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=waterf[i].name
    location=waterf[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_userw()

    map_widget.set_position(waterf[i].coordinates[0],waterf[i].coordinates[1])
    map_widget.set_zoom(17)





#water_user

def add_userw():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= Userw(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    userw.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_userw()



def show_userw():
    listbox_lista_userw.delete(0,END)
    for idx,val in enumerate(userw):
        listbox_lista_userw.insert(idx,f'{idx+1}. {val.name}')

def remove_userw():
    i=listbox_lista_userw.index(ACTIVE)
    userw[i].marker.delete()
    userw.pop(i)
    show_userw()

def edit_userw():
    i=listbox_lista_userw.index(ACTIVE)
    name=userw[i].name
    location=userw[i].location
    location2=userw[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_userw.config(text='Zapisz',command=lambda: update_userw(i))

def update_userw(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    userw[i].name=new_name
    userw[i].location=new_location
    userw[i].location2=new_location2

    userw[i].marker.delete()
    userw[i].coordinates=userw[i].get_coordinates()
    userw[i].marker=map_widget.set_marker(userw[i].coordinates[0],userw[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_userw.config(text='Dodaj obiekt',command=add_userw)
    show_userw()


def show_userw_details():
    i=listbox_lista_userw.index(ACTIVE)
    name=userw[i].name
    location=userw[i].location
    location2=userw[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(userw[i].coordinates[0],userw[i].coordinates[1])
    map_widget.set_zoom(17)



#water_worker

def add_worker():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= Worker(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    worker.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_worker()



def show_worker():
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,user in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx,f'{idx+1}. {user.name}')


def remove_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    worker[i].marker.delete()
    worker.pop(i)
    show_worker()

def edit_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_worker.config(text='Zapisz',command=lambda: update_worker(i))

def update_worker(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    worker[i].name=new_name
    worker[i].location=new_location
    worker[i].location2=new_location2

    worker[i].marker.delete()
    worker[i].coordinates=worker[i].get_coordinates()
    worker[i].marker=map_widget.set_marker(worker[i].coordinates[0],worker[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_worker.config(text='Dodaj obiekt',command=add_worker)
    show_worker()


def show_worker_details():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(worker[i].coordinates[0],worker[i].coordinates[1])
    map_widget.set_zoom(17)








root = Tk()
root.geometry("1920x1080")
root.title("Project POP BB")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista punktów poboru wody")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły użytkowników', command=show_waterf_userw)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły pracowników', command=show_waterf_workers)
button_pokaz_szczegoly_obiektu.grid(row=3, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_waterf)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_waterf)
button_edytuj_obiekt.grid(row=2, column=2)


label_lista_obiektow_userw=Label(ramka_lista_obiektow, text="Lista użytkowników")
label_lista_obiektow_userw.grid(row=0, column=3,columnspan=2)
listbox_lista_userw=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_userw.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_userw=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_userw_details)
button_pokaz_szczegoly_obiektu_userw.grid(row=2, column=3)
button_usun_obiekt_userw=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_userw)
button_usun_obiekt_userw.grid(row=2, column=4)
button_edytuj_obiekt_userw=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_userw)
button_edytuj_obiekt_userw.grid(row=2, column=5)

label_lista_obiektow_worker=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_worker.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_worker=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_worker.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_worker=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_worker_details)
button_pokaz_szczegoly_obiektu_worker.grid(row=2, column=6)
button_usun_obiekt_worker=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_worker)
button_usun_obiekt_worker.grid(row=2, column=7)
button_edytuj_obiekt_worker=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_worker)
button_edytuj_obiekt_worker.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Nazwa:")
label_name.grid(row=1, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=2, column=0,sticky=W)
label_location2=Label(ramka_formularz, text="Punkt poboru:")
label_location2.grid(row=3, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=2, column=1)
entry_location2=Entry(ramka_formularz)
entry_location2.grid(row=3, column=1)

button_dodaj_placowke=Button(ramka_formularz, text='Dodaj punkt poboru wody',command=add_waterf)
button_dodaj_placowke.grid(row=5, column=0, columnspan=2)

button_dodaj_userw=Button(ramka_formularz, text='Dodaj użytkownika',command=add_userw)
button_dodaj_userw.grid(row=6, column=0, columnspan=2)

button_dodaj_worker=Button(ramka_formularz, text='Dodaj pracownika',command=add_worker)
button_dodaj_worker.grid(row=7, column=0, columnspan=2)

button_odswiez=Button(ramka_formularz,text='Odśwież listę',command=restore)
button_odswiez.grid(row=8, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=1, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Nazwa:")
label_szczegoly_name.grid(row=1, column=1)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=2)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=3)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=4)
label_szczegoly_location2=Label(ramka_szczegoly_obiektow, text="Punkt poboru wody:")
label_szczegoly_location2.grid(row=1, column=5)
label_szczegoly_location2_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location2_wartosc.grid(row=1, column=6)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()
