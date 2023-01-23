import angreal

green = "\33[32m"
red = "\33[31m"
end = "\33[0m"

@angreal.command(name="echo", about="an echo replacement")
@angreal.argument(name="phrase", help="the phrase to echo", required=True)
@angreal.argument(name="color", long="color", short='c', help="apply a color to the echo phrase")
def task_echo(phrase,color=None):

    if color=="red":
        print(red + phrase + end )
        return
    if color=="green":
        print(green + phrase + end )
        return
    print(phrase)