def test_vote(authorized_user, test_posts):
    res = authorized_user.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 201


def test_vote_twice(authorized_user, test_posts, create_test_vote):
    res = authorized_user.post("/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 409


def test_delete_vote(authorized_user, test_posts, create_test_vote):
    res = authorized_user.post("/vote/", json={"post_id": test_posts[0].id, "dir": 0})
    assert res.status_code == 201
