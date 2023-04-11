
from flet import *



def main(page: Page):
    appbar = AppBar(
        title=Text("My app", size=30, color='white'),
        bgcolor='blue'
    )

    content_1 = Container(
        content=Column([
            Text(
                'Hello From My App', size=40
            )
        ])
    )
    page.add(appbar,content_1)


flet.app(target=main)
