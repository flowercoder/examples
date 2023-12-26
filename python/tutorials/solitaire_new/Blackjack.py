import flet


def main(page: flet.Page):
    st = flet.Stack(
        controls=[
            flet.Image(
                src=f"https://picsum.photos/300/300 ", width=300, height=300, fit=flet.ImageFit.CONTAIN,
            ), flet.Row(

                controls=[
                    flet.Text(
                        "Image title", color="white", size=40, weight="bold", opacity=0.5,
                    )
                ], alignment=flet.MainAxisAlignment.CENTER,
            ),
        ], width=300, height=300,
    )


page.add(st)
flet.app(target=main)
