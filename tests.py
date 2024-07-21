import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize(
        'name',
        [
            '!',
            'Ёж',
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ])
    def test_add_new_book_checking_name_lenght_more_zero_and_less_forty_one(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {name : ''}

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'Что делать, если ваш кот хочет вас убить?'
        ])
    def test_add_new_book_checking_name_lenght_zero_and_more_forty(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre != {name: ''}

    def test_set_book_genre_add_book_and_set_book_genre_from_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        assert collector.books_genre == {'Профессия: ведьма': 'Детективы'}

    def test_set_book_genre_add_book_and_set_book_genre_not_from_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Фентези')
        assert collector.books_genre != {'Профессия: ведьма': 'Фентези'}

    def test_set_book_genre_do_not_add_book_and_set_book_genre_from_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Профессия: ведьма','Детективы')
        assert collector.books_genre != {'Профессия: ведьма': 'Детективы'}

    def test_get_book_genre_add_book_set_book_genre_from_genre_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        assert collector.get_book_genre('Профессия: ведьма') == 'Детективы'

    def test_get_book_genre_add_book_do_not_set_book_genre_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        assert collector.get_book_genre('Профессия: ведьма') == ''

    def test_get_book_genre_do_not_add_book_get_book_genre_by_name(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Профессия: ведьма') == None

    def test_get_books_with_specific_genre_add_books_different_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_new_book('Барраяр')
        collector.set_book_genre('Барраяр', 'Фантастика')
        collector.add_new_book('Три закона робототехники')
        collector.set_book_genre('Три закона робототехники', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre_getting_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_new_book('Барраяр')
        collector.set_book_genre('Барраяр', 'Фантастика')
        assert collector.get_books_genre() == {'Профессия: ведьма':'Детективы','Барраяр':'Фантастика'}

    def test_get_books_for_children_add_books_different_genre_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_new_book('Барраяр')
        collector.set_book_genre('Барраяр', 'Фантастика')
        collector.add_new_book('Три закона робототехники')
        collector.set_book_genre('Три закона робототехники', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Ужасы')
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_new_books_two_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_new_book('Барраяр')
        collector.set_book_genre('Барраяр', 'Фантастика')
        collector.add_new_book('Три закона робототехники')
        collector.set_book_genre('Три закона робототехники', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Ужасы')
        collector.add_book_in_favorites('Профессия: ведьма')
        collector.add_book_in_favorites('Барраяр')
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_add_new_books_two_books_in_favorites_delete_one(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_new_book('Барраяр')
        collector.set_book_genre('Барраяр', 'Фантастика')
        collector.add_new_book('Три закона робототехники')
        collector.set_book_genre('Три закона робототехники', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Ужасы')
        collector.add_book_in_favorites('Профессия: ведьма')
        collector.add_book_in_favorites('Барраяр')
        collector.delete_book_from_favorites('Барраяр')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_add_new_book_in_favorites_get_favorite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Профессия: ведьма')
        collector.set_book_genre('Профессия: ведьма', 'Детективы')
        collector.add_book_in_favorites('Профессия: ведьма')
        assert collector.get_list_of_favorites_books() == ['Профессия: ведьма']