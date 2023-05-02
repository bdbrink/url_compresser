import random
import string

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
shorten_urls = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))