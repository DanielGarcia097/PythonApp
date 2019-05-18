import gi
import random
import threading
import requests
import time
import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,  GLib

class LabelWindow(Gtk.Window):
    filename = ""
    avance_actual = 0
    avance_barra = 0
    perdidas = 0
    exitosas = 0
    hora_inicio = ""
    hora_fin = ""

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")
        self.set_default_size(500,500)
        
        Vbox = Gtk.VBox()
        hbox0 = Gtk.HBox()
        Vbox.pack_start(hbox0,True,False,0)

        #ENCABEZADO:
        label = Gtk.Label()
        label.set_text("Ingresa los parametros y opciones para enviar el trafico")
        label.set_justify(Gtk.Justification.LEFT)
        hbox0.pack_start(label, True, True, 2)

        hbox1 = Gtk.HBox()
        Vbox.pack_start(hbox1,True,False,0)

        #URL:
        label = Gtk.Label()
        label.set_text("URL para Solicitudes: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox1.pack_start(label, True, True, 2)

        self.entry = Gtk.Entry()
        self.entry.set_text("http://35.185.119.34:8000/Tweets/")
        hbox1.pack_start(self.entry, True, True, 2)

        #SEGUNDO BLOQUE
        hbox2 = Gtk.HBox(True)
        Vbox.pack_start(hbox2,True,True,0)

        #CONCURRENCIA
        label = Gtk.Label()
        label.set_text("Concurrencia: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox2.pack_start(label, True, True, 2)

        self.entry2 = Gtk.Entry()
        hbox2.pack_start(self.entry2, True, True, 2)


        #SEGUNDO BLOQUE
        hbox3 = Gtk.HBox(True)
        Vbox.pack_start(hbox3,True,True,0)

        #SOLICITUDES
        label = Gtk.Label()
        label.set_text("Solicitudes: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox3.pack_start(label, True, True, 2)

        self.entry3 = Gtk.Entry()
        hbox3.pack_start(self.entry3, True, True, 2)

        #TERCER BLOQUE
        hbox4 = Gtk.HBox(True)
        Vbox.pack_start(hbox4,True,True,0)

        #PARAMETROS
        label = Gtk.Label()
        label.set_text("Parametros: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox4.pack_start(label, True, True, 2)

        file = Gtk.FileChooserButton()
        file.connect("selection-changed", self.on_file_selected)
        hbox4.pack_start(file, True, True, 2)

        #CUARTO BLOQUE
        hbox5 = Gtk.HBox(True)
        Vbox.pack_start(hbox5,True,True,0)

        #TIME OUT
        label = Gtk.Label()
        label.set_text("Time Out: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox5.pack_start(label, True, True, 2)

        self.entry4 = Gtk.Entry()
        hbox5.pack_start(self.entry4, True, True, 2)

        #CUARTO BLOQUE
        hbox6 = Gtk.HBox(True)
        Vbox.pack_start(hbox6,True,True,0)

        #BARRA CARGA
        label = Gtk.Label()
        label.set_text("Completado: ")
        label.set_justify(Gtk.Justification.LEFT)
        hbox6.pack_start(label, True, True, 2)

        self.barra = Gtk.LevelBar()
        self.barra.set_min_value(0)
        self.barra.set_max_value(100)
        self.barra.set_value(0)
        hbox6.pack_start(self.barra, True, True, 2)

        button4 = Gtk.Button("Ejecutar")
        button4.connect("clicked",self.on_clicked_button)
        hbox6.pack_start(button4, True, True, 2)

        #BARRA CARGA
        label = Gtk.Label()
        label.set_text("Resumen")
        Vbox.pack_start(label, True, True, 2)

        self.resumen = Gtk.Label()
        Vbox.pack_start(self.resumen, True, True, 2)


        close = Gtk.Button("SALIR")
        close.connect("clicked",self.quit)
        Vbox.pack_start(close,True,True,2)

        self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

        self.add(Vbox)
        
    def on_file_selected(self, widget):
      self.filename= widget.get_filename()
        
    def quit(self,window):
      Gtk.main_quit()

    def on_clicked_button(self,widget):
      t = threading.Thread(target=self.Hilo_Hilos)
      t.start()
    


    def Hilo_Hilos(self):

      self.hora_inicio = str(datetime.datetime.now())
      parametros = []
      
      print "File Choosen: ", self.filename
      f = open(self.filename)
      for linea in f:
        parametros.append(linea)

      f.close()

      x = random.randrange(len(parametros))

      parametro = parametros[x]

      num_soli = int(self.entry3.get_text())
      
      self.avance_barra = int(100/num_soli)
      
      concurrentes = int(self.entry2.get_text())

      rafagas = int(num_soli/concurrentes)

      print("Rafagas: ",rafagas)

      for j in range(rafagas):
        for i in range(num_soli):
          self.avance_actual += self.avance_barra
          t = threading.Thread(target=self.crear_solicitud, args = (parametro,))
          t.start()

      self.resumen.set_text("Hora inicio: "+self.hora_inicio+"\nHora fin: "+str(datetime.datetime.now()))
      self.hora_fin = str(datetime.datetime.now())


    def crear_solicitud(self, parametro):
      alias = "" 
      categoria = "" 
      nombre = "" 
      txt = ""


      x = parametro.split(';')
      
      val = 0

      for i in x:
        if(val == 0):
          #print("usuario:",i)
          user = i.split("=")
          alias = user[1]
        elif(val == 1):
          #print("nombre:",i)
          name = i.split("=")
          nombre = name[1]
        elif(val == 2):
          #print("texto: ",i)
          text = i.split("=")
          cat = text[1].split("#")
          txt = text[1]
          categoria = cat[1]

        val = val + 1



      url = self.entry.get_text()


      #print(url)
      #print(alias,categoria,txt,nombre)

      data = {
      "alias": alias,
      "categoria": categoria,
      "txt": txt,
      "nombre": nombre,
      }

      
      #response = requests.get('https://google.com/',timeout=float(self.entry4.get_text()))

      response = requests.post(url, data = data,timeout = float(self.entry4.get_text()))
      respuesta = response.json()
      print respuesta["respuesta"]
      

      if(respuesta["respuesta"] == 1):
        self.exitosas = self.exitosas + 1
      else:
        self.perdidas = self.perdidas + 1
      

      


    def on_timeout(self, user_data):
        self.resumen.set_text("Hora inicio: "+self.hora_inicio+"\nHora fin: "+self.hora_fin+ "\nExitosas: "+str(self.exitosas)+"\nPerdidas: "+str(self.perdidas))
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.avance_actual

            if new_value > 100:
                new_value = 0

            self.barra.set_value(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True

window = LabelWindow()        
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()