from app.tools import crawler

def test_crawler():
    assert len(crawler.get_images()) > 0