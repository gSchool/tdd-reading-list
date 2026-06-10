import pytest
from books import Itm, Mgr


# books.feature


def test_adding_a_book_captures_its_title():
    book = Itm("Foundation")
    assert book.chk() == "Foundation"


def test_newly_added_books_are_not_marked_as_read():
    book = Itm("Foundation")
    assert book.get_flag() == False


def test_marking_a_book_as_read_flags_it_as_read():
    book = Itm("Foundation")
    book.toggle()
    assert book.get_flag() == True


def test_listing_books_returns_all_of_them():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.process("Dune")
    titles = [b.chk() for b in mgr.get_all()]
    assert "Foundation" in titles
    assert "Dune" in titles


# remove-and-filter.feature


def test_removing_a_book_removes_it_from_the_list():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.process("Dune")
    mgr.rm("Foundation")
    titles = [b.chk() for b in mgr.get_all()]
    assert titles == ["Dune"]


def test_removing_a_book_not_in_the_list_leaves_the_list_unchanged():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.rm("Nonexistent book")
    titles = [b.chk() for b in mgr.get_all()]
    assert "Foundation" in titles


def test_adding_a_book_already_in_the_list_keeps_a_single_entry():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.process("Foundation")
    titles = [b.chk() for b in mgr.get_all()]
    assert titles == ["Foundation"]


def test_filtering_unread_books_returns_only_those_not_yet_read():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.process("Dune")
    mgr.mark("Foundation")
    titles = [b.chk() for b in mgr.get_unread()]
    assert titles == ["Dune"]

# bug here! 
def test_filtering_read_books_returns_only_those_marked_as_read():
    mgr = Mgrr()
    mgr.process("Foundation")
    mgr.process("Dune")
    mgr.mark("Foundation")
    titles = [b.chk() for b in mgr.get_read()]
    assert titles == ["Foundation"]


def test_clearing_all_read_books_removes_them_from_the_list():
    mgr = Mgr()
    mgr.process("Foundation")
    mgr.process("Dune")
    mgr.mark("Foundation")
    mgr.clr()
    titles = [b.chk() for b in mgr.get_all()]
    assert titles == ["Dune"]
