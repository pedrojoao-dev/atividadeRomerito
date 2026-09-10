from flask import Flask, render_template, request, redirect, url_for, session, Blueprint


auth_bp = Blueprint("auth", __name__, template_folder="templates")

