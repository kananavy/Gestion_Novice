from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import pymysql
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import pathlib
from tkinter import filedialog 
import os
import mysql.connector
import shutil

class Etudiant():
    def __init__(self,root):
        self.root = root
        self.root.title("Inscription")
        self.root.geometry("1920x1080+0+0")

        # Formulaire
        Gestion_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        Gestion_Frame.place(x=10, y=0, width=550, height=700)
        
#==========================================VARIABLE==========================#

        # les variables
        self.id = StringVar()
        self.nom = StringVar()
        self.prenom = StringVar()
        self.sexe = StringVar()
        self.adresse = StringVar()
        self.contact = StringVar()
        self.filiere = StringVar()
        self.niveau = StringVar()
        self.origine=StringVar()
        self.filename=StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()
 


        gestion_title = Label(Gestion_Frame, text="Information de Novice", font=("times new roman", 30, "bold"),
                              bg="cyan")
        gestion_title.place(x=100, y=10)
        gestion_title = Label(Gestion_Frame, text="ACUMg", font=("times new roman", 30, "bold"),
                              bg="cyan")
        gestion_title.place(x=200, y=50)
        gestion_title = Label(Gestion_Frame, text="Aumonerie Catholique Universitaire de Mahajanga", font=("times new roman", 15, "bold"),
                              bg="cyan")
        gestion_title.place(x=40, y=100)

#==========================================FORMULAIRE==========================#
        # ID
        id_compt = Label(Gestion_Frame, text="ID", font=("times new roman", 20), bg="cyan")
        id_compt.place(x=50, y=160)

        id_txt = Entry(Gestion_Frame, textvariable=self.id, font=("times new roman", 20), bg="lightgray")
        id_txt.place(x=220, y=160, width=50)

        # Nom Complet
        idcomplete = Label(Gestion_Frame, text="Nom Complet", font=("times new roman", 20), bg="cyan")
        idcomplete.place(x=50, y=210)

        nom_txt = Entry(Gestion_Frame, textvariable=self.nom, font=("times new roman", 20), bg="lightgray")
        nom_txt.place(x=220, y=210)

        # Prenom
        prenomcomplet = Label(Gestion_Frame, text="Prenom", font=("times new roman", 20), bg="cyan")
        prenomcomplet.place(x=50, y=260)

        prenom_txt = Entry(Gestion_Frame, textvariable=self.prenom, font=("times new roman", 20), bg="lightgray")
        prenom_txt.place(x=220, y=260)

        # Sexe
        Sexe = Label(Gestion_Frame, text="Sexe", font=("times new roman", 20), bg="cyan")
        Sexe.place(x=50, y=310)

        sexe_txt = Entry(Gestion_Frame, textvariable=self.sexe, font=("times new roman", 20),bg="lightgray")
        sexe_txt.place(x=220, y=310, width=285)


        # Adresse
        Adresse = Label(Gestion_Frame, text="Adresse", font=("times new roman", 20), bg="cyan")
        Adresse.place(x=50, y=360)

        adresse_txt = Entry(Gestion_Frame,textvariable=self.adresse, font=("times new roman", 20), bg="lightgray")
        adresse_txt.place(x=220, y=360, width=285)

        # Contact
        contact = Label(Gestion_Frame, text="Contact", font=("times new roman", 20), bg="cyan")
        contact.place(x=50, y=410)

        contact_txt = Entry(Gestion_Frame, textvariable=self.contact, font=("times new roman", 20), bg="lightgray")
        contact_txt.place(x=220, y=410)

        # Filiere
        filiere = Label(Gestion_Frame, text="Filiere", font=("times new roman", 20), bg="cyan")
        filiere.place(x=50, y=460)

        filiere_txt = Entry(Gestion_Frame, textvariable=self.filiere, font=("times new roman", 20), bg="lightgray")
        filiere_txt.place(x=220, y=460)
        
        # Niveau
        Niveau = Label(Gestion_Frame, text="Niveau", font=("times new roman", 20), bg="cyan")
        Niveau.place(x=50, y=510)

        Nivau_txt = Entry(Gestion_Frame, textvariable=self.niveau, font=("times new roman", 20), bg="lightgray")
        Nivau_txt.place(x=220, y=510)
        
        # Origine
        Origine = Label(Gestion_Frame, text="Origine", font=("times new roman", 20), bg="cyan")
        Origine.place(x=50, y=560)

        Origine_txt = Entry(Gestion_Frame, textvariable=self.origine, font=("times new roman", 20), bg="lightgray")
        Origine_txt.place(x=220, y=560)


