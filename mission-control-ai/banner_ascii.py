import argparse
import pyfiglet

from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()


def banner_padrao():

    linha1 = pyfiglet.figlet_format(
        "Global Solution",
        font="ansi_shadow"
    )

    linha2 = pyfiglet.figlet_format(
        "Mission Control AI",
        font="ansi_shadow"
    )

    console.print(
        Align.center(
            Text(
                linha1,
                style="bold #A855F7"
            )
        )
    )

    console.print(
        Align.center(
            Text(
                linha2,
                style="bold #06B6D4"
            )
        )
    )

    console.print(
        Align.center(
            Text(
                "── 2026.1 · Prompt Engineering and AI · FIAP ──",
                style="italic #8484A0"
            )
        )
    )


def listar_fontes():

    fontes = pyfiglet.FigletFont.getFonts()

    for fonte in fontes:
        print(fonte)


def testar_fonte(fonte, texto):

    try:

        banner = pyfiglet.figlet_format(
            texto,
            font=fonte
        )

        console.print(
            Align.center(
                Text(
                    banner,
                    style="bold #06B6D4"
                )
            )
        )

    except:
        console.print(
            "[red]Fonte inválida.[/red]"
        )


def demo():

    fontes_demo = [
        "slant",
        "standard",
        "doom",
        "big",
        "digital",
        "small",
        "smslant",
        "ansi_shadow"
    ]

    for fonte in fontes_demo:

        console.print(
            f"\n[bold magenta]Fonte:[/bold magenta] {fonte}\n"
        )

        banner = pyfiglet.figlet_format(
            "Mission Control AI",
            font=fonte
        )

        console.print(
            Align.center(
                Text(
                    banner,
                    style="bold #06B6D4"
                )
            )
        )


parser = argparse.ArgumentParser()

parser.add_argument(
    "-fonts",
    action="store_true"
)

parser.add_argument(
    "-font",
    type=str
)

parser.add_argument(
    "-text",
    type=str
)

parser.add_argument(
    "-demo",
    action="store_true"
)

args = parser.parse_args()


if args.fonts:

    listar_fontes()

elif args.demo:

    demo()

elif args.font and args.text:

    testar_fonte(
        args.font,
        args.text
    )

else:

    banner_padrao()