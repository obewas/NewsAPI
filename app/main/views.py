from ..requests import get_news,search_news,sources_news
from flask import render_template,request,redirect,url_for
from . import main



# Views
@main.route('/')
def index():

    top_headlines = get_news("top-headlines")

    title = 'Home - Welcome to the latest news Website'

    search_news = request.args.get("news_query")
    search_sources = request.args.get("news_sources")
    if search_news:
        return redirect(url_for(".search", news_name=search_news))
    elif search_sources:
        return redirect(url_for(".sources", sources_name=search_sources))
    else:
        return render_template('index.html', title=title, top=top_headlines)

@main.route('/search/<news_name>')
def search(news_name):

    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f"search results for {news_name}"

    return render_template('search.html',news=searched_news)


@main.route("/sources")
def sources():

    sources = sources_news()
    title = f"{sources} news "

    return render_template("sources.html", sources=sources)