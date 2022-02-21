import pytest


def test_get_posts(authorized_user, test_posts):
    res = authorized_user.get("/posts/")
    assert res.status_code == 200


def test_get_post(authorized_user, test_posts):
    res = authorized_user.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 200


def test_not_exists_post(authorized_user):
    res = authorized_user.get("/posts/888888")
    assert res.status_code == 404


@pytest.mark.parametrize("title, content, published", [
    ("fav music", "cannibal corpse", True),
    ("bad day", "cool story", True),
    ("awesome architecture", "buildings", False),
])
def test_create_post(authorized_user, test_user, title, content, published):
    res = authorized_user.post("/posts/", json={"title": title, "content": content, "published": published})
    assert res.status_code == 201
