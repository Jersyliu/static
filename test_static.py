import os
import subprocess
import tempfile
from bs4 import BeautifulSoup

def check_file(path, title, body):
    soup = BeautifulSoup(open(path), 'html.parser')
    titletag = soup.find('title')
    assert titletag.string.strip() == title
    bodytag = soup.find('body')
    assert bodytag.string.strip() == body

def test_simple():
    with tempfile.TemporaryDirectory(suffix='static') as tmpdirname:
        result = subprocess.run(['./generate.sh', 'examples/simple/', tmpdirname])
        assert result.returncode == 0

        files = os.listdir(tmpdirname)
        files.sort()
        assert files == ['post1.html', 'post2.html']

        # check that files have appropriate content

        potst1path = os.path.join(tmpdirname, files[0])
        check_file(potst1path, "Post 1 Title", "This is the body of Post 1.")

        post2path = os.path.join(tmpdirname, files[1])
        check_file(post2path, "Post 2 Title", "This is the body of Post 2.")
