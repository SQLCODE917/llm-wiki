from typing import Any

from llmwiki.pdf.layout_lines import page_words


class _Page:
    def __init__(self) -> None:
        self.sort_arg: bool | None = None

    def get_text(self, kind: str, *, sort: bool) -> list[Any]:
        assert kind == "words"
        self.sort_arg = sort
        return [
            (30, 10, 40, 20, "second"),
            (None,),
            (10, 10, 20, 20, "first"),
            (50, 10, 45, 20, "bad"),
            (10, 30, 20, 40, " "),
        ]


def test_page_words_filters_invalid_rows_and_sorts_without_pymupdf_sort() -> None:
    page = _Page()

    words = page_words(page)

    assert page.sort_arg is False
    assert [word.text for word in words] == ["first", "second"]
