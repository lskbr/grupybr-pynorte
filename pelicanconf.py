#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'Python Norte'
AUTHOR = u'PyNorte'
THEME = "themes/malt"
MALT_BASE_COLOR = "blue-grey"


META_DESCRIPTION = '''O PyNorte é um grupo de usuários (profissionais e
                      amadores) da linguagem Python, onde prezamos pela troca de
                      conhecimento, respeito mútuo e diversidade (tanto de opinião
                      quanto de tecnologias).'''

META_KEYWORDS = ['pynorte', 'python', 'amazonas', 'desenvolvimento',
                 'acre', 'para', 'tocantins', 'rondonia', 'roraima', 'amapa']

# Referências à Github
GITHUB_REPO = "https://github.com/lskbr/grupybr-pynorte"
GITHUB_BRANCH = "master"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python do Norte do Brasil."
SITE_BACKGROUND_IMAGE = "images/banners/background.png"
FOOTER_ABOUT = "O Grupo Python Norte é uma comunidade de usuários do Acre, Amazonas, Pará, Rondônia, Roraima, Amapá e Tocantins"

# Tema do Syntax Hightlight
PYGMENTS_STYLE = "perldoc"

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    # {
    #     "title": "Comunidade",
    #     "href": "comunidade",
    # },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "https://telegram.me/joinchat/COYq6QM8RkebVUVK1WxRHQ",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
    {
        "href": "https://groups.google.com/d/forum/pynorte",
        "icon": "fa-envelope",
        "text": "Lista de e-mail",
    },
    {
        "href": "https://github.com/grupydf",
        "icon": "fa-github",
        "text": "Grupy-DF",
    },
    {
        "href": "http://wiki.python.org.br/",
        "icon": "fa-globe",
        "text": "Python Brasil",
    },
    {
        "href": "https://python.org",
        "icon": "fa-globe",
        "text": "Python",
    },
    {
        "href": "http://www.pythonclub.com.br/",
        "icon": "fa-globe",
        "text": "PythonClub",
    },
    {
        "href": "http://dojoto.info/",
        "icon": "fa-globe",
        "text": "CodingDojoTocantins"
    },
)

# Membros do Grupy
MEMBROS = OrderedDict((
    ("Nilo Menezes", {
        "twitter": "@lskbr",
        "github": "lskbr",
        "site": {
                 "nome": "Nilo Menezes",
                 "href": "http://www.nilo.pro.br",
                }
        }),
    ("Adriano Praia", {
           "github": "adrianopraia",
        }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade PyNorte se comunica através de mailing " +\
                    "lists, grupo no telegram e ocasionalmente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em>, hangouts e palestras. ",
                # "buttons": [
                #     {
                #         "text": "Saiba Mais",
                #         "href": "comunidade",
                #     },
                # ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade PyNorte inicia sua organização, mas já possui alguns " +\
                        "colaboradores, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Entre em Contato",
                "icon": "fa-paper-plane",
                "text": "Deseja participar? Sugerir uma atividade ou simplesmente acompanhar o grupo?"
                        " Contacte-nos via Telegram.",
                "buttons": [
                    {
                        "text": "Telegram",
                        "href": "https://telegram.me/joinchat/COYq6QM8RkebVUVK1WxRHQ",
                    },
                           ]
            },
            # {
            #     "title": "Projetos",
            #     "icon": "fa-briefcase",
            #     "text": " Atualmente o PyNorte possui poucos projetos em andamento:" +\
            #             "Traduções do Django-docs e Python on Campus.",
            #     "buttons": [
            #         {
            #             "text": "Mais detalhes",
            #             "href": "projetos",
            #         },
            #     ],
            # },
        ]
    },
    # {
    #     "color": "blue-grey lighten-4",
    #     "title": "Nosso Projetos",
    #     "items": [
    #         {
    #         "title": "MIG-29",
    #         "icon": "fa-fighter-jet",
    #         "text": "MIG-29 é um caça Russo cujo projeto original visava" +\
    #                 "superar o F-22 Raptor",
    #         "buttons": [
    #                 {
    #                     "text": "Código Fonte",
    #                     "href": "#",
    #                 },
    #                 {
    #                     "text": "Wiki",
    #                     "href": "#",
    #                 },
    #             ]
    #         },
    #         {
    #         "title": "SNES",
    #         "icon": "fa-gamepad",
    #         "text": "O Super Nintendo Entertainment Systems visa superar" +\
    #                 "o sucesso de seu antecessor, o NES.",
    #         "buttons": [
    #                 {
    #                     "text": "Site",
    #                     "href": "#",
    #                 },
    #                 {
    #                     "text": "Comprar",
    #                     "href": "#",
    #                 },
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "color": "blue-grey lighten-5",
    #     "title": "Entre em Contato",
    #     "items": [
    #         {
    #         "title": "",
    #         },
    #         {
    #         "icon": "fa-envelope",
    #         "buttons": [
    #                 {
    #                     "text": "Envie um e-mail!",
    #                     "href": "#",
    #                 },
    #             ]
    #         }
    #     ]
    # }
    ]

from themes.malt.functions import *
