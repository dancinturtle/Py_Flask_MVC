from flask import Flask, render_template, redirect, request

class Welcome:
    """Welcome Controller"""

    def index(app):
        return render_template("welcome.html")