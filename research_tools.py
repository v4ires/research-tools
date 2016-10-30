import os
import requests
import lxml.html

def download_href(url, file_format):
    print('Loading the url from: "{}"'.format(url))
    response = requests.get(url)
    dom = lxml.html.fromstring(response.content)
    file_names = [file_name for file_name in dom.xpath('//a/@href') if file_name[-2:] == file_format]

    download_directory = 'download'
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    for file_name in file_names:
        url += "{}".format(file_name)
        arch = os.path.join(download_directory, file_name)
        if os.path.exists(arch):
            print('The file "{}" already exists, and is not going to download'.format(file_name))
        else:
            with open(arch, 'wb') as the_file:
                print("Wait, downloading '{file_name}'".format(file_name=file_name))
                r = requests.get(url)
                the_file.write(r.content)
            print('The file "{}" has been download, and saved in: {}'.format(file_name, arch))