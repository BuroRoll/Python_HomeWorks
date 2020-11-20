import urllib.request
from threading import Thread


# Скачивание файлов в несколько потоков
def download_file(link, file_format=''):
    filename = link.split('/')[-1] + file_format
    file = open(filename, 'wb')
    with urllib.request.urlopen(link) as url:
        s = url.read()
        file.write(s)


t1 = Thread(target=download_file, args=('https://habrastorage.org/webt/bw/sc/8n/bwsc8np51ystvqsvlchcn-ukvwi.jpeg',))
t2 = Thread(target=download_file,
            args=('https://dev.by/storage/images/24/42/54/83/derived/5db4ac23270d1330580e8b7068ad350f.jpg',))
t3 = Thread(target=download_file, args=('https://tayga.info/media/images/news/159/159078/thumb.jpg',))
t4 = Thread(target=download_file,
            args=('https://dev-gang.ru/static/storage/44100770647918351649702322357495907235.jpeg',))
t5 = Thread(target=download_file, args=('http://5.45.70.162/parse/d.rutor.org/download/684242', '.torrent'))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
