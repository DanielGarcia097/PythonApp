import gtk
class packing:
	def __init__(self):
 		window = gtk.Window()
		window.connect("destroy",self.quit)
 		window.set_title("Empacado de widgets")
 		window.set_border_width(6)
 		window.set_default_size(400,200)
 		Vbox = gtk.VBox()
		window.add(Vbox)
 		hbox1 = gtk.HBox()
 		Vbox.pack_start(hbox1,True,False,0)
		button1 = gtk.Button("Button1")
		button1.connect("clicked",self.on_clicked_button)
		hbox1.pack_start(button1,False,False,2)
		button2 = gtk.Button("Button2")
		button2.connect("clicked",self.on_clicked_button)
		hbox1.pack_start(button2,True,False,2)
		button3 = gtk.Button("Button3")
		button3.connect("clicked",self.on_clicked_button)
		hbox1.pack_start(button3,False,True,2)
		button4 = gtk.Button("Button4")
		button4.connect("clicked",self.on_clicked_button)
		hbox1.pack_start(button4,True,True,2)
		hbox2 = gtk.HBox(True)
		Vbox.pack_start(hbox2,True,True,0)
		button5 = gtk.Button("Button5")
		button5.connect("clicked",self.on_clicked_button)
		hbox2.pack_end(button5,False,False,2)
		button6 = gtk.Button("Button6")
		button6.connect("clicked",self.on_clicked_button)
		hbox2.pack_end(button6,True,False,2)
		button7 = gtk.Button("Button7")
		button7.connect("clicked",self.on_clicked_button)
		hbox2.pack_end(button7,False,True,2)
		button8 = gtk.Button("Button8")
		button8.connect("clicked",self.on_clicked_button)
		hbox2.pack_end(button8,True,True,2)
		close = gtk.Button("",gtk.STOCK_CLOSE)
		close.connect("clicked",self.quit)
		Vbox.pack_start(close,True,True,6)
		window.show_all()

		def quit(self,window):
			gtk.main_quit()
		
		def on_clicked_button(self,widget):
			text = widget.get_label()
			print "%s ha sido presionado"%text

		
gtk.main()
