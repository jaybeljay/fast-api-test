import pytest


def test_get_posts(authorized_user, test_posts):
    res = authorized_user.get("/posts/")
    assert res.status_code == 200


def test_get_post(authorized_user, test_posts):
    res = authorized_user.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 200


def test_not_exists_post(authorized_user, test_posts):
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


def test_unauthorized_user_create_post(client):
    res = client.post("/posts/", json={"title": "giegje", "content": "kjfbjngw", "published": False})
    assert res.status_code == 401


def test_delete_post(authorized_user, test_posts):
    res = authorized_user.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_unauthorized_user_delete_post(client, test_posts):
    res = client.delete(f"/posts/f{test_posts[0].id}")
    assert res.status_code == 401


def test_update_post(authorized_user, test_posts):
    res = authorized_user.put(f"/posts/{test_posts[0].id}", json={"title": "giegje", "content": "kjfbjngw"})
    assert res.status_code == 200
