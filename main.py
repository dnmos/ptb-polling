import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from data import config, messages


logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO
)


def posts_params_func():
  """Return json with PDF list"""
  with open('../webpdf/posts_params.json', 'r') as file:
    result_json = json.load(file)

  return result_json


def get_text_services(messages):
  text_services = ""
  for link in messages.LINKS:
    service = messages.LINKS[link]["text"]
    url = messages.LINKS[link]["url"]
    text_services += f"{service} <a href='{url}'>{link}</a>\n\n"
  return text_services


async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text=messages.TEXT_START,  
                                 parse_mode="HTML", 
                                 disable_web_page_preview=True)


async def command_services(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text_services = get_text_services(messages)
  await context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text=text_services,  
                                 parse_mode="HTML", 
                                 disable_web_page_preview=True)


async def command_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
  """PDF Command send posts PDF list"""
  posts_params = posts_params_func()
  text_posts = messages.TEXT_PDF
  for post in posts_params:
    title = posts_params[post]['title']
    command = post.replace('-', '_')
    text_posts = text_posts + title + '\n' + f' /{command}\n\n' 
  await context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text=text_posts,  
                                 parse_mode="HTML", 
                                 disable_web_page_preview=True)


async def command_other(update: Update, context: ContextTypes.DEFAULT_TYPE):
  """Send PDF"""
  text = update.message.text
  chat_id = update.message.chat.id 
  msg_id = update.message.message_id
  userid = update.message.from_user.id
  username = update.message.from_user.username
  userfullname = update.message.from_user.full_name
  posts_params = posts_params_func()
  for post in posts_params:
    command = post.replace('-', '_')
    if text == f"/{command}":
      await context.bot.send_document(chat_id=update.effective_chat.id, 
                                      document=open(f"../webpdf/pdf/{post}.pdf", "rb"))


def main():
  application = ApplicationBuilder().token(config.TOKEN).build()
  
  application.add_handler(CommandHandler('start', command_start))
  application.add_handler(CommandHandler('services', command_services))
  application.add_handler(CommandHandler('pdf', command_pdf))

  pdfs = []
  posts_params = posts_params_func()
  for post in posts_params:
    command = post.replace('-', '_')
    pdfs.append("/" + command)
  application.add_handler(MessageHandler(filters.Text(pdfs), command_other))

  application.run_polling()


if __name__ == '__main__':
  main()