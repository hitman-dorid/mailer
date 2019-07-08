#!/data/data/com.termux/files/usr/bin/python

#XXX: EDITING THE SCRIPT CAN DAMAGE YOUR ID

# [[[CODE BY MOSHEUR RAHMAN]]]

# REPORT ERROR:::::::

# EMAIL : mosheur.rahman.15@gmail.com
# FACEBOOK : https://www.facebook.com/mosheur.rahman.anik
# GITHUB : https://github.com/hitman-dorid/mailer
import sys, time, smtplib, socket, os, argparse
from email.mime.text import MIMEText as txt
banner = """
\033[32m
    _ ___    __ _
|V||_| | |  |_ |_)
| || |_|_|__|__| \
v.1.0.1
\033[0m
AUTHOR:mosheur_rahman!

GITHUB:https://github.com/hitman-dorid/mailer

"""

gmail = ['smtp.gmail.com',587]
yahoo = ['smtp.mail.yahoo.com',587]
outlook = ['smtp-mail.outlook.com',587]

def main (id, pas, target, msg, ser_name, ser_port,spam):
	"""
	EMAIL CLIENT SIDE FUNCTION

	"""
	if spam:
		os.system('clear')
		writer (banner)
		for i in range (20):
			try:
				client = smtplib.SMTP(ser_name,ser_port)
				client.ehlo()
				client.starttls()
				client.login(id,pas)
				client.sendmail(id,target,msg)
				client.quit()
				writer (f'\n\033[32m[+] {i+1} msg sent\033[0m\n')
			except socket.gaierror:
				writer ('\n\033[31m\nno internet\n\033[0m')
				break
			except smtplib.SMTPAuthenticationError:
				writer ('\033[31m\nemail/pass error\n\033[0m')
				break
			except smtplib.SMTPServerDisconnected:
				writer ('\033[31m\nserver disconnected\n\033[0m')
				break
			except TypeError:
				writer ('\n\033[31mtype error! please chack your args\n\033[0m')
				break
			except KeyboardInterrupt:
				writer ('\033[31m\ncanceled by user\n\033[0m')
				break
			except EOFError:
				writer ('\033[31m\ncanceled by user\n\033[0m')
				break
	else:
		try:
			os.system('clear')
			writer (banner)
			writer (f'\033[32m\nconnecting with {ser_name}\n\033[0m')
			client = smtplib.SMTP(ser_name,ser_port)
			writer (f'\033[32m\nconneted with {ser_name}\n\033[0m')
			writer ('\033[32m\nchacking connection power...\n\n\033[0m')
			client.ehlo()
			writer ('\033[32m\n\nchacked\n\033[0m')
			writer (f'\033[32m\nstarting TLS incription at {ser_name}\n\033[0m')
			client.starttls()
			writer (f'\033[32m\nincription started at {ser_name}\n\033[0m')
			writer (f'\033[32m\nlogging in {id}\n\033[0m')
			client.login(id, pas)
			writer (f'\033[32m\nsucsessfuly loged in {id}\n\033[0m')
			writer ('\033[32m\nsending mail\n\033[0m')
			client.sendmail(id, target, msg)
			writer ('\033[32m\nmail sent\n\033[0m')
			writer ('\033[32m\nclosing connection \n\033[0m')
			client.quit()
			writer ('\033[32m\ncolsed\n\033[0m')

		except socket.gaierror:
			writer ('\n\033[31m\nno internet\n\033[0m')
		except smtplib.SMTPAuthenticationError:
			writer ('\033[31m\nemail/pass error\n\033[0m')
		except smtplib.SMTPServerDisconnected:
			writer ('\033[31m\nserver disconnected\n\033[0m')
		except TypeError:
			writer ('\n\033[31mtype error! please chack your args\n\033[0m')

		except KeyboardInterrupt:
			writer ('\033[31m\ncanceled by user\n\033[0m')
		except EOFError:
			writer ('\033[31m\ncanceled by user\n\033[0m')


def writer (data):
	"""
	DATA WRITER
	"""
	try:

		for content in data:
			sys.stdout.write(content)
			time.sleep(0.01)
			sys.stdout.flush()
	except KeyboardInterrupt:
		writer ('\033[31m\ncanceled by user\n\033[0m')
		sys.exit(0)
	except EOFError:
		writer ('\033[31m\ncanceled by user\n\033[0m')
		sys.exit(0)

def service_handler (service_name):
	"""
	SERVICE NAME FINDER
	"""

	if '@' in service_name:
		at_pos = service_name.find('@')
		name = service_name[at_pos+1:]
		print (name)
		if name == 'gmail.com':
			return gmail
		elif name == 'yahoo.com':
			return yahoo
		elif name == 'outlook.com':
			return outlook
		else:
			return None,None
	else:
		writer ('\ninvalid address..\n')
		sys.exit(0)

