#!/data/data/com.termux/files/usr/bin/python

#XXX: EDITING THE SCRIPT CAN DAMAGE YOUR ID

# [[[CODE BY MOSHEUR RAHMAN]]]

# REPORT ERROR:::::::

# EMAIL : mosheur.rahman.15@gmail.com
# FACEBOOK : https://www.facebook.com/mosheur.rahman.anik

import sys, time, smtplib, socket, os

banner = """

    _ ___    __ _
|V||_| | |  |_ |_)
| || |_|_|__|__| \
v.1.0.1

AUTHOR:mosheur_rahman!

"""

gmail = ['smtp.gmail.com',587]
yahoo = ['smtp.mail.yahoo.com',587]
outlook = ['smtp-mail.outlook.com',587]

help = """
mailer is a script for sending email from comand line!

specaly desined for termux !

type 'mailer' for run it !

or use command line arguments !

arguments list:

[-i] = used to put user email id!

[-p] = used to  put user email password!

[-t] = used to put target mail address!

[-m] = used to put  the message to send!

[-sn]= used to put the smtp server address of user!

[-sp]= usee to put the smtp server port of user !

"""
def main (id, pas, target, msg, ser_name, ser_port):
	"""
	EMAIL CLIENT SIDE FUNCTION

	"""
	try:
		os.system('clear')
		writer (banner)
		writer (f'\nconnecting with {ser_name}\n')
		client = smtplib.SMTP(ser_name,ser_port)
		writer (f'\nconneted with {ser_name}\n')
		writer ('\nchacking connection power...\n\n')
		client.ehlo()
		writer ('\n\nchacked\n')
		writer (f'\nstarting TLS incription at {ser_name}\n')
		client.starttls()
		writer (f'\nincription started at {ser_name}\n')
		writer (f'\nlogging in {id}\n')
		client.login(id, pas)
		writer (f'\nsucsessfuly loged in {id}\n')
		writer ('\nsending mail\n')
		client.sendmail(id, target, msg)
		writer ('\nmail sent\n')
		writer ('\nclosing connection \n')
		client.quit()
		writer ('\ncolsed\n')

	except socket.gaierror:
		writer ('no internet')
	except smtplib.SMTPAuthenticationError:
		writer ('email/pass error')
	except smtplib.SMTPServerDisconnected:
		writer ('server disconnected')


def writer (data):
	"""
	DATA WRITER
	"""
	for content in data:
		sys.stdout.write(content)
		time.sleep(0.01)
		sys.stdout.flush()


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
			return 'not found'
	else:
		writer ('\ninvalid address..\n')
		sys.exit(0)

def input_handler ():

	"""
	INPUT TAKER FOR RUNTIME
	"""
	try:
		os.system('clear')
		writer (banner)
		writer ('\nenter your email address:\n')
		id = input ('\n>> ')
		writer (f'\nenter password for {id}\n')
		pas = input ('\n>> ')
		writer ('\nenter target email address:\n')
		target = input ('\n>> ')
		writer ('\nenter your message :\n')
		msg = input ('\n>> ')
		id_chack = service_handler (id)
		if id_chack == 'not found':
			writer (f'\n please use castom\n')
			writer ('\nenter your service smtp address:\n')
			ser_name = input ('\n>> ')
			writer (f'\nenter port for {ser_name}\n')
			ser_port = input ('\n>> ')
			main (id, pas, target, msg, ser_name, ser_port)
		else:
			(ser_name, ser_port) = id_chack
			main (id, pas, target, msg, ser_name, ser_port)
	except KeyboardInterrupt:
		writer ('\ncanceled by user\n')
		sys.exit(0)
	except EOFError:
		writer ('\ncanceled by user\n')
		sys.exit(0)

	else:
		pass

def cmd_argv_handler ():

	"""
	SYSTEM ARGUMENTS HANDLER

	"""

	try:

		argv = sys.argv
		o = 0
		id = ''
		pas = ''
		target = ''
		msg = 'mailer has you'
		ser_name = ''
		ser_port = ''
		for i in argv:
			if i == '-i':
				id = argv[o+1]
				o = o + 1
			elif i == '-p':
				pas = argv[o+1]
				o = o + 1
			elif i == '--help':
				writer (help)
				sys.exit(0)
			elif i == '-t':
				target = argv[o+1]
				o = o + 1
			elif i == '-m':
				msg = argv[o+1]
				o = o + 1
			elif i == '-sn':
				ser_name = argv[o+1]
				o = o + 1
			elif i == '-sp':
				ser_port = argv[o+1]
				o = o + 1
			else:
				o = o + 1
		if id == '' or pas == '' or target == '':
			writer ('\ninvalid option \n\ntype --help for help\n')
			sys.exit(0)
		elif ser_name == '' or ser_port == '':
			s = service_handler(id)
			if s == 'not found':
				writer ('\nenter server address manualy:\n')
				ser_name = input ('\n>> ')
				writer ('\nenter port:\n')
				ser_port = input ('\n>> ')
			else:
				ser_name,ser_port = s
		else:
			writer ('\error to send mail\n')
		main(id,pas,target,msg,ser_name,ser_port)
	except IndexError:
		writer ('\nif your arguments have special char please write them under ""\n')
	else:
		pass



if __name__=='__main__':
	a = 0
	for i in sys.argv:
		a = a + 1
	if a>1:
		cmd_argv_handler()
	else:
		input_handler()


