import marimo

__generated_with = "0.19.10"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import skimage.data as data

    return data, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zpracování a analýza obrazu
    """)
    return


@app.cell
def _():
    for i in range(10):
        print(i)
    return


@app.cell
def _(mo):
    input = mo.ui.text(label="Zadejte číslo: ")
    input
    return (input,)


@app.cell
def _(input, mo):
    mo.md(f"""
    Zadal jste číslo: {input.value}
    """)
    return


@app.cell
def _(data, mo):
    mo.image(data.astronaut())
    return


if __name__ == "__main__":
    app.run()