#==========================================BUTON==========================#


        # Buton Ajouter
        btn_Ajouter = Button(Gestion_Frame, command=self.ajou_etudiant, text="Ajouter", font=("times new roman", 15),
                             bd=10, relief=GROOVE, bg="green")
        btn_Ajouter.place(x=5, y=615, width=100)

        # Buton Modifier
        btn_modifier = Button(Gestion_Frame , command=self.modifier,text="Modifier", font=("times new roman", 15), bd=10, relief=GROOVE,
                              bg="yellow")
        btn_modifier.place(x=130, y=615, width=100)

        # Supprimer
        btn_nouvelle = Button(Gestion_Frame, command=self.supprimer, text="Supprimer", font=("times new roman", 15), bd=10, relief=GROOVE,
                               bg="red")
        btn_nouvelle.place(x=400, y=615, width=100)

        # Buton Renitialiser
        btn_renitialiser = Button(Gestion_Frame, text="Rénitialier", command=self.reini, font=("times new roman", 15), bd=10,relief=GROOVE, bg="gray")
        btn_renitialiser.place(x=260, y=615, width=100)

        # Recherche
        self.Detais_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="cyan")
        self.Detais_Frame.place(x=600, width=745, height=700)

        Affichage_resultat = Label(self.Detais_Frame, text="Rechercher par", font=("times new roman", 15, "bold"), bg="cyan")
        Affichage_resultat.place(x=10, y=50)

        rech = ttk.Combobox(self.Detais_Frame, textvariable=self.recherche_par, font=("times new roman", 20),state="readonly")
        rech["values"] = ("id","nom","prenom","sexe","adresse", "contact","filiere","niveau","origine")
        rech.place(x=150, y=45, width=110, height=40)
        rech.current(0)

        rech_txt = Entry(self.Detais_Frame, textvariable=self.recherche, font=("times new roman", 20), bd=5, relief=GROOVE)
        rech_txt.place(x=270, y=45, width=160, height=40)

        btn_rech = Button(self.Detais_Frame, command=self.rechercher_info, text="Rechercher", font=("times new roman", 13), bd=8, bg="gray",
                          relief=GROOVE)
        btn_rech.place(x=450, y=45, width=125, height=40)

        btn_afftou = Button(self.Detais_Frame,command=self.afficherRechertat, text="Afficher Tous", font=("times new roman", 13), bd=8, bg="gray",
                            relief=GROOVE)
        btn_afftou.place(x=600, y=45, width=125, height=40)
        
        #Btn
        
        file = Button(self.Detais_Frame, text="File", font=("times new roman", 15),command=self.get_image ,bd=5,
                        bg="#5789b0",activebackground="#5789b0")
        file.place(x=300, y=610, width=100)
    
    
     
        
        
#==========================================AFFICHAGE==========================#



    #Affichage
        result_Frame = Frame(self.Detais_Frame, bd=5, relief=GROOVE, bg="cyan")
        result_Frame.place(x=5, y=110, width=730, height=250)
        self.tabl_result = ttk.Treeview(result_Frame,
                                        columns=("id","nom", "prenom", "sexe", "adresse", "contact", "filiere", "niveau", "origine"))

        self.tabl_result.heading("id", text="ID")
        self.tabl_result.heading("nom", text="Nom Complet")
        self.tabl_result.heading("prenom", text="Prenom")
        self.tabl_result.heading("sexe", text="Sexe")
        self.tabl_result.heading("adresse", text="Adresse")
        self.tabl_result.heading("contact", text="Contact")
        self.tabl_result.heading("filiere", text="Filiere")
        self.tabl_result.heading("niveau", text="Niveau")
        self.tabl_result.heading("origine", text="Origine")

        self.tabl_result["show"] = "headings"

        self.tabl_result.column("id", width=30)
        self.tabl_result.column("nom", width=130)
        self.tabl_result.column("prenom", width=100)
        self.tabl_result.column("sexe", width=40)
        self.tabl_result.column("adresse", width=85)
        self.tabl_result.column("contact", width=80)
        self.tabl_result.column("filiere", width=90)
        self.tabl_result.column("niveau", width=55)
        self.tabl_result.column("origine", width=120)

        self.tabl_result.pack()
        
        self.afficherRechertat()

        self.tabl_result.bind("<ButtonRelease-1>", self.information)
        
        
        #image😀😀😀😀😀
        # self.canvas = Canvas(self.Detais_Frame, relief=GROOVE,border=0,width=199,height=199)
        
        self.canvas = Canvas(self.Detais_Frame, relief=GROOVE,border=0,width=199,height=199)
        self.canvas.place(x=250, y=400 )
        
    def reinit_canvas(self):
        self.canvas = Canvas(self.Detais_Frame, relief=GROOVE,border=0,width=199,height=199)
        self.canvas.place(x=250, y=400 )
        
    def get_image(self, evt=None):
        selected_file = filedialog.askopenfilename(title="Select image file",filetype=(("JPG file","*.jpg"), ("PNG file","*.png"),("ALL file",".*")),initialdir=os.getcwd())
        if selected_file:
            dest = "./Images_set/"
            self.filename.set(shutil.copy2(selected_file, dest))
            self.change_image()
       
    def change_image(self):
        if self.filename.get() == "":
            self.reinit_canvas()
            return
        i = self.on_set_image(self.filename.get())
        self.canvas.create_image(100, 100, image=i)
        self.canvas.image = i
  
    def on_set_image(self, filename):
        image = Image.open(filename)
        # if you resize...
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)        
    
