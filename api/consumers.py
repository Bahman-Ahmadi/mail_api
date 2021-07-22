from channels.generic.websocket import WebsocketConsumer

class AppConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		self.send(text_data="Welcome!")

	def disconnect(self, close_code):
		pass

	def receive(self, text_data):
		keys,values = [i.split("=")[0] for i in text_data.split("/")[-1][1:].split("&")], [j.split("=")[1] for j in text_data.split("/")[-1][1:].split("&")]
		my_mail,my_pass,to_mail,subject_mail,text_mail=values[keys.index("my_mail")],values[keys.index("my_pass")],values[keys.index("to_mail")],values[keys.index("subject_mail")],values[keys.index("text_mail")]
		import ssl, smtplib
		port = 465
		message = "Subject: {}\n\n{}".format(subject_mail, text_mail)
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
			server.login(my_mail,my_pass)
			server.sendmail(my_mail, to_mail, message)