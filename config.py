# config.py

import os

# main information
main = {
    "author"    : "Albert Szadziński",
    "version"   : "v3.3",
    "domain"    : "https://fenu-exp.us.edu.pl",
    "internal"  : "https://fenu-experiment.pl/",
    "repo"      : "https://github.com/aszadzinski/BINA-CCB.git",
    "tags"      : "BINA, BINA detector, 3nf, space star, CCB, bronowice, nuclear forces, UŚ, UJ, IFJ PAN, experiments, 3-nucleon forces, breakup, elastic scattering, few nucleon systems",
    }
languages = ["en","pl"]

# Internal config
PHOTOS_TYPE = ["BINA_window","Schemes", "Detector", "Others", "Target", "Public", "Production", "Salad", "Plans", "Target_chamber"]
FORUM_CATEGORIES = {  "Information":["Announcements", "Bug Reports & Suggestions"],
                    "General":["Events", "Plans", "Orders"],
                    "Discussions":["Data Analysis", "Experiments", "Software"],
                    "Off-Topic":["General Discussions"]
                }
MEMBERS_GROUP = {  "sta"   : "Staff",
                    "phd"   : "PhD Students",
                    "stu"   : "Students",
                }

# Server config
ORIGINS = ["*"]
SECRET_KEY = "ad39defhkasdf0avfdsiav90AOD0DFs1"
PORT = 8000
DEBUG = True
TESTING = False
ENV = 'dev'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(basedir, 'database/sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = os.path.join('static', 'img')
HOMEPAGE_FOLDER = os.path.join(basedir, 'App/static/homepage')
REPOSITORY_FOLDER = os.path.join(basedir, 'App/static/repository')
