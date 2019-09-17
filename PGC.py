from requests import Session
from hashlib import sha256
from json import loads, dumps
import smtplib

def sendMail(gmail_login, gmail_passowrd, recepient_address):
	s = smtplib.SMTP("smtp.gmail.com", 587)
	s.starttls()
	s.login(gmail_login, gmail_passowrd)
	s.sendmail(
		gmail_login,
		recepient_address,
		"Subject: Grades\n\nI felt a great disturbance in the force.\nGo check https://pamplemousse.ensae.fr/index.php?p=105"
	)
	s.quit()

config = loads(open("config.json").read())

data = {
	"sph_username":config["pamp_username"],
	"sph_password":config["pamp_password"]
}

if not(config["old_hash"]):
	with Session() as s:
		s.post("https://pamplemousse.ensae.fr/site_publishing_helper/login_check/0", data=data)
		response = s.get("https://pamplemousse.ensae.fr/index.php?p=105")
		old_grades = response.text
		hash = sha256(old_grades.encode("utf8")).hexdigest()
		config["old_hash"] = hash
		open("config.json","w").write(dumps(config))
		s.close()

with Session() as s:
	s.post("https://pamplemousse.ensae.fr/site_publishing_helper/login_check/0", data=data)
	response = s.get("https://pamplemousse.ensae.fr/index.php?p=105")
	new_grades = response.text
	hash = sha256(new_grades.encode("utf8")).hexdigest()
	if hash != config["old_hash"]:
		config["old_hash"] = hash
		open("config.json","w").write(dumps(config))
		sendMail(config["gmail_login"], config["gmail_password"],config["recepient_address"])
	s.close()
