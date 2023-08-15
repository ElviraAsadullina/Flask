# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template, request

app = Flask(__name__)

menu_items = [
    {'Главная': ['/']},
    {'Новости': ['/news']},
    {'Магазин': ['/marketplace']},
    {'О нас': ['/about']},
    {'Контакты': ['/contact']},
]


@app.route('/')
def index():
    title_html = 'Главная'
    content = ''
    return render_template('headers.html', menu_items=menu_items, current_path=request.path,
                           title=title_html, context=content)


@app.route('/news/')
def news():
    title_html = 'Свежие новости'
    site_news = [
        {'publish_date': '01.08.2023',
         'news_header': 'Как программисты пишут стихи',
         'news_anons': 'Программисты тоже любят поэзию, но у них свой особый стиль. '
                       'Они пишут стихи на разных языках программирования, используя синтаксис, '
                       'переменные и функции. Некоторые из них даже создают свои собственные языки для '
                       'поэтического творчества. В этом посте мы расскажем вам о самых интересных и оригинальных '
                       'примерах программистской поэзии.'},
        {'publish_date': '03.08.2023',
         'news_header': 'Почему программисты не любят понедельник',
         'news_anons': 'Понедельник - день, когда все начинается сначала. Для программистов это значит, '
                       'что нужно вспомнить, что они делали на прошлой неделе, разобраться в своем коде, '
                       'исправить ошибки и снова сесть за работу. Но не все так плохо, ведь есть способы сделать '
                       'понедельник легче и веселее. В этом посте мы поделимся с вами несколькими советами, '
                       'как пережить понедельник и не потерять мотивацию.'},
        {'publish_date': '05.08.2023',
         'news_header': 'Как программисты выбирают имена для своих детей',
         'news_anons': 'Программисты - люди творческие и неординарные, поэтому они не хотят давать своим детям '
                       'обычные имена. Они ищут вдохновение в своей профессии, в науке, в культуре и в интернете. '
                       'Иногда их выбор может быть неожиданным или забавным для окружающих. В этом посте мы собрали '
                       'самые необычные имена, которые программисты давали своим детям.'},
        {'publish_date': '07.08.2023',
         'news_header': 'Как программисты отмечают свой день рождения',
         'news_anons': 'День рождения - это особый день для каждого человека, и каждый хочет отметить его по-своему. '
                       'Программисты не исключение, они тоже любят праздновать свой день рождения, но у них свои '
                       'традиции и привычки. Они могут устроить вечеринку с коллегами, заказать торт с кодом или '
                       'логотипом своей компании, подарить себе новый гаджет или курс по программированию. '
                       'В этом посте мы расскажем вам о самых интересных и забавных способах, как программисты '
                       'отмечают свой день рождения.'},
        {'publish_date': '09.08.2023',
         'news_header': 'Как программисты общаются с животными',
         'news_anons': 'Программисты - это не только люди, которые пишут код и создают приложения. Они также любят '
                       'животных и хотят с ними общаться. Но как программисты могут понять язык животных и научить '
                       'их чему-то новому? Оказывается, что есть специальные приложения и устройства, которые '
                       'помогают программистам взаимодействовать с животными. В этом посте мы покажем вам самые '
                       'удивительные и креативные примеры, как программисты общаются с животными.'},
    ]

    return render_template('news.html', menu_items=menu_items, current_path=request.path,
                           title=title_html, context=site_news)


@app.route('/about/')
def about():
    title_html = 'О нас'
    content = """
   Космонавты - это люди, которые летают в космосе и делают там всякие интересные вещи. 
   Они видят звезды, планеты и кометы. Они встречаются с инопланетянами и общаются с ними на языке жестов. 
   Они играют в футбол, шахматы и прятки в невесомости. Они едят сухофрукты, печенье и мороженое из тюбиков. 
   Они спят в специальных мешках, которые не падают с потолка. 
   Космонавты - это веселые, умные и отважные люди, которые любят свою работу и свою планету."""
    return render_template('about.html', menu_items=menu_items, current_path=request.path,
                           title=title_html, context=content)


@app.route('/contact/')
def contact():
    title_html = 'Контактная информация'
    contacts = {
        "name": "Arthur Dent",
        "email": "arthur.dent@earth.com",
        "phone": "+44 1234 5678",
        "planet": "Earth (destroyed)",
        "system": "Sun",
        "ship": "Heart of Gold",
        "continent": "Europe",
        "country": "United Kingdom",
        "region": "England",
        "city": "London"
    }

    return render_template('contact.html', menu_items=menu_items, current_path=request.path,
                           title=title_html, contacts=contacts)


marketplace_dict = [
    {'category': 'Одежда',
     'url': 'cloth',
     'description': 'Описание одежды',
     'content': [
         {'name': 'Костюм', 'description': 'Брючный костюм из 3х элементов', 'price': '42'},
         {'name': 'Рубашка', 'description': 'Рубашка размер 44', 'price': '22'},
         {'name': 'Рубашка', 'description': 'Рубашка размер 46', 'price': '22'},
     ]
     },
    {'category': 'Обувь', 'url': 'shoes', 'description': '',
     'content': [
         {'name': 'Башмак', 'description': 'Левый башмак, размер 55 ', 'price': '122'},
     ]},
    {'category': 'Куртки', 'url': 'jackets', 'description': '',
     'content': []
     },
]


@app.route('/marketplace/')
def marketplace():
    title_html = 'Маркетплейс'
    return render_template('marketplace.html', menu_items=menu_items, title=title_html,
                           context=marketplace_dict, current_path=request.path, )


@app.route('/marketplace/<product>/')
def product(product: str):
    title_html = f'Купи {next((item["category"] for item in marketplace_dict if item["url"] == product), None)}'

    return render_template('product.html', menu_items=menu_items, title=title_html,
                           context=marketplace_dict, current_path=request.path, product=product)


if __name__ == '__main__':
    app.run(debug=True)