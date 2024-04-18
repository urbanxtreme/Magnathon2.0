from tkinter import *
from tkinter import messagebox
import pymysql
import cryptography
def sign():
    root.destroy()
    import signin
def login_user():
    if self.username.get()=="" or self.password.get()=="":
        messagebox.showerror("Error","All fields are required to login")
class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        icon =PhotoImage(file="icon.png")
        root.iconphoto(True, icon)
        self.root.geometry("1920x1080+0+2")
        self.bg=PhotoImage(file="bg.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root, bg="lemon chiffon")
        Frame_login.place(x=500,y=200,width=500,height=400)
        title=Label(Frame_login,text="LOGIN MENU", font=("Impact",35,"bold","underline"),fg="yellow",bg="black")
        title.place(x=130, y=30)
        username = Label(Frame_login, text="E-mail:", font=("Algerian", 15), fg="navy",bg="alice blue")
        username.place(x=40, y=150)
        self.usernameentry= Entry(Frame_login, font=("Times New Roman", 15), fg="dark blue")
        self.usernameentry.place(x=160, y=150, width=300, height=26)
        password = Label(Frame_login, text="PASSWORD:", font=("Algerian", 15), fg="navy",bg="alice blue")
        password.place(x=40, y=230)
        self.passwordentry = Entry(Frame_login, font=("Times New Roman", 15), fg="dark blue")
        self.passwordentry.place(x=160, y=230, width=300, height=26)
        forgot_password = Button(Frame_login,cursor="hand2",command=self.forgotpswd, text="FORGOT PASSWORD?",bd=0, font=("Goudy old style", 10,"bold"), fg="saddle brown",bg="lemon chiffon")
        forgot_password.place(x=323, y=260)
        submit = Button(Frame_login,command=self.check_function,cursor="hand2", text="LOGIN", bd=0, font=("Bubbly", 15,"bold"), fg="white",bg="black", activebackground="magenta",activeforeground="black")
        submit.place(x=215,y=325)
        sign_inlabel = Label(Frame_login, text="Don't have an account?", font=("Open Sans", 9, "bold"), fg="navy",bg="lemon chiffon")
        sign_inlabel.place(x=150, y=370)
        sign_upbutton = Button(Frame_login, text="Sign In", font=("Open Sans", 9, "bold underline"),command=sign, bd=0,cursor="hand2", fg="blue", bg="lemon chiffon", activebackground="lemon chiffon",activeforeground="hot pink")
        sign_upbutton.place(x=285, y=370)
    def check_function(self):
        if self.usernameentry.get() == "" or self.passwordentry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="1234")
                mycursor = con.cursor()
                query = "USE handsign"
                mycursor.execute(query)
                con.commit()
                query = "SELECT * FROM data WHERE email=%s AND password=%s"
                mycursor.execute(query, (self.usernameentry.get(), self.passwordentry.get()))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    messagebox.showinfo("Welcome User", "Login Successful")
                    self.root.destroy()
            except pymysql.err.OperationalError as e:
                messagebox.showerror("Error", f"Connection failed: {e}", parent=self.root)
            finally:
                con.close()
    def forgotpswd(self):
        def fetch_password(email):
            try:
                connection = pymysql.connect(host='localhost',user='root',password='1234',database='handsign')
                cursor = connection.cursor()
                sql_query = "SELECT password FROM data WHERE email = %s"
                cursor.execute(sql_query, (email,))
                row = cursor.fetchone()
                cursor.close()
                connection.close()
                if row is None:
                    return None
                else:
                    return row[0]
            except pymysql.Error as e:
                print("Error:", e)
                return None
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        def send_email(subject, message, to_email):
            email = "skrhari2020@gmail.com"
            password = "aueq tfzq qypp sxee"
            sender_email = email
            receiver_email = to_email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
        # Prompt the user to enter email
        email = self.usernameentry.get()
        # Fetch password for the entered email
        password = fetch_password(email)
        # Check if password is fetched successfully
        if password is not None:
            print("Password fetched successfully.")
            print("Entered email:", email)
            print("Corresponding password:", password)
            a = email
            b = password
            subject = "kya huva tere password?"
            message = b
            to_email = a
            send_email(subject, message, to_email)
            messagebox.showinfo("Password Sent","Your password has been sent to your mail id")
        else:
            messagebox.showerror("Error","Email not registered, Sign-in to create an account")
root=Tk()
obj=Login(root)
root.mainloop()