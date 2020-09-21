from ..requests import get_news,search_news,sources_news
from flask import render_template,request,redirect,url_for
from . import main



# Views
@main.route('/')
def index():

    top_headlines = get_news("top-headlines")

    title = 'Home - Welcome to the latest news Website'

    search_news = request.args.get("everything_query")
    search_sources = request.args.get("news_sources")
    if search_news:
        return redirect(url_for(".search", news_item=search_news))
    elif search_sources:
        return redirect(url_for(".sources", sources_name=search_sources))
    else:
        return render_template('navbar.html', title=title, top=top_headlines)

@main.route('/search/<everything>')
def search(everything):

    news_name_list = everything.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f"search results for {everything}"

    return render_template('search.html',news=searched_news,title=title)


@main.route("/sources/",methods=["POST"])
def sources():
    keyword = request.form['keyword']
    sources = sources_news(q=keyword, language='en',country='us')
    title = f"{sources} news "

    return render_template("sources.html", sources=sources['articles'],title=title)