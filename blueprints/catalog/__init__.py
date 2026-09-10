from flask import Flask, render_template, request, redirect, url_for, session, Blueprint

reviews_bp = Blueprint("reviews", __name__,template_folder="templates")