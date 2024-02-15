from typing import Any


class RenderList:
    def __init__(self, type_list) -> None:
        self.type_list = type_list if type_list in {'ul', 'ol'} else "ul"

    def __call__(self, lst) -> Any:
        if not lst:
            return ''

        html = f"<{self.type_list}>\n"
        for item in lst:
            html += f"<li>{item}</li>\n"
        html += f"</{self.type_list}>"
        return html


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