#==========================================FUNCTION==========================#

    #add
    
    def ajou_etudiant(self):
        if self.nom.get() == "" or self.prenom.get() == "":
            messagebox.showerror("Erreur", "Vous n'avez pas rempli les champs obligatoires", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="creer")
                cur = con.cursor()
                # cur.execute("INSERT INTO inscrietudiant values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id.get(),self.nom.get(),self.prenom.get(),self.sexe.get(),self.adresse.get(),self.contact.get(),self.filiere.get(),self.niveau.get(),self.origine.get(),self.filename))
                cur.execute("INSERT INTO inscrietudiant values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id.get(),self.nom.get(),self.prenom.get(),self.sexe.get(),self.adresse.get(),self.contact.get(),self.filiere.get(),self.niveau.get(),self.origine.get(),self.filename.get()))
                con.commit()
                self.afficherRechertat()
                self.reini()
            except:
                messagebox.showinfo("Succses", "Enregistre Effectué")
            con.close()
    #set
           
    def afficherRechertat(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="creer")
        cur = con.cursor()
        cur.execute("SELECT id,nom,prenom,sexe,adresse,contact,filiere,niveau,origine,photo FROM inscrietudiant")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_result.delete(*self.tabl_result.get_children())
  
            for row in rows:
                self.tabl_result.insert("", END, values=row)
            
        con.commit()
        con.close()
        

        
    #clear 
    def reini(self):
        self.id.set("")
        self.nom.set("")
        self.prenom.set("")
        self.sexe.set("")
        self.adresse.set("")
        self.contact.set("")
        self.filiere.set("")
        self.niveau.set("")
        self.origine.set("")
        self.filename.set("")
        self.change_image()
        
        
       #information 
    def information(self,ev):
        Cursor_row = self.tabl_result.focus()
        contents = self.tabl_result.item(Cursor_row)
        row = contents["values"]

        self.id.set(row[0]),
        self.nom.set(row[1]),
        self.prenom.set(row[2]),
        self.sexe.set(row[3]),
        self.adresse.set(row[4]),
        self.contact.set(row[5]),
        self.filiere.set(row[6]),
        self.niveau.set(row[7]),
        self.origine.set(row[8]),
        self.filename.set(row[9]),
        self.change_image()
        
        
    #remove
    def modifier(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="creer")
        cur = con.cursor()
        cur.execute("UPDATE inscrietudiant SET nom=%s,prenom=%s,sexe=%s,adresse=%s,contact=%s,filiere=%s,niveau=%s,origine=%s,photo=%s WHERE id=%s",(self.nom.get(),self.prenom.get(),self.sexe.get(),self.adresse.get(),self.contact.get(),self.filiere.get(),self.niveau.get(),self.origine.get(),self.filename,self.id.get()))
        # cur.execute("UPDATE inscrietudiant SET nom=%s,prenom=%s,sexe=%s,adresse=%s,contact=%s,filiere=%s,niveau=%s,origine=%s WHERE id=%s",(self.nom.get(),self.prenom.get(),self.sexe.get(),self.adresse.get(),self.contact.get(),self.filiere.get(),self.niveau.get(),self.origine.get(),self.id.get()))
        messagebox.showinfo("Succses", "Modification Effectuer")
        con.commit()
        self.afficherRechertat()
        self.reini()
        con.close()
       
    #delete
    def supprimer(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="creer")
        cur = con.cursor()
        os.remove(self.filename.get())
        cur.execute("DELETE FROM inscrietudiant WHERE id =%s", self.id.get())
        con.commit()
        messagebox.showinfo("Succses", "Suppresion Effectuer")
        self.afficherRechertat()
        self.reini()
        con.close()


    #cherche_info
    
    def rechercher_info(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="creer")
        cur = con.cursor()
        var="SELECT * FROM inscrietudiant WHERE "+str(self.recherche_par.get())+" like '%"+str(self.recherche.get())+"%'"
        print(var)
        cur.execute(var)
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_result.delete(*self.tabl_result.get_children())
            for row in rows:
                self.tabl_result.insert("", END, values=row)
        con.commit()
        con.close()
       
#file_img
    def showimg(self, event):
        # self.filename=filedialog.askopenfile(title="Select image file",filetype=(("JPG file","*.jpg"), ("PNG file","*.png"),("ALL file","*.txt")),initialdir=os.getcwd())
        self.filename=filedialog.askopenfilename(title="Select image file",filetype=(("JPG file","*.jpg"), ("PNG file","*.png"),("ALL file",".*")),initialdir=os.getcwd())
        
        if self.filename =="":
            pass
        else:                                                                   
            self.imageicone = (on_set_image(self.filename))
            self.imageicone4=""
            print(self.imageicone)
            return ImageTk.PhotoImage(self.imageicone)
            lab=Label(self.upade_btn,image=self.imageicone,height=200,width=200)
            lab.place(x=0,y=0)
                
root = Tk()
obj = Etudiant(root)
root.mainloop()