def input_handler ():

	"""
	INPUT TAKEING
	"""
	try:
		os.system('clear')
		writer (banner)
		writer ('\033[32m\nenter your email address:\n\033[0m')
		id = input ('\033[32m\n>> \033[0m')
		writer (f'\033[32m\nenter password for {id}\n\033[0m')
		pas = input ('\033[0m\n>> \033[0m')
		writer ('\033[32m\nenter target email address:\n\033[0m')
		target = input ('\033[32m\n>> \033[0m')
		writer ('\033[32m\nenter your message :\n\033[0m')
		msg = input ('\033[32m\n>> \033[0m')
		id_chack = service_handler (id)
		if id_chack == 'not found':
			writer ('\033[32m\n please use castom\n\033[0m')
			writer ('\033[32m\nenter your service smtp address:\n\033[0m')
			ser_name = input ('\033[32m\n>> \033[0m')
			writer (f'\033[32m\nenter port for {ser_name}\n\033[0m')
			ser_port = input ('\033[32m\n>> \033[0m')
			main (id, pas, target, msg, ser_name, ser_port)
		else:
			(ser_name, ser_port) = id_chack
			main (id, pas, target, msg, ser_name, ser_port)
	except KeyboardInterrupt:
		writer ('\033[31m\ncanceled by user\n\033[0m')
		sys.exit(0)
	except EOFError:
		writer ('\033[31m\ncanceled by user\n\033[0m')
		sys.exit(0)

	else:
		pass


def args ():

	"""
	COMMAND LINE ARGUMENT HANDLER!
	"""
	help_msg = """
	\n\n\033[32m
	mailer is a simple tool for sending email from
	command line...
	you can simply run it by "$ python mailer.py"!
	or use the command line arguments\n\n\033[0m
	"""

	par = argparse.ArgumentParser(description=help_msg)
	par.add_argument('-i','--id',type=str,metavar='',help='used to put user mail id\n')
	par.add_argument('-p','--pas',type=str,metavar='',help='used to put user passrord\n')
	par.add_argument('-t','--target',type=str,metavar='',help='used to put an target\n')
	par.add_argument('-m','--msg',type=str,metavar='',help='used to put the message\n')
	par.add_argument('-sra','--s_address',type=str,metavar='',help='used to given server address manualy name\n')
	par.add_argument('-srp','--s_port',type=str,metavar='',help='used to put port for manualy specified  address\n')
	par.add_argument('-sub','--subject',type=str,metavar='',help='used to put a subject')
	group = par.add_mutually_exclusive_group()
	group.add_argument('-sp','--spam',action='store_true',help='used for spamming')
	args = par.parse_args()
	return args.id,args.pas,args.target,args.msg,args.subject,args.s_address,args.s_port,args.spam


def sub_handler (msg,sub,id,target):

	"""
	HANDLING MESSAGE!
	"""
	if sub == None:
		sub = 'mailer has you'
	else:
		pass
	m = txt (msg)
	m['Subject'] = sub
	m['From'] = id
	m['To'] = target
	return m.as_string()

def arg_controler():

	"""
	PUTING ARGUMENTS AT THE RIGHT PLACE!
	"""
	id,pas,target,msg,sub,sa,sp,spam = args()
	if id ==None and pas==None and target == None and msg == None and sa == None and sp == None:
		input_handler()
		sys.exit(0)
	else:
		if id == None:
			print ('\n\033[31merror! required  user id\n\033[0m')
			sys.exit(0)
		elif pas == None:
			print ('\n\033[31merror! required  user pas\n\033[0m')
			sys.exit(0)
		elif target == None:
			print ('\n\033[31merror! required  a target id\n\033[0m')
			sys.exit(0)
		elif msg == None:
                        print ('\n\033[31merror! required  a messgae\n\033[0m')
                        sys.exit(0)
		elif sa == None or sp == None:
			sa,sp = service_handler(id)
			if sa == None and sp == None:
				writer ('\n\033[31mplz input the smtp details \n\033[0m')
				writer ('\033[32menter the smtp server address:\n\033[0m')
				sa = input ('\033[32m\n>> \033[0m')
				writer ('\n\033[32menter port:\n\033[0m')
				sp = input ('\033[32m\n>> \033[0m')
			else:
				pass
		msg = sub_handler (msg,sub,id,target)
		main (id,pas,target,msg,sa,sp,spam)
	sys.exit(0)

if __name__ == '__main__':

	arg_controler()
