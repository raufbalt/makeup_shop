from decouple import config

from twilio.rest import Client

account_sid = config('Account_sid', cast=str)
auth_token = config('Twilio', cast=str)
client = Client(account_sid, auth_token)

def whatsapp_message(name, last_name, phone_number, address, inform, product, quantity, price):

  message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f'Заказ от: {name} {last_name}\nНомер телефона: {phone_number}\nАдрес: {address}\nЗаказ: {product}\n'
         f'Количество:{quantity}\nИтоговая цена:{price}\nКомментарий:{inform}',
    to='whatsapp:+996553937937'
  )

  return message.sid
