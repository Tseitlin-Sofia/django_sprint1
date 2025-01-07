def test_blog_posts(posts):
    try:
        from blog.views import POSTS as solution_posts
    except Exception as e:
        raise AssertionError(
            'При импорте списка `POSTS` из файла `blog/views.py` '
            f'произошла ошибка: {e}') from e
    assert solution_posts == posts, (
        'Убедитесь, что список с постами `POSTS` из файла `blog/views.py` '
        'соответствуют списку из задания.')
