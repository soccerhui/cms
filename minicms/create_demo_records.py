#coding:utf-8

'''
create some records for demo database
'''

from minicms.wsgi import *
from news.models import  Column, Article

def main():
    colunms_urls = [
        ('体育新闻', 'sports'),
        ('社会新闻', 'society'),
        ('科技新闻', 'tech'),
    ]

    for colunm_name, url in colunms_urls:
        c = Column.objects.get_or_create(name=colunm_name, slug=url)[0]

        #创建10篇新闻
        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title = '{}_{}'.format(colunm_name, i),
                slug='article={}'.format(i),
                content='新闻详细内容： {} {}'.format(colunm_name, i)
            )[0]

            article.column.add(c)

if __name__ == '__main__':
    main()
    print("done!")
